import pytest
from person.extract_en import get_persons_en


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            """
            Ruling Georgian Dream party chair Irakli Kobakhidze has announced Georgia will file for the EU membership tomorrow, following the suit of Ukraine.
            """,
            ["Irakli Kobakhidze"],
        ),
        (
            """
            Shaking hands in front of a grand Geneva villa, U.S. President Joe Biden and Russian President Vladimir Putin on Wednesday began their first
            summit since Biden took office, with deep disagreements likely and expectations of solving them low.
            ...
            “I’m not sure that any agreements will be reached,” said Putin’s foreign policy adviser, Yuri Ushakov.

            Kremlin spokesman Dmitry Peskov said two presidents would "need to determine how to proceed with the heads of the diplomatic missions", according Peskov to Russian news agencies.

            """,
            ["Joe Biden", "Vladimir Putin", "Yuri Ushakov", "Dmitry Peskov"],
        ),
        (
            "Local media ynet.co.il spreads information about it.",
            [],
        ),
        (
            """French President Emmanuel Macron held a new 90-minute phone call with Russian counterpart Vladimir Putin today""",
            ["Emmanuel Macron", "Vladimir Putin"],
        ),
    ],
)
def test_get_persons_en(text, expected):
    assert get_persons_en(text) == sorted(expected)
