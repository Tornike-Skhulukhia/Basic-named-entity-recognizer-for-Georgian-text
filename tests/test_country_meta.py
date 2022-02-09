from country.get_meta import get_country_meta_info_with_iso2_code as get_country_meta


def test_georgia():
    resp = get_country_meta("GE")

    for key, value in {
        "english_short_name": "Georgia",
        "friendly_name": "Georgia",
        "alpha_3_code": "GEO",
        "numeric_code": 268,
        "flag": "🇬🇪",
    }.items():
        assert resp.get(key) == value


def test_russia():
    resp = get_country_meta("RU")

    for key, value in {
        "english_short_name": "Russian Federation (the)",
        "friendly_name": "Russia",
        "alpha_3_code": "RUS",
        "numeric_code": 643,
        "flag": "🇷🇺",
    }.items():
        assert resp.get(key) == value


def test_us():
    resp = get_country_meta("US")

    for key, value in {
        "english_short_name": "United States of America (the)",
        "friendly_name": "United States of America",
        "alpha_3_code": "USA",
        "numeric_code": 840,
        "flag": "🇺🇸",
    }.items():
        assert resp.get(key) == value
