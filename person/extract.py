import string

from . import NAMES, SURNAMES
from .util import normalize_surname


def _normalize_text(text):

    # replace punctuation signs with spaces
    for i in string.punctuation:
        text = text.replace(i, " ")

    return text


def extract_persons(text):
    """
    Get text and return list of person name & surnames strings that was
    identified sorted in ascending order.

    Only currently listed name & surname combinations will be matched and
    only in case when we have name first directly followed with surname.

    If name has more than 1 word in it and we find it, result
    will have only last part.
    """

    text = _normalize_text(text)

    splitted_words = text.split()

    result = set()

    for i in range(0, len(splitted_words) - 1):
        curr_word = splitted_words[i]
        next_word = splitted_words[i + 1]

        if curr_word in NAMES:
            # maybe next word is surname
            normalized_possible_surname = normalize_surname(next_word)

            if normalized_possible_surname in SURNAMES:
                result.add(f"{curr_word} {normalized_possible_surname}")

    result = list(sorted(result))

    return result
