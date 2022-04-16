import json
import glob
import sys

sys.path.append('/home/tornike/Desktop/nerge/')
from person import NAMES, SURNAMES


jsons_folder = '/home/tornike/Downloads/BioguideProfiles/'

# name_surnames = []
names = set()
surnames = set()


for index, i in enumerate(glob.glob(f'{jsons_folder}*.json')):
    info = json.load(open(i))

    # full_name = f'{info.get("unaccentedGivenName", "")} {info.get("unaccentedMiddleName", "")} {info.get("unaccentedFamilyName", "")}'

    if i := info.get("unaccentedGivenName"):
        names.add(i.lower())

    if i := info.get("unaccentedMiddleName"):
        names.add(i.lower())

    if i := info.get("unaccentedFamilyName"):
        surnames.add(i.lower())

    # full_name = full_name.replace(".", " ").replace("-", " ").replace(")", " ").replace("(", " ")

    # full_name = " ".join(full_name.split())

    # name_surnames.append(full_name)

    print(index, "+")


# print(len(name_surnames))
# name_surnames = set(name_surnames)
# print(len(name_surnames))

print(f'{len(names)=}, {len(surnames)=}')
