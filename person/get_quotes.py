"""
Todo:
    add most accurate new match_case, which
    will match only when we have possible quote-ending-phrase followed with 
    name_surname in base form "სახელობითი ბრუნვა", or
    in second form, which indicates that this text is said/written
    by that person. 
"""

import re
from string import punctuation
from uuid import uuid4


from . import SURNAMES
from .extract import extract_persons
from .util import normalize_surname

QUOTE_LIKE_CHARS = [
    '"',  # basic double quote
    "'",  # basic single quote
    "“",  # quote start sign
    "„",  # quote end sign
    "’’",  # WTF (What the function :) ?
]

# because of quote in quotes replacement
for i in QUOTE_LIKE_CHARS:
    assert "-" not in i

QUOTE_ENDING_PHRASES = {
    "განაცხადა",
    "განგვიცხადა",
    "განუცხადა",
    "აცხადებს",
    "ამბობს",
    "ნათქვამია",
    "თქვა",
    "მითხრა",
    "წერს",
    "მწერს",
    "ვკითხულობთ",
    "წერია",
    "იკითხა",
    "დაამატა",
    "მოიწერა",
    "იწერება",
    "ნახსენებია",
    "აღნიშნა",
    "აღნიშნულია",
    "აღნიშნავს",
    "მიმართა",
    "ეხმიანება",
}


_is_geo_letter_or_digit = lambda l: 4304 <= ord(l) <= 4336 or l.isdigit()


def _tokenize_text(
    raw_text,
):
    # leave georgian letters and replace all other symbol with space
    text = []
    for c in raw_text:
        # letter is georgian
        if _is_geo_letter_or_digit(c):
            text.append(c)
        else:
            text.append(" ")

    text = "".join(text)

    # rm more than 1 spaces between and get resulting list
    text = text.split()

    return text


def _get_normalized_surname_if_surname(word):
    normalized = normalize_surname(word)

    if normalized in SURNAMES:
        return normalized
    return False


def _encode_quotes_in_quotes(raw_text):
    """
    Sometimes we have texts like this:

    "შეგახსენებთ, რომ რუსეთი მთელი თავისი ისტორიის განმავლობაში არასდროს არავის
    დასხმია თავს( მტყუნის? :-) - ავტორის შენიშვნა). რუსეთი, რომელმაც ამდენი ომი გადაიტანა,
    უკანასკნელი ქვეყანაა ევროპაში, რომელსაც საერთოდ სიტყვა "ომის" წარმოთქმა სურს".

    Here we have a quote with quote inside of it, so our current basic
    splitting by possible quotes approach will fail and think that first quote ends when
    next quoted text starts (3-rd last word).

    To make important step towards fixing this problem, lets encode quotes
    in parts where main quote is not yet finished, with some random string,
    so that out splitting method will continue working as these words will not
    have valid quote-like strings. Of course we replace this encoded strings with
    their basic quotes form at the end.

    How to decide if specific quote is not the one that ends currently
    started quote? According to our observation, real quote endings most of the
    time happen without space between letter and quote mark, so if we have
    any quote-like character after space(not directly followed after word, without space)
    and are in a place where quoting started somewhere and not ended yet,
    we encode that quote mark and its ending pair.
    """

    text = []

    in_quoted_part = False
    encode_next_quote_char = False
    decoder = {}  # what encoded string replaces what quote mark

    for index, c in enumerate(raw_text):
        if c not in QUOTE_LIKE_CHARS:
            text.append(c)
            continue

        if encode_next_quote_char:
            encoded_char = str(uuid4())
            text.append(encoded_char)

            decoder[encoded_char] = c

            encode_next_quote_char = False
            continue

        if not in_quoted_part:
            in_quoted_part = True
            text.append(c)
        else:
            # quote does not end previous quote
            if (
                not _is_geo_letter_or_digit(raw_text[index - 1])
                and raw_text[index - 1] not in punctuation
            ):
                encode_next_quote_char = True

                encoded_char = str(uuid4())
                decoder[encoded_char] = c
                text.append(encoded_char)
            else:
                in_quoted_part = False
                text.append(c)

    text = "".join(text)

    return text, decoder


def _preprocess_text(text):
    # rm newlines
    text = re.sub("\n", " ", text)

    # rm multiple continuous spaces
    text = " ".join(text.split())

    return text


def _decode_result(result, quotes_decoder):
    # decode - will slow things a lot, but may be worth it, as
    # we do not want to change original text much, may optimize later...
    for i in result:
        for encoded_char, original_char in quotes_decoder.items():
            i["quote"] = i["quote"].replace(encoded_char, original_char)

    return result


def _deduplicate_result(result):
    deduplicated_result = []

    seen_person_and_quotes = set()

    for i in result:
        key = (i["person"], i["quote"])

        if key not in seen_person_and_quotes:
            seen_person_and_quotes.add(key)

            deduplicated_result.append(i)

    return deduplicated_result


def get_quotes(text, v=0):
    """
    extract quotes and persons who say that in given Georgian text.

    Before extraction from text starts, any newline and multiple
    continuous space characters are replaced with just one,
    no other normalization is done, like making sure quotes end with dots
    or something like that.

    result structure:
    [
        {
            "person": "person_1",
            "quote": "continuous_quote_1",
            "match_case": 1,
        },
        {
            "person": "person_2",
            "quote": "continuous_quote_2",
            "match_case": 2,
        },
        ...
    ]


    ------------------------------------------------------------------------
    result explanation:
    ------------------------------------------------------------------------
        each identified quote with person who said that, are in a separate
        dictionary with keys "person" and "quote" accordingly.

        match_case key denotes which method resulted this quote identification,
        their extraction logics are different and lower number means it is usually
        more realiable, so having this information can be useful to make decisions
        in our specific use case.

        From our testing, most of the time results with match_case < X(?)
        are good enough.

        ---------------------------------------------------------------------
            match_case explanation:
        ---------------------------------------------------------------------

                ----
                1.
                ----
                    "quote" -> quote_ending_string -> person_name_surname

                    ex:
                        "ტესტი", - განაცხადა გიორგი გიორგაძემ

                ----
                2.  person_name_surname: "quote"
                ----
                    ex:
                        გიორგი გიორგაძე: "ჩემთვის დიდი პატივია"

                ----
                3.
                ----
                    "quote" - quote_ending_string person_surname.
                    only one person was mentioned in full text with this surname

                    ex:
                        გიორგი გიორგაძე დღეს ილაპარაკებს.
                        "ვილაპარაკე", განაცხადა გიორგაძემ ჟურნალისტებთან.


    For example real input/outputs see test files/do your testing.
    """

    text = _preprocess_text(text)

    text, quotes_decoder = _encode_quotes_in_quotes(text)

    result = []
    parts_splitted_by_quote_chars = re.split("|".join(QUOTE_LIKE_CHARS), text)

    # { index_in_splitted_part: quote_text }
    quote_indices_and_texts = {}

    start_i = 1

    while start_i < len(parts_splitted_by_quote_chars):
        quote_indices_and_texts[start_i] = parts_splitted_by_quote_chars[start_i]
        start_i += 2

    normalized_splitted_parts = [
        _tokenize_text(part) for part in parts_splitted_by_quote_chars
    ]

    # to skip for next match_cases
    already_matched_quotes_indices = set()

    text_to_extract_persons_from = " ".join(
        [
            i
            for index, i in enumerate(parts_splitted_by_quote_chars)
            if index not in quote_indices_and_texts
        ]
    )
    extracted_persons = extract_persons(text_to_extract_persons_from)

    ####################################################

    """
        case 1 
        
        ex: 
            "ტესტი", - განაცხადა გიორგი გიორგაძემ
    """
    for quote_index, quote_text in quote_indices_and_texts.items():

        if quote_index in already_matched_quotes_indices:
            continue

        tokens = normalized_splitted_parts[quote_index + 1]

        if len(tokens) < 3 or tokens[0] not in QUOTE_ENDING_PHRASES:
            continue

        author_candidate = extract_persons(f"{tokens[1]} {tokens[2]}")

        if author_candidate:
            result.append(
                {
                    "person": author_candidate[0],
                    "quote": quote_text,
                    "match_case": 1,
                }
            )
            already_matched_quotes_indices.add(quote_index)

    """
        case 2

        ex:
            გიორგი გიორგაძე: "ჩემთვის დიდი პატივია"
    """
    for quote_index, quote_text in quote_indices_and_texts.items():

        if quote_index in already_matched_quotes_indices:
            continue

        prev_text = parts_splitted_by_quote_chars[quote_index - 1]

        if not prev_text.strip().endswith(":"):
            continue

        here_should_be_person_mentioned = " ".join(_tokenize_text(prev_text)[-2:])

        author_candidate = extract_persons(here_should_be_person_mentioned)

        if author_candidate:
            result.append(
                {
                    "person": author_candidate[0],
                    "quote": quote_text,
                    "match_case": 2,
                }
            )
            already_matched_quotes_indices.add(quote_index)

    """
    case 3
    
    ex:
        გიორგი გიორგაძე დღეს ილაპარაკებს.
        "ვილაპარაკე", განაცხადა გიორგაძემ ჟურნალისტებთან.

    """
    if len(extracted_persons) == 1:
        for quote_index, quote_text in quote_indices_and_texts.items():

            if quote_index in already_matched_quotes_indices:
                continue

            tokens = normalized_splitted_parts[quote_index + 1]

            if len(tokens) < 2 or tokens[0] not in QUOTE_ENDING_PHRASES:
                continue

            possible_surname = _get_normalized_surname_if_surname(tokens[1])

            if (
                possible_surname
                and possible_surname == extracted_persons[0].split()[-1]
            ):

                result.append(
                    {
                        "person": extracted_persons[0],
                        "quote": quote_text,
                        "match_case": 3,
                    }
                )
                already_matched_quotes_indices.add(quote_index)

    # # case 3
    # else:
    #     author_candidate = extract_persons(f"{tokens[0]} {tokens[1]}")

    #     if author_candidate:
    #         result.append(
    #             {
    #                 "person": author_candidate[0],
    #                 "quote": parts_splitted_by_quote_chars[index - 1],
    #                 "match_case": 3,
    #             }
    #         )

    # """
    # გუშინ გიორგი გიორგაძემ რაღაც გააკეთა.

    # "მე გუშინ გავაკეთე რაღაც" - ნათქვამია მის განცხადებაში.

    # "გუშინ წინაც ვფიქრობდი, მაგრამ გადავიფიქრე", დაამატა გიორგიმ.
    # """

    # # so it after case 1 from start, to make code much clearer.

    # # extract from non-quote parts, as sometimes people
    # # mention other persons in quotes, but they are not actual persons
    # # who say something in the text

    # if v:
    #     print()
    #     print("extracted_persons_in_non_quoted_text", extracted_persons)
    #     print()

    # if len(extracted_persons) == 1:

    #     for index in range(1, len(parts_splitted_by_quote_chars)):  # skip first one
    #         if index in quote_text_indices_in_splitted_parts:
    #             continue

    #         # breakpoint()
    #         tokens = normalized_splitted_parts[index]

    #         if len(tokens) == 0:
    #             continue

    #         if tokens[0] in QUOTE_ENDING_PHRASES or (
    #             len(tokens) > 1 and f"{tokens[0]} {tokens[1]}" in QUOTE_ENDING_PHRASES
    #         ):
    #             result.append(
    #                 {
    #                     "person": extracted_persons[0],
    #                     "quote": parts_splitted_by_quote_chars[index - 1],
    #                     "match_case": 4,
    #                 }
    #             )
    # # case 3
    # # at least 1 person identified on page and after some quote-ending-like text
    # # we have just the surname part of a person, without name.
    # # in this case, check if this is the surname of already fully identified person,
    # # consider that this is quote of that person
    # # ex:
    # """
    # გიორგი გიორგაძე დღეს რაღაცას აკეთებს.

    # "მე რაღაცას ვაკეთებ" - განაცხადა გიორგაძემ
    # """
    # if len(extracted_persons) > 0:
    #     for index in range(1, len(parts_splitted_by_quote_chars)):  # skip first one
    #         if index in quote_text_indices_in_splitted_parts:
    #             continue

    #         tokens = normalized_splitted_parts[index]

    #         if len(tokens) < 2:
    #             continue

    #         if tokens[0] not in QUOTE_ENDING_PHRASES:
    #             continue

    #         # breakpoint()
    #         normalized_possible_surname = _get_normalized_surname_if_surname(tokens[1])

    #         if not normalized_possible_surname:
    #             continue

    #         # if we have only one unique person name_surname on page with given surname,
    #         # assume that this quote is also from this person name_surname
    #         possible_person_matches = [
    #             i
    #             for i in extracted_persons
    #             if i.endswith(f" {normalized_possible_surname}")
    #         ]

    #         if len(possible_person_matches) == 1:
    #             result.append(
    #                 {
    #                     "person": possible_person_matches[0],
    #                     "quote": parts_splitted_by_quote_chars[index - 1],
    #                     "match_case": 2,
    #                 }
    #             )

    result = _decode_result(result, quotes_decoder)
    result = _deduplicate_result(result)

    return result


"""
    ######################
    # some new case ideas
    ######################
    ----
    .
    ----
        "quote" person_name_surname

        ex:
            "ტესტი" - გიორგი გიორგაძე
    ----
    .
    ----
        "quote" -> quote_ending_string
        only one person was mentioned in full text(exluding quoted parts)

    
    ----
    .
    ----
        person_name_surname -> quote_starting_string -> "quote"

        ex:
            გიორგი გიორგაძე წერს: "ტესტი"

    
    ----
    .
    ----
        "quote" -> quote_ending_string -> person_name_surname_somewhere_in_current_sentence

        ex:
            "ტესტი" ვკითხულობთ წერილში რომელიც გიორგი გიორგაძის მიერ დღეს გავრცელდა.


    ----
    .
    ----
        person_name_surname_somewhere_in_current_sentence -> quote_starting_string -> "quote"

        ex:
            ყოფილი მხატვარი გიორგი გიორგაძე მიმდინარე მოვლენებს ასე ეხმიანება: "ტესტი"

    ----
    .
    ----
        just_one_person_name_surname_somewhere_in_current_sentence_with_quote_starting_or_ending_prefix_suffix

        ex:
            "ტესტი ტესტობდა" გაისმა ხმა და გამოჩნდა გიორგი გიორგაძის ქუდი

    ----
    .
    ----
        all quotes(starting or ending with starting/ending appropriate strings)
        and just 1 person name_surname in current full text --> all these quotes are 
        said by this person
            ex:
                გიორგი გიორგაძე დაიბადა.
                "იყო და არა იყო რა" თქვა ვიღაცამ.


    #############################




"""
