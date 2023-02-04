from country.get_meta import (
    get_populated_area_meta,
)


def test_tbilisi():
    resp = get_populated_area_meta("თბილისი")

    for key, value in {
        "name_ge": "თბილისი",
        "name_en": "Tbilisi",
        "is_region_center": 1,
        "region_ge": "თბილისი",  # actually მუნიციპალიტეტი, but anyways
        "region_en": "Tbilisi",
        "population_in_thousands": 1201.8,
        "coordinates_lat_lon": [41.7151, 44.8271],
    }.items():
        assert resp.get(key) == value


def test_walka():
    resp = get_populated_area_meta("წალკა")

    for key, value in {
        "name_ge": "წალკა",
        "name_en": "Tsalka",
        "is_region_center": 0,
        "region_ge": "ქვემო ქართლი",
        "region_en": "Kvemo Kartli",
        "population_in_thousands": 3.2,
        "coordinates_lat_lon": [41.5980, 44.0947],
    }.items():
        assert resp.get(key) == value


def test_gori():
    resp = get_populated_area_meta("გორი")

    for key, value in {
        "name_ge": "გორი",
        "name_en": "Gori",
        "is_region_center": 1,
        "region_ge": "შიდა ქართლი",
        "region_en": "Shida Kartli",
        "population_in_thousands": 45.6,
        "coordinates_lat_lon": [41.9854, 44.1084],
    }.items():
        assert resp.get(key) == value
