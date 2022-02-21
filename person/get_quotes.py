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
    "განუცხადა",
    "აცხადებს",
    "ამბობს",
    "ნათქვამია",
    "თქვა",
    "წერს",
    "ვკითხულობთ",
    "იკითხა",
    "დაამატა",
    "მოიწერა",
    "იწერება",
    "ნახსენებია",
    "აღნიშნა",
    "აღნიშნულია",
    "აღნიშნავს",
    "ამის შესახებ",
    "მიმართა",
    "ასე ეხმიანება",
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


def get_normalized_surname_if_surname(word):
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


    result explanation:
        each identified quote with person who said that, are in a separate
        dictionary with keys "person" and "quote" accordingly.

        match_case key denotes which method resulted this quote identification,
        their extraction logics are different and more/less reliable, so having
        this information can be useful to make decisions in our specific use case.

        currently match_case can be number number from 1 to 2,
        with following extraction logics:

            1. if match_case is 1, quote found in text, enclosed in common
            quote symbols, and was directly followed by word like said/wrote(I mean, in Georgian) and
            full person name and surname.

                . example input string:

                '''
                "ტესტი", - განაცხადა გიორგი გიორგაძემ
                '''

                . example output:
                     [
                        {
                            'person': 'გიორგი გიორგაძე',
                            'quote': 'ტესტი',
                            'match_case': 1,
                        }
                    ]
            2. if match_case is 2, if person extraction found just 1 person(name_surname) in
            full text, all quotes will be thought to be from this person. Quotes are identified
            the same way as in previous case - it should be followed with one of
            quote-ending words, to avoid false positives for just quoted entities.

                . example input string:

                '''
                    გუშინ გიორგი გიორგაძემ რაღაც გააკეთა.
                    'მე გუშინ გავაკეთე რაღაც' - ნათქვამია მის განცხადებაში.
                    'გუშინ წინაც ვფიქრობდი, მაგრამ გადავიფიქრე', დაამატა გიორგიმ.
                '''

                . example output:

                    [
                        {
                            'person': 'გიორგი გიორგაძე',
                            'quote': 'მე გუშინ გავაკეთე რაღაც',
                            'match_case': 2,
                        },
                        {
                            'person': 'გიორგი გიორგაძე',
                            'quote': 'გუშინ წინაც ვფიქრობდი, მაგრამ გადავიფიქრე',
                            'match_case': 2,
                        },
                    ]

        Matches are deduplicated before returning, leaving
        matches that correspond to lower match_case number,
        as they are usually more reliable.

    For example real input/outputs see test files/do your testing.




    """
    text = _preprocess_text(text)

    text, quotes_decoder = _encode_quotes_in_quotes(text)

    result = []
    parts_splitted_by_quote_chars = re.split("|".join(QUOTE_LIKE_CHARS), text)

    # to avoid incorrect matches when quote itself starts with
    # person name and surname, so we may mistakenly match previous
    # part without this checks
    quote_text_indices_in_splitted_parts = set()
    # start_i = 0 if text[0] in QUOTE_LIKE_CHARS else 1
    start_i = 1

    while start_i < len(parts_splitted_by_quote_chars):
        quote_text_indices_in_splitted_parts.add(start_i)
        start_i += 2

    normalized_tokens_by_splitted_parts = [
        _tokenize_text(part) for part in parts_splitted_by_quote_chars
    ]

    if v:
        print("text:", text)
        print(
            "parts_splitted_by_quote_chars:",
            parts_splitted_by_quote_chars,
        )
        print()
        print(
            "normalized_tokens_by_splitted_parts:",
            normalized_tokens_by_splitted_parts,
        )
        print()
        print(
            "quote_text_indices_in_splitted_parts:",
            quote_text_indices_in_splitted_parts,
        )
        print()

    # cases N1 - basic | quoted text followed with person name and surname
    """
        ex: 
            "ტესტი", - განაცხადა გიორგი გიორგაძემ
            "დროა", - გიორგი გიორგაძე
    """

    # currently most reliable solution.
    # split with quote and quote-like symbols and see
    # where possible quote-ending phrase is followed with person name_surname.
    # if such a case/cases found, it should be quote of following person.
    # also match cases when no possible quote_ending_phrase is mentioned,
    # but person name_surname is mentioned directly afterwards

    for index in range(1, len(parts_splitted_by_quote_chars)):  # skip first one
        if index in quote_text_indices_in_splitted_parts:
            continue

        tokens = normalized_tokens_by_splitted_parts[index]

        if len(tokens) < 2:
            continue

        if len(tokens) > 2 and tokens[0] in QUOTE_ENDING_PHRASES:
            author_candidate = extract_persons(f"{tokens[1]} {tokens[2]}")

            if author_candidate:

                result.append(
                    {
                        "person": author_candidate[0],
                        "quote": parts_splitted_by_quote_chars[index - 1],
                        "match_case": 1,
                    }
                )
        else:
            author_candidate = extract_persons(f"{tokens[0]} {tokens[1]}")

            if author_candidate:
                result.append(
                    {
                        "person": author_candidate[0],
                        "quote": parts_splitted_by_quote_chars[index - 1],
                        "match_case": 1,
                    }
                )

    # case 2
    # not so much reliable solution, but
    # with many possible results if correct.
    # useful when article/text is mostly on one person, with lots of possible quotes.
    # check, if full text has just one person mentioned
    # assume that any quoted text followed by possible quote-ending-phrase
    # is from this person.
    # only quote-ending-phrases,
    # because quoted texts may be some entities themself,
    # not quotes of someone
    """
    გუშინ გიორგი გიორგაძემ რაღაც გააკეთა.

    "მე გუშინ გავაკეთე რაღაც" - ნათქვამია მის განცხადებაში.

    "გუშინ წინაც ვფიქრობდი, მაგრამ გადავიფიქრე", დაამატა გიორგიმ.
    """

    # so it after case 1 from start, to make code much clearer.

    # extract from non-quote parts, as sometimes people
    # mention other persons in quotes, but they are not actual persons
    # who say something in the text
    text_to_extract_persons_from = " ".join(
        [
            i
            for index, i in enumerate(parts_splitted_by_quote_chars)
            if index not in quote_text_indices_in_splitted_parts
        ]
    )
    extracted_persons = extract_persons(text_to_extract_persons_from)

    if v:
        print()
        print("extracted_persons", extracted_persons)
        print()

    if len(extracted_persons) == 1:

        for index in range(
            1, len(parts_splitted_by_quote_chars)
        ):  # skip first one
            if index in quote_text_indices_in_splitted_parts:
                continue

            # breakpoint()
            tokens = normalized_tokens_by_splitted_parts[index]

            if len(tokens) == 0:
                continue

            if tokens[0] in QUOTE_ENDING_PHRASES or (
                len(tokens) > 1
                and f"{tokens[0]} {tokens[1]}" in QUOTE_ENDING_PHRASES
            ):
                result.append(
                    {
                        "person": extracted_persons[0],
                        "quote": parts_splitted_by_quote_chars[index - 1],
                        "match_case": 2,
                    }
                )
    # case 3
    # at least 1 person identified on page and after some quote-ending-like text
    # we have just the surname part of a person, without name.
    # in this case, check if this is the surname of already fully identified person,
    # consider that this is quote of that person
    # ex:
    """
    გიორგი გიორგაძე დღეს რაღაცას აკეთებს.

    "მე რაღაცას ვაკეთებ" - განაცხადა გიორგაძემ
    """
    if len(extracted_persons) > 0:
        for index in range(
            1, len(parts_splitted_by_quote_chars)
        ):  # skip first one
            if index in quote_text_indices_in_splitted_parts:
                continue

            tokens = normalized_tokens_by_splitted_parts[index]

            if len(tokens) == 0:
                continue

            if tokens[0] not in QUOTE_ENDING_PHRASES:
                continue

            # breakpoint()
            normalized_possible_surname = get_normalized_surname_if_surname(
                tokens[1]
            )

            if not normalized_possible_surname:
                continue

            # if we have only one unique person name_surname on page with given surname,
            # assume that this quote is also from this person name_surname
            possible_person_matches = [
                i
                for i in extracted_persons
                if i.endswith(f" {normalized_possible_surname}")
            ]

            if len(possible_person_matches) == 1:
                result.append(
                    {
                        "person": possible_person_matches[0],
                        "quote": parts_splitted_by_quote_chars[index - 1],
                        "match_case": 3,
                    }
                )

    # remove duplicates | may be subject of reformat later
    deduplicated_result = []
    seen_person_and_quotes = set()

    for i in result:
        key = (i["person"], i["quote"])

        if key not in seen_person_and_quotes:
            seen_person_and_quotes.add(key)

            deduplicated_result.append(i)

    # decode - will slow things a lot, but may be worth it, as
    # we do not want to change original text much, may optimize later...
    for i in result:
        for encoded_char, original_char in quotes_decoder.items():
            i["quote"] = i["quote"].replace(encoded_char, original_char)

    return deduplicated_result
