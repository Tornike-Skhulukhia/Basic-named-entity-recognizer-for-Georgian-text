import re


INFO = {
    "ა": "a",
    "ბ": "b",
    "გ": "g",
    "დ": "d",
    "ე": "e",
    "ვ": "v",
    "ზ": "z",
    "თ": "t",
    "ი": "i",
    "კ": "k",
    "ლ": "l",
    "მ": "m",
    "ნ": "n",
    "ო": "o",
    "პ": "p",
    "ჟ": "zh",
    "რ": "r",
    "ს": "s",
    "ტ": "t",
    "უ": "u",
    "ფ": "p",
    "ქ": "k",
    "ღ": "gh",
    "ყ": "k",
    "შ": "sh",
    "ჩ": "ch",
    "ც": "ts",
    "ძ": "dz",
    "წ": "ts",
    "ჭ": "ch",
    "ხ": "kh",
    "ჯ": "j",
    "ჰ": "h",
}

FULL_WORD_EXCEPTIONS = {
    # what it is & what it should be because of exception
    "davit": "david",
    "alexandre": "alexander",
    # until finding pattern
    "stefanchuk": "stefancuk" 
}

# ex:  მარქსი -> marx, ალექსი -> alex 
EXCEPTION_LETTERS = {
    "ksi": "x",
    "ks": "x",
    "ai": "i",
}

# ex: Sergei --> Sergey
EXCEPTION_WORD_ENDING_REPLACEMENTS = {
    "ei": "ey",
    "eni": "en",
    "ki": "k",
} 

# TODO-> add ending fixers - like ბაიდენ-ი (remove last letter) 
# and replace two letter combos with one where makes sense - like b-ai-deni - b-i-den


def translate_to_en(text):
    """
    Do basic letter-by letter translation of name or name & surname
    combination from Georgian to English.

    example input --> output:

    "გიორგი" --> "Giorgi"
    "მარიამი" --> "Mariami"

    "ია ფარულავა" --> "Ia Parulava"
    "გია დვალი" --> "Gia Dvali"
    "ბადრი პატარკაციშვილი" --> "Badri Patarkatsishvili"

    There are some exceptions included, like

    "დავით" will return "David", not "Davit"

    For foreign name/surnames, just this function translation
    will sometimes not be very accurate, as rules for this kind of translation'
    are much harder/not direct to write in few lines of code.

    Example like this:
    "ბაიდენი" --> "Baideni"
    "პუტინი" --> "Putin"


    """
    result = [INFO.get(i, i).lower() for i in text]

    result = "".join(result)

    # handle exceptions
    # parts of words
    for resulted, but_must_be in EXCEPTION_LETTERS.items():
        result = result = result.replace(resulted, but_must_be)

    # full words
    for resulted, but_must_be in FULL_WORD_EXCEPTIONS.items():
        result = re.sub(fr"{resulted}\b", but_must_be, result)

    # word ends
    for resulted, but_must_be in EXCEPTION_WORD_ENDING_REPLACEMENTS.items():
        result = re.sub(fr"{resulted}\b", but_must_be, result)

    result = result.title()

    return result
