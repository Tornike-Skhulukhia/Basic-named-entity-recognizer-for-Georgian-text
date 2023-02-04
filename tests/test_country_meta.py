from country.get_meta import (
    get_country_meta_info_with_iso2_code as get_country_meta,
)


def test_georgia():
    resp = get_country_meta("GE")

    for key, value in {
        "official_name": "Georgia",
        "name_en": "Georgia",
        "name_ge": "საქართველო",
        "alpha_2_code": "GE",
        "alpha_3_code": "GEO",
        "numeric_code": 268,
        "continent_en": "Europe",
        "continent_ge": "ევროპა",
        "dial_code": "+995",
        "flag": "🇬🇪",
    }.items():
        assert resp.get(key) == value


def test_russia():
    resp = get_country_meta("RU")

    for key, value in {
        "official_name": "Russian Federation (the)",
        "name_en": "Russia",
        "name_ge": "რუსეთი",
        "alpha_2_code": "RU",
        "alpha_3_code": "RUS",
        "numeric_code": 643,
        "continent_en": "Europe",
        "continent_ge": "ევროპა",
        "dial_code": "+7",
        "flag": "🇷🇺",
    }.items():
        assert resp.get(key) == value


def test_us():
    resp = get_country_meta("US")

    for key, value in {
        "official_name": "United States of America (the)",
        "name_en": "United States of America",
        "name_ge": "ამერიკის შეერთებული შტატები",
        "alpha_2_code": "US",
        "alpha_3_code": "USA",
        "numeric_code": 840,
        "continent_en": "North America",
        "continent_ge": "ჩრდილოეთ ამერიკა",
        "dial_code": "+1",
        "flag": "🇺🇸",
    }.items():
        assert resp.get(key) == value
