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

EXCEPTIONS = {
    # what it is & what it should be because of exception
    "davit": "david",
}


def translate_to_en(text):  # pragma: no cover  # not important functionality, maybe add tests if needed later
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
    for resulted, but_must_be in EXCEPTIONS.items():
        result = re.sub(fr"{resulted}\b", but_must_be, result)

    # maybe implement basic rules to solve "ბაიდენი" --> "Baideni" like issues

    result = result.title()

    return result
