from person.translate_to_en import translate_to_en


# M
def test_1():
    assert translate_to_en("თორნიკე") == "Tornike"


def test_2():
    assert translate_to_en("გიორგი") == "Giorgi"


def test_3():
    assert translate_to_en("დავით") == "David"


def test_4():
    assert translate_to_en("ჯიმშერ") == "Jimsher"


# F
def test_5():
    assert translate_to_en("მარიამ") == "Mariam"


def test_6():
    assert translate_to_en("ნინო") == "Nino"


def test_7():
    assert translate_to_en("თეკლე") == "Tekle"


def test_8():
    assert translate_to_en("ანასტასია") == "Anastasia"


# surnames
def test_9():
    assert translate_to_en("ბურდული") == "Burduli"


def test_10():
    assert translate_to_en("კაპანაძე") == "Kapanadze"


def test_11():
    assert translate_to_en("რუსთაველი") == "Rustaveli"


def test_12():
    assert translate_to_en("გელაშვილი") == "Gelashvili"


def test_13():
    assert translate_to_en("უგულავა") == "Ugulava"


# name & surname
def test_14():
    assert translate_to_en("ია ფარულავა") == "Ia Parulava"


def test_15():
    assert translate_to_en("გია დვალი") == "Gia Dvali"


def test_16():
    assert translate_to_en("ბადრი პატარკაციშვილი") == "Badri Patarkatsishvili"


def test_17():
    assert translate_to_en("თეა წულუკიანი") == "Tea Tsulukiani"


def test_18():
    assert translate_to_en("ნანუკა ჟორჟოლიანი") == "Nanuka Zhorzholiani"


def test_19():
    assert translate_to_en("ნინო ქათამაძე") == "Nino Katamadze"
