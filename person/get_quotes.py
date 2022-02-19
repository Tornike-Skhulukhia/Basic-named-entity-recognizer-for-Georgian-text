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


from .extract import extract_persons

QUOTE_LIKE_CHARS = [
    '"',  # basic double quote
    "'",  # basic single quote
]

QUOTE_ENDING_PHRASES = {
    "განაცხადა",
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
    "აღნიშნულია",
    "აღნიშნავს",
}


def _tokenize_text(
    text,
):  # we can replace this method with just language-specific char-only extractions
    # rm punctuation marks
    text = re.sub("|".join([re.escape(i) for i in punctuation]), " ", text)

    # rm more than 1 spaces between and get resulting list
    text = text.split()

    return text


def _preprocess_text(text):
    # rm newlines
    text = re.sub("\n", " ", text)

    # rm multiple continuous spaces
    text = " ".join(text.split())

    return text


def get_quotes(text):
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

    result = []

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
    parts = re.split("|".join(QUOTE_LIKE_CHARS), text)

    for index in range(1, len(parts)):  # skip first one
        tokens = _tokenize_text(parts[index])

        if len(tokens) < 2:
            continue

        if len(tokens) > 2 and tokens[0] in QUOTE_ENDING_PHRASES:
            author_candidate = extract_persons(f"{tokens[1]} {tokens[2]}")

            if author_candidate:
                result.append(
                    {
                        "person": author_candidate[0],
                        "quote": parts[index - 1],
                        "match_case": 1,
                    }
                )
        else:
            author_candidate = extract_persons(f"{tokens[0]} {tokens[1]}")

            if author_candidate:
                result.append(
                    {
                        "person": author_candidate[0],
                        "quote": parts[index - 1],
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

    # so it after case 1 from start, to make code much clearer
    extracted_persons = extract_persons(text)

    if len(extracted_persons) == 1:
        parts = re.split("|".join(QUOTE_LIKE_CHARS), text)

        for index in range(1, len(parts)):  # skip first one
            tokens = _tokenize_text(parts[index])

            if len(tokens) == 0:
                continue

            if tokens[0] in QUOTE_ENDING_PHRASES:
                result.append(
                    {
                        "person": extracted_persons[0],
                        "quote": parts[index - 1],
                        "match_case": 2,
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

    return deduplicated_result
