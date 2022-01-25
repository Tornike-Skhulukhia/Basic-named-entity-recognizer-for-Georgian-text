import pandas as pd

_df = pd.read_json("data_1.jl", lines=True)

_df = _df.rename(
    columns={
        "სრული სახელი": "person",
        "პირადი ნომერი": "person_id",
        # "შემოწირულობის ოდენობა": "quantity",
    }
)

df = _df[_df["person_id"].apply(lambda x: len(str(x)) == 11)]

df = df[df.person.apply(lambda x: len(x.split()) == 2)]

df["name"] = df.person.apply(lambda x: x.split(" ")[0].strip())
df["surname"] = df.person.apply(lambda x: x.split(" ")[1].strip())


_is_geo_or_space_char = lambda j: j == " " or (ord("ა") <= ord(j) <= ord("ჰ"))

names = {
    i
    for i in df.name.unique()
    if i.strip() and all([_is_geo_or_space_char(j) for j in i])
}
surnames = {
    i
    for i in df.surname.unique()
    if i.strip() and all([_is_geo_or_space_char(j) for j in i])
}

# remove too short names & surnames
names = {i for i in names if len(i) > 2}
surnames = {i for i in surnames if len(i) > 2}

print("Unique names: ", len(names))
print("Unique surnames: ", len(surnames))

# in some cases, first part is not name, and then surname, but reversed, so we should
# take a look until adding data or using it somewhere else
# OR check that newly identified names are not in already got saved bigger surnames list and reversed


# names - (NAMES.union(SURNAMES))
# surnames - (NAMES.union(SURNAMES))
