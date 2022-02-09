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
# ['BR', 'CN', 'DE', 'FR', 'GB', 'GE', 'RU', 'US']

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
# ['დიმიტრი შაშკინი', 'ნიკა გვარამია']

```


