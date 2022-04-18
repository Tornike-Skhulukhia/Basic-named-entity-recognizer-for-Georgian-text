import re
import string

import spacy

from .stop_words_en import INCORRECT_PERSON_LIKE_WORDS_FOR_SPACY

NLP = spacy.load(
    "en_core_web_sm",
    disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"],
)


def _preprocess_text(text):
    # remove incorrectly label-causing words
    text = re.sub(
        fr'\b({"|".join(INCORRECT_PERSON_LIKE_WORDS_FOR_SPACY)})\b',
        " ",
        text,
        flags=re.IGNORECASE,
    )

    # remove all digits (not useful & causes incorrect spacy matches, ex: Rustavi 2)
    text = re.sub(r"[0-9]", " ", text)

    # this way, cpacy identifies more names
    for old_char in string.punctuation:
        if old_char == ".":
            new_char = " . "
        else:
            new_char = " , "

        text = text.replace(old_char, new_char)

    text = " ".join(text.split()).strip()

    return text


def _text_seems_person(text):
    text = text.strip()

    if not text:
        return False

    # min words num check
    spaces_num = text.count(" ")

    if spaces_num == 0:
        return False

    # max words num check
    if spaces_num > 3:
        return False

    return True


def get_persons_en(text):
    """
    Return sorted list of unique identified person name_surnames, sorted in ascending order,
    using spacy.

    To match, name_surname must have at least 1 space in it.

    It seems to heavily depend on just capitalization of words, so
    there may be lots of false positives.
    """
    text = _preprocess_text(text)

    doc = NLP(text)

    persons = set()

    for ent in doc.ents:
        # without this check, if sentence has person surname only and then name & surname, we will get
        # two items, one for person name and one for name_surname
        # this simple check should be good enough in most cases
        # otherwise add deduplication logic
        if ent.label_ == "PERSON":
            persons.add(ent.text)

    # remove incorrect matches - they are a lot
    persons = {i for i in persons if _text_seems_person(i)}

    # capitalize each word first letter only
    persons = {i.title() for i in persons}

    return sorted(persons)  # list
