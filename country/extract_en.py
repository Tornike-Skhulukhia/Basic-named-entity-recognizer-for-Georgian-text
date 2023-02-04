from .get_meta import COUNTRIES_DATA


COUNTRY_NAMES_TO_ISO2_CODES = {}
for iso2_code, info in COUNTRIES_DATA.items():
    COUNTRY_NAMES_TO_ISO2_CODES[info["name_en"].lower()] = iso2_code


# add some overrides not mentioned yet
COUNTRY_NAMES_TO_ISO2_CODES.update(
    {
        # make sure to use lowercase here
        "britain": "GB",
        "united kingdom": "GB",
        "myanmar": "MM",
        "usa": "US",
        "u.s.": "US",
        "u.s": "US",
        "columbia": "CO",
    }
)

MATCH_ONLY_IF_UPPERCASED_IN_SOURCE_TEXT = {
    # make sure to use uppercase here
    "US": "US",
}


def get_countries_en(original_text):
    """
    Get countries from English text as a list of ISO 3166-s 2 letter codes sorted in ascending order.

    Extraction returns result for country, only if it is mentioned exactly
    as COUNTRIES_EXTRACT_INFO's iso_country_name, which is different from Georgian
    extraction function in this library, which also works if country is
    mentioned in a bit different form(ex: nationality) are mentioned.

    Few countries will not be matched because of some uncertainties about their names.

    Current implementation is not optimized for speed and can be too slow for large texts,
    currently it is just to work implementation - fast and simple.

    * spacy implementation with GPE label_-s does not seem to identify some countries,
    because of this we use current manual approach.
    """
    lowercased_text = original_text.lower()
    result = set()

    # main data
    for country_name, iso2_code in COUNTRY_NAMES_TO_ISO2_CODES.items():
        if country_name in lowercased_text:
            result.add(iso2_code)

    # exceptions like US
    for (
        country_name,
        iso2_code,
    ) in MATCH_ONLY_IF_UPPERCASED_IN_SOURCE_TEXT.items():
        if country_name in original_text:
            result.add(iso2_code)

    return sorted(result)  # list
