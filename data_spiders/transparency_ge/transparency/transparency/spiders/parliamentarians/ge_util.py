
def get_retrieved_name_surnames(file_path):
    import pandas as pd

    df = pd.read_json(file_path, lines=True)

    names = set()
    surnames = set()

    for name_surname in df.name_surname:
        # as we store empty name_surnames if it seems invalid
        if not name_surname: continue

        
        name, surname = name_surname.rsplit(" ", maxsplit=1)

        for n in name.split("-"):
            if not n.isdigit():
                names.add(n)
        
        for s in surname.split("-"):
            if not s.isdigit():
                surnames.add(s)

    print(f'\nunique {len(names)=}, unique {len(surnames)=}')

    return names, surnames


def get_name_surnames_not_in_person_init_listings(names :set, surnames :set):
    import sys

    sys.path.append('/home/tornike/Desktop/nerge/')

    from person import NAMES, SURNAMES

    new_names = names - NAMES
    new_surnames = surnames - SURNAMES
    
    print(f'\n{len(new_names)=}, {len(new_surnames)=}')

    return new_names, new_surnames


if __name__ == "__main__":
    filepath = "/home/tornike/Desktop/nerge/data_spiders/transparency_ge/transparency/transparency/data.jl"
    
    names, surnames = get_retrieved_name_surnames(filepath)
    
    new_names, new_surnames = get_name_surnames_not_in_person_init_listings(names, surnames)
    
