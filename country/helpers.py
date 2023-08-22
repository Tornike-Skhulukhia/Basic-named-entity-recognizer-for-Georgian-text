# helper definitions
SINGULAR_PEOPLE_SUFFIXES = [
    "ელი",
    "ელია",
    "ელმა",
    "ელ",
    "ელს",
    "ელსა",
    "ელის",
    "ელისა",
    "ელით",
    "ელად",
    "ელადაა",
    "ელო",
]
PLURAL_PEOPLE_SUFFIXES = [
    "ელთა",
    "ელნი",
    "ელები",
    "ელებმა",
    "ელებს",
    "ელებსა",
    "ელების",
    "ელებისა",
    "ელებით",
    "ელებად",
    "ელებადაა",
    "ელებო",
]

FROM_THAT_PLACE_SUFFIXES_1 = [
    "ური",
    "ურია",
    "ურმა",
    "ურ",
    "ურსა",
    "ურს",
    "ურის",
    "ურით",
    "ურად",
    "ურო",
]

FROM_THAT_PLACE_SUFFIXES_2 = [
    "ული",
    "ულია",
    "ულმა",
    "ულ",
    "ულს",
    "ულსა",
    "ულის",
    "ულით",
    "ულად",
    "ულო",
]

OTHER_COMMMON_SUFFIXES = [
    "ში",
    "ზე",
]

PROXIMITY_SUFFIXES = [
    "მდე",
    "თან",
]

"""
some examples for quick reminder

    # თბილისი
    # ჭიათურა
    # წყალტუბო
    # საჩხერე
    # ჩხოროწყუ

"""


def _get_populated_area_word_in_all_different_common_forms(word):
    '''

    TODO: Add კუმშვა support if specific flag was provided - ex:
        . ფანჯარის must be ფანჯრის, so "ა" is unnecessary/wrong according to Georgian grammer 

    '''

    word_1 = word[:-1]
    last_char = word[-1]

    res = {word}

    word_1_suffixes = []
    full_word_suffixes = []

    # suffixes for word itself
    if last_char == "ი":
        word_1_suffixes.extend(
            [
                # singular word
                "მა",
                "ს",
                "სა",
                "ის",
                "ისთვის",
                "ისა",
                "ით",
                "ადაა",
                "ად",
                "ო",
            ]
        )

        word_1_suffixes += (
            SINGULAR_PEOPLE_SUFFIXES + PLURAL_PEOPLE_SUFFIXES + FROM_THAT_PLACE_SUFFIXES_1 + OTHER_COMMMON_SUFFIXES
        )

        for i in PROXIMITY_SUFFIXES:
            if i == "თან":
                word_1_suffixes.append(i)

            elif i == "მდე":
                word_1_suffixes.append("ა" + i)

    else:
        # suffixes for word itself
        full_word_suffixes.extend(
            [
                "მ",
                "ს",
                "სა",
                "დ",
                "და",
                "დაა",
                "ვ",
            ]
        )
        if last_char in "აე":
            word_1_suffixes.extend(
                [
                    "ის",
                    "ისთვის",
                    "ისა",
                    "ით",
                ]
            )
        elif last_char in "ოუ":
            full_word_suffixes.extend(
                [
                    "სთვის",
                    "სა",
                    "თი",
                ]
            )

        # suffixes for other cases
        if last_char in "აე":
            word_1_suffixes += SINGULAR_PEOPLE_SUFFIXES + PLURAL_PEOPLE_SUFFIXES + FROM_THAT_PLACE_SUFFIXES_2

        elif last_char in "ო":
            full_word_suffixes += SINGULAR_PEOPLE_SUFFIXES + PLURAL_PEOPLE_SUFFIXES + FROM_THAT_PLACE_SUFFIXES_2

        elif last_char == "უ":
            full_word_suffixes += SINGULAR_PEOPLE_SUFFIXES + PLURAL_PEOPLE_SUFFIXES
            word_1_suffixes += FROM_THAT_PLACE_SUFFIXES_2

        # other commons - easy
        full_word_suffixes += OTHER_COMMMON_SUFFIXES

        # location related
        for i in PROXIMITY_SUFFIXES:
            if i == "თან":
                word_1_suffixes.append("ს" + i)

            elif i == "მდე":
                word_1_suffixes.append(i)

    # add data at once at the end
    res.update([f"{word}{suffix}" for suffix in [*full_word_suffixes]])
    res.update([f"{word_1}{suffix}" for suffix in [*word_1_suffixes]])

    return res
