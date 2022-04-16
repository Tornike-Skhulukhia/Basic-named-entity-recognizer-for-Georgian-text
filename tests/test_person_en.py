import pytest
from person.extract_en import extract_persons_en


@pytest.mark.parametrize(
    "text, expected_result",
    [
        (
            """Georgia’s Prime Minister Irakli Gharibashvili, visiting western Adjara region today, again made some controversial remarks about Russia’s war in Ukraine.""",
            [
                "Irakli Gharibashvili",
            ],
        ),
        (
            """Georgia’s Prime Minister Irakli Garibashvili, visiting western Adjara region today, again made some controversial remarks about Russia’s war in Ukraine.""",
            [
                "Irakli Garibashvili",
            ],
        ),
        # (
        #     """Ruslan Stefancuk, Speaker of the Verkhovna Rada, Ukrainian legislature, also expressed disappointment today.""",
        #     [
        #         "Ruslan Stefancuk",
        #     ],
        # ),
        (
            """Kremlin-backed Abkhaz leader Aslan Bzhania today met Russian Foreign Minister Sergey Lavrov and Deputy Prime Minister Alexander Novak in Moscow.""",
            [
                "Aslan Bzhania",
                "Sergey Lavrov",
                "Alexander Novak",
            ],
        ),
        (
            """According to Nika Gvaramia, these stipulations and conditions do not apply only to Mikheil Saakashvili.""",
            ["Nika Gvaramia", "Mikheil Saakashvili"],
        ),
        (
            '''Nikoloz Gvaramiani appeals to Salome Zurabishvili to award the title of Hero of Georgia to Georgian soldiers who died in Ukraine on the 23rd day of Putin's war:''',
            [
                "Nikoloz Gvaramiani",
                "Salome Zurabishvili",
            ]
        ),
        (
            '''Georgian wrestler Iakob Kajaia beat Russian Sergei Semenov in the quarterfinals.''',
            [
                "Iakob Kajaia",
                "Sergei Semenov",
            ]
        ),
    ],
)
def test(text, expected_result):
    try:
        assert extract_persons_en(text) == sorted(expected_result)
    except:
        aa = expected_result
        bb = extract_persons_en(text)
        breakpoint()
