"""
Logic we used to extract possible surnames from br.geostat.ge 
website which allows to download full information about registered people there.

Data is not clean, so we could only use possible new surnames that
were checked and not existed not in previously saved NAMES/SURAMES,
it was about 7K in this date - February 2020.
"""

import pandas as pd
import glob
import string

# NAMES = set()
SURNAMES = set()


# simple pd.read_csv did not work for some reason, so...
def read_data(filename):
    headers = []
    rows = []

    content = open(filename, "r", encoding="utf-16")

    for i in content:
        i = i.strip()

        if not headers:
            # first line
            headers = i.split("\t")
        else:
            row = dict(zip(headers, i.split("\t")))
            rows.append(row)

    df = pd.DataFrame(rows)

    return df


_is_geo_or_space_char = lambda j: j == " " or (ord("ა") <= ord(j) <= ord("ჰ"))


def refine_name_surname(text):
    # remove punctuation

    for i in string.punctuation:
        text = text.replace(i, " ")

    text = " ".join(text.split())
    return text


def is_valid(name_surname):
    if name_surname.count(" ") != 1:
        return False

    return all(_is_geo_or_space_char(i) for i in name_surname)


def _seems_surname(text):
    for i in [
        "შვილი",
        "ძე",
        "ვა",
        "ია",
        "იანი",
        "ანი",
        "ელი",
        "ერი",
        "ური",
    ]:
        # some false positives are good here, as before importing, we check that new surnames are not in alredy big list of names
        # so names like ილია will be removed from this list, but similar ending surnames will not
        if text.endswith(i):
            return True

    return False


for index, filename in enumerate(sorted(glob.glob("*.csv"))):
    print(index, filename, end="")

    # # df = pd.read_csv(i)
    # df = pd.read_csv(open(i, "r", encoding="utf-16"), sep="\t")

    df = read_data(filename)

    all_name_surnames = df[df["ორგანიზციულ-სამართლებრივი ფორმა"] == "იმ"][
        "სუბიექტის დასახელება"
    ].unique()

    all_name_surnames = [refine_name_surname(i) for i in all_name_surnames]

    valid_name_surnames = [i for i in all_name_surnames if is_valid(i)]
    possible_surnames = {j for i in valid_name_surnames for j in i.split()}

    seems_surnames = {i for i in possible_surnames if _seems_surname(i)}

    # NAMES.update({i.split()[0] for i in valid_name_surnames})
    SURNAMES.update(seems_surnames)

    print("+")
    # print(f"NAMES: {len(NAMES)}, SURNAMES: {len(SURNAMES)}")
    print(f"SURNAMES: {len(SURNAMES)}")

    print(list(SURNAMES)[:100])
    # breakpoint()

"""
SURNAMES that we imported:
    . had more than 4 characters length
    . were not in previously saved names or surnames(union)
"""
