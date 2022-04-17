import spacy

NLP = spacy.load("en_core_web_sm")


def get_persons(text):
    """
    Return sorted list of unique identified person name_surnames, sorted in ascending order,
    using spacy.

    To match, name_surname must have at least 1 space in it.
    """
    doc = NLP(text)

    persons = set()

    for ent in doc.ents:
        # without this check, if sentence has person surname only and then name & surname, we will get 
        # two items, one for person name and one for name_surname 
        # this simple check should be good enough in most cases
        # otherwise add deduplication logic
        if ent.label_ == "PERSON":
            if ent.text.count(" ") != 0 :
                persons.add(ent.text)

    return sorted(persons)  # list

