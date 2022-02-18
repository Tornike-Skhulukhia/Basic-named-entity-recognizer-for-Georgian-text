from country.get_meta import get_country_meta_info_with_iso2_code as get_country_meta


def test_georgia():
    resp = get_country_meta("GE")

    for key, value in {
        "official_name": "Georgia",
        "name_en": "Georgia",
        "name_ge": "საქართველოს",
        "alpha_3_code": "GEO",
        "numeric_code": 268,
        "flag": "🇬🇪",
    }.items():
        assert resp.get(key) == value


def test_russia():
    resp = get_country_meta("RU")

    for key, value in {
        "official_name": "Russian Federation (the)",
        "name_en": "Russia",
        "name_ge": "რუსეთი",
        "alpha_3_code": "RUS",
        "numeric_code": 643,
        "flag": "🇷🇺",
    }.items():
        assert resp.get(key) == value


def test_us():
    resp = get_country_meta("US")

    for key, value in {
        "official_name": "United States of America (the)",
        "name_en": "United States of America",
        "name_ge": "ამერიკის შეერთებული შტატები",
        "alpha_3_code": "USA",
        "numeric_code": 840,
        "flag": "🇺🇸",
    }.items():
        assert resp.get(key) == value
