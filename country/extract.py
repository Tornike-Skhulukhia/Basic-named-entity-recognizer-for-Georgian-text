import string

from . import COUNTRIES_EXTRACT_INFO, POPULATED_AREAS_EXTRACT_INFO

PUNCTUATION_SYMBOLS = set(string.punctuation)


def _is_a_match(i, unique_words, text):
    # is full word there?
    for full_word in i.get("possible_full_words", []):
        if full_word in unique_words:
            return True

    # is any word that starts with ... there?
    for word_should_start, spaces_num_in_word_should_start in zip(
        i["word_should_start"], i["_word_should_start_spaces_nums"]
    ):
        if spaces_num_in_word_should_start == 0:
            # if it is one word start
            for k in unique_words:
                if k.startswith(word_should_start):
                    return True
        else:
            # for more than 1 word starts (like "შეერთებულ შტატებ") we have to go through full text
            if word_should_start in text:
                return True

    return False


def _normalize_text(text, extraction_case):
    # replace punctuation signs with spaces
    new_text = []
    for i in text:
        new_text.append(i if i not in PUNCTUATION_SYMBOLS else " ")

    text = "".join(new_text)

    # extraction case specific replacements
    if extraction_case == "countries":
        # replace words/phrases that may give incorrect matches
        for i in ["აშშ დოლარ", "\n", "კუბურ მეტრ"]:
            text = text.replace(i, " ")

    elif extraction_case == "populated_areas":
        for i in ["რუსთავი 2", "რუსთავი2", "შოთა რუსთაველ"]:
            text = text.replace(i, " ")

    return text


def _extract(extraction_case, text):
    assert extraction_case in ("countries", "populated_areas")

    text = _normalize_text(text, extraction_case)

    result = set()
    unique_words = set(text.split())

    extract_info_iterator = {
        "countries": COUNTRIES_EXTRACT_INFO,
        "populated_areas": POPULATED_AREAS_EXTRACT_INFO,
    }[extraction_case]

    for i in extract_info_iterator:
        if _is_a_match(i, unique_words, text):
            result.add(i["id"])

    result = sorted(result)

    return result


def extract_countries(text):
    """
    Get countries from georgian text as a list of ISO 3166-s 2 letter codes sorted in ascending order.
    example output:
        [ "GE", "FR", "ES", "TR" ]

    Extraction returns result for country, even if its nationality is mentioned.

    Few countries will not be matched because of some uncertainties about their names.
    """

    return _extract("countries", text)


def extract_populated_areas(text):
    """
    Get list of relatively large populated areas (cities, towns, villages, resorts e.t.c) from Georgian text.

    example output:
        [ "თბილისი", "ბათუმი", "ქუთაისი" ]

    """

    return _extract("populated_areas", text)
