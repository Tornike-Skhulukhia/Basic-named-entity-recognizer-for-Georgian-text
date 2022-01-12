import string

from . import COUNTRIES_EXTRACT_INFO


def _country_is_a_match(i, unique_words, text):
    # is full word there?
    for full_word in i.get("possible_full_words", []):
        if full_word in unique_words:
            return True

    # is any word that starts with ... there?
    for index, j in enumerate(i.get("word_should_start", [])):
        if i["_word_should_start_spaces_nums"] == 0:
            # if it is one word start
            for k in unique_words:
                if k.startswith(j):
                    return True
        else:
            # for more than 1 word starts (like "შეერთებულ შტატებ") we have to go through full text
            if j in text:
                return True

    return False


def _normalize_text(text):

    # replace punctuation signs with spaces
    for i in string.punctuation:
        text = text.replace(i, " ")

    # replace words/phrases that may give incorrect matches
    for i in ["აშშ დოლარ", "\n"]:
        text = text.replace(i, " ")

    return text


def extract_countries(text):
    """
    Get countries from georgian text as a list of ISO 3166-s 2 letter codes sorted in ascending order.

    Extraction returns result for country, even if its nationality is mentioned.

    Few countries will not be matched because of some uncertainties about their names.
    """

    text = _normalize_text(text)

    result = set()
    unique_words = set(text.split())

    # get countries
    for i in COUNTRIES_EXTRACT_INFO:
        if _country_is_a_match(i, unique_words, text):
            result.add(i["country_code"])

    result = sorted(result)

    return result
