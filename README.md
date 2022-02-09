# Basic named entity recognizer for Georgian text
Non ML-based approach to extract named entities from Georgian text using Python.
Currently supported extractions are for countries and persons.

# countries extraction example
```python
from nerge import get_countries

# GET ISO-3166 2 letter country codes from given text

c = get_countries(
    "საქართველოს პრეზიდენტი შალვა ნათელაშვილი შეერთებული შტატების "
    "პრეზიდენტს საპრეზიდენტო სასახლეში დღეს უმასპინძლებს. შეხვედრას ასევე დაესწრებიან რუსი, "
    "ჩინელი, ფრანგი და დიდი ბრიტანელი დიპლომატები. შეხვედრის შემდეგ გაიმართება ამხანაგური "
    "საფეხბურთო მატჩი ბრაზილია-გერმანია, რომელსაც კორონავირუსის გავრცელების პრევენციის "
    "მიზნით მაყურებელი არ დაესწრება."
)

print(c)
# result
['BR', 'CN', 'DE', 'FR', 'GB', 'GE', 'RU', 'US']

```

# persons extraction example
```python
from nerge import get_persons


p = get_persons(
    'შესაძლოა "მთავარი არხის" დირექტორის პოსტი,  ნიკა გვარამიამ დატოვოს.'
    'მის შემცვლელად კი "ნაციონალური მოძრაობის" ყოფილი თავდაცვის მინისტრი,'
    'დიმიტრი შაშკინი სახელდება. ინფორმაციას ამის შესახებ, "პრაიმტაიმი" ავრცელებს. '
)

print(p)
# result
['დიმიტრი შაშკინი', 'ნიკა გვარამია']

```


# helper functions to get meta information where possible
```python
from nerge import get_country_meta

iso_alpha_2_code = "US"
m = get_country_meta(iso_alpha_2_code)

print(m)
# result
{
    'english_short_name': 'United States of America (the)',
    'friendly_name': 'United States of America',
    'alpha_3_code': 'USA',
    'numeric_code': 840,
    'flag': '🇺🇸'
}
```
