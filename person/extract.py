import string

from . import NAMES, SURNAMES
from .util import normalize_surname

CHARACTERS_THAT_CAN_BE_USED_TO_JOIN_MULTI_NAME_HAVING_NAME_SURNAMES = [
    "-",
    "—",
    "(",
    ")",  # ( ) ex: :ირაკლი (დაჩი) ბერაია
]


def _normalize_text(text):

    # benchmark/test performance later using this and new text creation and other approaches...

    for i in CHARACTERS_THAT_CAN_BE_USED_TO_JOIN_MULTI_NAME_HAVING_NAME_SURNAMES:
        # these symbols are concatinating possible one name-surnames ex: ლაშა-გიორგი გიორგაძე
        # so we should replace them with space
        text = text.replace(i, " ")

    # replace punctuation signs with spaces
    for i in string.punctuation:
        if i not in CHARACTERS_THAT_CAN_BE_USED_TO_JOIN_MULTI_NAME_HAVING_NAME_SURNAMES:
            # but all others should remain, but separated from words so that
            # we can still identify after space-splitting if word is name/surname or not
            text = text.replace(i, f" {i} ")

    # replace multiple spaces with just 1
    text = " ".join(text.split())

    return text


def word_seems_name(word):
    return word in NAMES


def word_seems_surname(word):
    return word in SURNAMES


def extract_persons(text):
    """
    Get text and return list of person name & surnames strings that was
    identified sorted in ascending order.

    Only currently listed name & surname combinations will be matched and
    only in case when we have name first(we may have first and middle name) directly followed with surname.

    Before starting matching, text goes through basic normalization to leave
    only relevant letters for extraction, so if for example input text
    contains something like "first_name (middle_name) last_name",
    extracted result will be "first_name middle_name last_name".

    Edit: added support for 4 letter full name & surnames(ex: ურსულა ფონ დერ ლაიენი),
    in this case, we assume first 3 word from full name_surname are names, and last is surname
    which is possible to change form in a sentence.
    """

    text = _normalize_text(text)

    splitted_words = text.split()

    result = set()
    skip_indexes = set()

    for i in range(0, len(splitted_words) - 1):
        if i in skip_indexes:
            continue

        curr_word = splitted_words[i]
        next_word = splitted_words[i + 1]

        if i < len(splitted_words) - 3 and all(
            [
                word_seems_name(curr_word),
                word_seems_name(next_word),
                word_seems_name(splitted_words[i + 2]),
            ]
        ):

            normalized_possible_surname = normalize_surname(splitted_words[i + 3])

            if word_seems_surname(normalized_possible_surname):

                result.add(
                    f"{curr_word} {next_word} {splitted_words[i + 2]} {normalized_possible_surname}"
                )
                skip_indexes.update([i, i + 1, i + 2, i + 3])
                continue

        # 2 word-having name & 1 word-having surname test | ex: name = "სანდრა ელისაბედ", surname="რულოვსი"
        if (
            i < len(splitted_words) - 2
            and word_seems_name(curr_word)
            and word_seems_name(next_word)
        ):
            normalized_possible_surname = normalize_surname(splitted_words[i + 2])

            if word_seems_surname(normalized_possible_surname):
                result.add(f"{curr_word} {next_word} {normalized_possible_surname}")
                skip_indexes.update([i, i + 1, i + 2])
                continue

        # 1 word-having name & 1 word-having surname test | ex: "გიორგი გიორგობიანი"
        if word_seems_name(curr_word):
            # maybe next word is surname
            normalized_possible_surname = normalize_surname(next_word)

            if word_seems_surname(normalized_possible_surname):
                result.add(f"{curr_word} {normalized_possible_surname}")
                skip_indexes.update([i, i + 1])

    result = list(sorted(result))

    return result
