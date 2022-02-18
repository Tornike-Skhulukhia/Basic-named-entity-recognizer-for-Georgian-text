from person.get_sex import get_sex


# unidentified
def test_1_1():
    assert get_sex("") == None


def test_1_1():
    assert get_sex("qwertyuiop") == None


def test_1_1():
    assert get_sex("პოიუყტრეწქ") == None


# F
def test_2_1():
    assert get_sex("მარიამი") == "F"


def test_2_2():
    assert get_sex("მაყვალა") == "F"


def test_2_3():
    assert get_sex("ნინელი") == "F"


# M
def test_3_1():
    assert get_sex("გიორგი") == "M"


def test_3_2():
    assert get_sex("ლუკა") == "M"


def test_3_3():
    assert get_sex("ნიკა") == "M"
