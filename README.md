# Basic named entity recognizer for Georgian text
Non ML-based approach to extract named entities from Georgian text using Python.
Currently supported extractions are for countries and persons.
For better idea how accurate these extractions are, please see files in tests directory and do your own testing.

# Person extraction examples

### get persons
```python
from nerge import get_persons

p = get_persons(
    'უკრაინის პრეზიდენტი ვლადიმირ ზელენსკი საქართველოს პრეზიდენტ სალომე ზურაბიშვილს'
    ' მხარდაჭერისთვის მადლობას ქართულ ენაზე უხდის.'
)

print(p)
# result
['ვლადიმირ ზელენსკი', 'სალომე ზურაბიშვილი']
```

### get sex from name
```python
from nerge import get_sex

name = "გიორგი"
s = get_sex(name)

print(s)
# result
"M"
```

### Basic(just letter-based) name/surname translation to English
```python
from nerge import translate_to_en

t = translate_to_en('კობა გვენეტაძე')

print(t)
# result
'Koba Gvenetadze'
```


# Country extraction examples

### get countries
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


### get meta information about country
```python
from nerge import get_country_meta

iso_alpha_2_code = "US"
m = get_country_meta(iso_alpha_2_code)

print(m)
# result
{
    "official_name": "United States of America (the)",
    "name_en": "United States of America",
    "name_ge": "ამერიკის შეერთებული შტატები",
    "alpha_3_code": "USA",
    "numeric_code": 840,
    "flag": "🇺🇸",
}
```
