from ast import Assert

import pytest
from country.extract_en import get_countries
from country.get_meta import get_country_meta_info_with_iso2_code


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            """
            Georgia, along with Turkey, Britain, and Cyprus, has been included in Israel's list of countries from which returning citizens will have to go 
            through a week of self-isolation. Local media ynet.co.il spreads information about it.
            Something ABOUT Côte d'Ivoire goes here.
            """,
            ["GE", "TR", "GB", "CY", "IL", "CI"],
        ),
        (
            """
            It should be noted that as of today, all travelers returning from the following countries will have to
             go through complete isolation and submit a negative PCR test result: United Arab Emirates, Seychelles, 
             Ecuador, Ethiopia, Bolivia, Guatemala, Honduras, Zimbabwe, Zambia, Columbia, Namibia, Costa Rica.
            """,
            ["AE", "SC", "EC", "ET", "BO", "GT", "HN", "ZW", "ZM", "CO", "NA", "CR"],
        ),
        (
            """
            From next Friday, the following countries will be added to the list:
             United Kingdom, Cyprus, Turkey, Georgia, Uganda, Myanmar, Fiji, Panama, Cambodia, Kenya, and Libya.
            """,
            ["GB", "CY", "TR", "GE", "UG", "MM", "FJ", "PA", "KH", "KE", "LY"],
        ),
        (
            """
            US Senate votes to end normal trade ties with Russia 
            """,
            ["US", "RU"],
        ),
        (
            """
            France, Germany, Ukraine, Russia agree to ministerial-level meeting
            """,
            ["FR", "DE", "UA", "RU"],
        ),
        (
            """
            No countries
            """,
            [],
        ),
    ],
)
def test_get_countries(text, expected):
    expected = sorted(expected)
    result = get_countries(text)

    assert result == expected
