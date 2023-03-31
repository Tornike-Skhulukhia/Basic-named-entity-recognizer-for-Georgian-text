# TODO: think about implementing trie which will make extraction of specific word-starting cases much easier

from .helpers import _get_populated_area_word_in_all_different_common_forms

"""


word_should_start:
    add info here if we can definitely say that word is a match if it starts by given text.
    ex: if word starts with "ქართულ", we can be sure that it is about Georgia. 

possible_full_words:
    add info here if we can not add info into word_should_start,
    for example if a word starts with "ჩადი", we can not say definitely
    if it is a country, as there are other similar Georgian words.

    This option is faster to lookup, but we have to list all possible ways the
    word may be written, so there is a chance that we may miss some forms,
    and also we have to make much more typing here.

"""

COUNTRIES_EXTRACT_INFO = [
    {
        "iso_country_name": "Afghanistan",
        "id": "AF",
        "word_should_start": ["ავღან"],
    },
    {
        "iso_country_name": "Albania",
        "id": "AL",
        "word_should_start": ["ალბან"],
    },
    {
        "iso_country_name": "Algeria",
        "id": "DZ",
        "word_should_start": ["ალჟირ"],
    },
    {
        "iso_country_name": "American Samoa",
        "id": "AS",
        "word_should_start": ["სამოა"],
    },
    {
        "iso_country_name": "Andorra",
        "id": "AD",
        "word_should_start": ["ანდორ"],
    },
    {
        "iso_country_name": "Angola",
        "id": "AO",
        "word_should_start": ["ანგოლ"],
    },
    {
        "iso_country_name": "Anguilla",
        "id": "AI",
        "word_should_start": ["ანგილ", "ანგვილ"],
    },
    {
        "iso_country_name": "Antarctica",
        "id": "AQ",
        "word_should_start": ["ანტარქტიკ"],
    },
    {
        "iso_country_name": "Antigua and Barbuda",
        "id": "AG",
        "word_should_start": ["ანტიგუა და ბარბუდ"],
    },
    {
        "iso_country_name": "Argentina",
        "id": "AR",
        "word_should_start": ["არგენტინ"],
    },
    {
        "iso_country_name": "Armenia",
        "id": "AM",
        "word_should_start": ["სომხეთ", "სომხურ", "სომეხ"],
    },
    {
        "iso_country_name": "Aruba",
        "id": "AW",
        "word_should_start": ["არუბ"],
    },
    {
        "iso_country_name": "Australia",
        "id": "AU",
        "word_should_start": ["ავსტრალ"],
    },
    {
        "iso_country_name": "Austria",
        "id": "AT",
        "word_should_start": ["ავსტრი"],
    },
    {
        "iso_country_name": "Azerbaijan",
        "id": "AZ",
        "word_should_start": ["აზერბაიჯან"],
    },
    {
        "iso_country_name": "Bahamas (the)",
        "id": "BS",
        "word_should_start": ["ბაჰამ"],
    },
    {
        "iso_country_name": "Bahrain",
        "id": "BH",
        "word_should_start": ["ბაჰრეინ"],
    },
    {
        "iso_country_name": "Bangladesh",
        "id": "BD",
        "word_should_start": ["ბანგლადეშ"],
    },
    {
        "iso_country_name": "Barbados",
        "id": "BB",
        "word_should_start": ["ბარბადოს"],
    },
    {
        "iso_country_name": "Belarus",
        "id": "BY",
        "word_should_start": ["ბელარუს"],
    },
    {
        "iso_country_name": "Belgium",
        "id": "BE",
        "word_should_start": ["ბელგი"],
    },
    {
        "iso_country_name": "Belize",
        "id": "BZ",
        "word_should_start": ["ბელიზ"],
    },
    {
        "iso_country_name": "Benin",
        "id": "BJ",
        "word_should_start": ["ბენინ"],
    },
    {
        "iso_country_name": "Bermuda",
        "id": "BM",
        "word_should_start": ["ბერმუდ"],
    },
    {
        "iso_country_name": "Bhutan",
        "id": "BT",
        "word_should_start": ["ბუტან"],
    },
    {
        "iso_country_name": "Bolivia (Plurinational State of)",
        "id": "BO",
        "word_should_start": ["ბოლივი"],
    },
    # {
    #     "iso_country_name": "Bonaire, Sint Eustatius and Saba",
    #     "id": "BQ",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Bosnia and Herzegovina",
        "id": "BA",
        "word_should_start": ["ბოსნი"],
    },
    {
        "iso_country_name": "Botswana",
        "id": "BW",
        "word_should_start": ["ბოცვან"],
    },
    # {
    #     "iso_country_name": "Bouvet Island",
    #     "id": "BV",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Brazil",
        "id": "BR",
        "word_should_start": ["ბრაზილ"],
    },
    # {
    #     "iso_country_name": "British Indian Ocean Territory (the)",
    #     "id": "IO",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Brunei Darussalam",
        "id": "BN",
        "word_should_start": ["ბრუნე"],
    },
    {
        "iso_country_name": "Bulgaria",
        "id": "BG",
        "word_should_start": ["ბულგარ"],
    },
    {
        "iso_country_name": "Burkina Faso",
        "id": "BF",
        "word_should_start": ["ბურკინა ფასო"],
    },
    {
        "iso_country_name": "Burundi",
        "id": "BI",
        "word_should_start": ["ბურუნდ"],
    },
    {
        "iso_country_name": "Cabo Verde",
        "id": "CV",
        "word_should_start": ["კაბო ვერდ"],
    },
    {
        "iso_country_name": "Cambodia",
        "id": "KH",
        "word_should_start": ["კამბოჯ"],
    },
    {
        "iso_country_name": "Cameroon",
        "id": "CM",
        "word_should_start": ["კამერუნ"],
    },
    {
        "iso_country_name": "Canada",
        "id": "CA",
        "word_should_start": ["კანად"],
    },
    {
        "iso_country_name": "Cayman Islands (the)",
        "id": "KY",
        "word_should_start": ["კაიმან"],
    },
    {
        "iso_country_name": "Central African Republic (the)",
        "id": "CF",
        "word_should_start": ["აფრიკის რესპუბლიკ"],
    },
    {
        "iso_country_name": "Ghana",
        "id": "TD",
        "word_should_start": [],
        "possible_full_words": [
            "ჩადიში",
            "ჩადში",
            "ჩადმა",
            "ჩადს",
            "ჩადური",
            "ჩადურმა",
            "ჩადურ",
            "ჩადელი",
            "ჩადელ",
            "ჩადელმა",
        ],
    },
    {
        "iso_country_name": "Chile",
        "id": "CL",
        "word_should_start": ["ჩილე"],
    },
    {
        "iso_country_name": "China",
        "id": "CN",
        "word_should_start": ["ჩინეთ", "ჩინურ", "ჩინელ"],
    },
    # {
    #     "iso_country_name": "Christmas Island",
    #     "id": "CX",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Cocos (Keeling) Islands (the)",
    #     "id": "CC",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Colombia",
        "id": "CO",
        "word_should_start": ["კოლუმბია", "კოლუმბიუ", "კოლუმბიე"],
    },
    {
        "iso_country_name": "Comoros (the)",
        "id": "KM",
        "word_should_start": ["კომორის კუნძულ"],
    },
    {
        "iso_country_name": "Congo (the Democratic Republic of the)",
        "word_should_start": ["კონგოს დემოკრატიულ"],
        "id": "CD",
    },
    {
        "iso_country_name": "Congo (the)",
        "id": "CG",
        "word_should_start": ["კონგო"],
    },
    {
        "iso_country_name": "Cook Islands (the)",
        "id": "CK",
        "word_should_start": ["კუკის კუნძულ"],
    },
    {
        "iso_country_name": "Costa Rica",
        "id": "CR",
        "word_should_start": ["კოსტა რიკ"],
    },
    {
        "iso_country_name": "Croatia",
        "id": "HR",
        "word_should_start": ["ხორვატ"],
    },
    {
        "iso_country_name": "Cuba",
        "id": "CU",
        "word_should_start": ["კუბა", "კუბურ", "კუბელ"],
    },
    {
        "iso_country_name": "Curaçao",
        "id": "CW",
        "word_should_start": ["კურასაო", "კურაჩაო"],
    },
    {
        "iso_country_name": "Cyprus",
        "id": "CY",
        "word_should_start": ["კვიპროს"],
    },
    {
        "iso_country_name": "Czechia",
        "id": "CZ",
        "word_should_start": ["ჩეხეთ", "ჩეხურ", "ჩეხელ"],
    },
    {
        "iso_country_name": "Côte d'Ivoire",
        "id": "CI",
        "word_should_start": ["კოტ დივუარ"],
    },
    {
        "iso_country_name": "Denmark",
        "id": "DK",
        "word_should_start": ["დანია", "დანიურ", "დანიელ"],
    },
    {
        "iso_country_name": "Djibouti",
        "id": "DJ",
        "word_should_start": ["ჯიბუტ"],
    },
    {
        "iso_country_name": "Dominica",
        "id": "DM",
        "word_should_start": ["დომინიკ"],
    },
    {
        "iso_country_name": "Dominican Republic (the)",
        "id": "DO",
        "word_should_start": ["დიმინიკის რესპუბლიკ"],
    },
    {
        "iso_country_name": "Ecuador",
        "id": "EC",
        "word_should_start": ["ეკვადორ"],
    },
    {
        "iso_country_name": "Egypt",
        "id": "EG",
        "word_should_start": ["ეგვიპტ"],
    },
    {
        "iso_country_name": "El Salvador",
        "id": "SV",
        "word_should_start": ["ელ სალვადორ"],
    },
    {
        "iso_country_name": "Equatorial Guinea",
        "id": "GQ",
        "word_should_start": ["ეკვატორული გვინ", "ეკვატორულ გვინ"],
    },
    {
        "iso_country_name": "Eritrea",
        "id": "ER",
        "word_should_start": ["ერიტრ"],
    },
    {
        "iso_country_name": "Estonia",
        "id": "EE",
        "word_should_start": ["ესტონეთ"],
    },
    {
        "iso_country_name": "Eswatini",
        "id": "SZ",
        "word_should_start": ["ესვატინ", "სვაზილენდ"],
    },
    {
        "iso_country_name": "Ethiopia",
        "id": "ET",
        "word_should_start": ["ეთიოპ"],
    },
    {
        "iso_country_name": "Falkland Islands (the) [Malvinas]",
        "id": "FK",
        "word_should_start": ["ფოლკლენდის კუნძულ", "მალვინის კუნძულ"],
    },
    {
        "iso_country_name": "Faroe Islands (the)",
        "id": "FO",
        "word_should_start": ["ფარერის კუნძულ"],
    },
    {
        "iso_country_name": "Fiji",
        "id": "FJ",
        "word_should_start": ["ფიჯი"],
    },
    {
        "iso_country_name": "Finland",
        "id": "FI",
        "word_should_start": ["ფინეთ", "ფინურ", "ფინელ"],
    },
    {
        "iso_country_name": "France",
        "id": "FR",
        "word_should_start": ["საფრანგეთ", "ფრანგ"],
    },
    # {
    #     "iso_country_name": "French Guiana",
    #     "id": "GF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "French Polynesia",
        "id": "PF",
        "word_should_start": ["პოლინეზი"],
    },
    # {
    #     "iso_country_name": "French Southern Territories (the)",
    #     "id": "TF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Gabon",
        "id": "GA",
        "word_should_start": ["გაბონ"],
    },
    {
        "iso_country_name": "Gambia (the)",
        "id": "GM",
        "word_should_start": ["გამბი"],
    },
    {
        "iso_country_name": "Georgia",
        "id": "GE",
        "word_should_start": ["საქართველო", "ქართულ", "ქართველ"],
    },
    {
        "iso_country_name": "Germany",
        "id": "DE",
        "word_should_start": ["გერმან"],
    },
    {
        "iso_country_name": "Ghana",
        "id": "GH",
        "word_should_start": [],
        "possible_full_words": [
            "განამ",
            "განას",
            "განაში",
            "განური",
            "განურმა",
            "განურ",
            "განელი",
            "განელ",
            "განელმა",
        ],
    },
    {
        "iso_country_name": "Gibraltar",
        "id": "GI",
        "word_should_start": ["გიბრალტარ"],
    },
    {
        "iso_country_name": "Greece",
        "id": "GR",
        "word_should_start": ["საბერძნეთ", "ბერძნ"],
    },
    {
        "iso_country_name": "Greenland",
        "id": "GL",
        "word_should_start": ["გრელანდ"],
    },
    {
        "iso_country_name": "Grenada",
        "id": "GD",
        "word_should_start": ["გრენად"],
    },
    {
        "iso_country_name": "Guadeloupe",
        "id": "GP",
        "word_should_start": ["გუადალუპ", "გვადალუპ"],
    },
    {
        "iso_country_name": "Guam",
        "id": "GU",
        "word_should_start": ["გუამ"],
    },
    {
        "iso_country_name": "Guatemala",
        "id": "GT",
        "word_should_start": ["გვატემალ"],
    },
    {
        "iso_country_name": "Guernsey",
        "id": "GG",
        "word_should_start": ["გერნს"],
    },
    {
        "iso_country_name": "Guinea",
        "id": "GN",
        "word_should_start": ["გვინე"],
    },
    {
        "iso_country_name": "Guinea-Bissau",
        "id": "GW",
        "word_should_start": ["გვინეა ბისაუ"],
    },
    {
        "iso_country_name": "Guyana",
        "id": "GY",
        "word_should_start": ["გაიან"],
    },
    {
        "iso_country_name": "Haiti",
        "id": "HT",
        "word_should_start": ["ჰაიტ"],
    },
    # {
    #     "iso_country_name": "Heard Island and McDonald Islands",
    #     "id": "HM",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Holy See (the)",
    #     "id": "VA",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Honduras",
        "id": "HN",
        "word_should_start": ["ჰონდურას"],
    },
    {
        "iso_country_name": "Hong Kong",
        "id": "HK",
        "word_should_start": ["ჰონგ კონგ", "ჰონგკონგ"],
    },
    {
        "iso_country_name": "Hungary",
        "id": "HU",
        "word_should_start": ["უნგრეთ", "უნგრულ", "უნგრელ"],
    },
    {
        "iso_country_name": "Iceland",
        "id": "IS",
        "word_should_start": ["ისლანდ"],
    },
    {
        "iso_country_name": "India",
        "id": "IN",
        "word_should_start": ["ინდოეთ", "ინდურ", "ინდოელ"],
    },
    {
        "iso_country_name": "Indonesia",
        "id": "ID",
        "word_should_start": ["ინდონეზი"],
    },
    {
        "iso_country_name": "Iran (Islamic Republic of)",
        "id": "IR",
        "word_should_start": ["ირან"],
    },
    {
        "iso_country_name": "Iraq",
        "id": "IQ",
        "word_should_start": ["ერაყ"],
    },
    {
        "iso_country_name": "Ireland",
        "id": "IE",
        "word_should_start": ["ირლანდ"],
    },
    # {
    #     "iso_country_name": "Isle of Man",
    #     "id": "IM",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Israel",
        "id": "IL",
        "word_should_start": ["ისრაელ", "ისრაულ"],
    },
    {
        "iso_country_name": "Italy",
        "id": "IT",
        "word_should_start": ["იტალ"],
    },
    {
        "iso_country_name": "Jamaica",
        "id": "JM",
        "word_should_start": ["იამაიკ"],
    },
    {
        "iso_country_name": "Japan",
        "id": "JP",
        "word_should_start": ["იაპონ"],
    },
    # {
    #     "iso_country_name": "Jersey",
    #     "id": "JE",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Jordan",
        "id": "JO",
        "word_should_start": ["იორდან"],
    },
    {
        "iso_country_name": "Kazakhstan",
        "id": "KZ",
        "word_should_start": ["ყაზახ"],
    },
    {
        "iso_country_name": "Kenya",
        "id": "KE",
        "word_should_start": ["კენია", "კენიურ", "კენიელ"],
    },
    {
        "iso_country_name": "Kiribati",
        "id": "KI",
        "word_should_start": ["კირიბატ"],
    },
    {
        "iso_country_name": "Korea (the Democratic People's Republic of)",
        "word_should_start": ["ჩრდილოეთ კორე", "ჩრდილო კორე"],
        "id": "KP",
    },
    {
        "iso_country_name": "Korea (the Republic of)",
        "id": "KR",
        "word_should_start": ["სამხრეთ კორე"],
    },
    {
        "iso_country_name": "Kuwait",
        "id": "KW",
        "word_should_start": ["ქუვეით"],
    },
    {
        "iso_country_name": "Kyrgyzstan",
        "id": "KG",
        "word_should_start": ["ყირგიზეთ"],
    },
    {
        "iso_country_name": "Lao People's Democratic Republic (the)",
        "word_should_start": ["ლაოს"],
        "id": "LA",
    },
    {
        "iso_country_name": "Latvia",
        "id": "LV",
        "word_should_start": ["ლატვი"],
    },
    {
        "iso_country_name": "Lebanon",
        "id": "LB",
        "word_should_start": ["ლიბან"],
    },
    # {
    #     "iso_country_name": "Lesotho",
    #     "id": "LS",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Liberia",
        "id": "LR",
        "word_should_start": ["ლიბერი"],
    },
    {
        "iso_country_name": "Libya",
        "id": "LY",
        "word_should_start": ["ლიბია", "ლიბიი", "ლიბიურ", "ლიბიელ"],
    },
    {
        "iso_country_name": "Liechtenstein",
        "id": "LI",
        "word_should_start": ["ლიხტენშტაინ"],
    },
    {
        "iso_country_name": "Lithuania",
        "id": "LT",
        "word_should_start": ["ლიტვ", "ლიეტუვ"],
    },
    {
        "iso_country_name": "Luxembourg",
        "id": "LU",
        "word_should_start": ["ლუქსემბურგ"],
    },
    {
        "iso_country_name": "Macao",
        "id": "MO",
        "word_should_start": ["მაკაო"],
    },
    {
        "iso_country_name": "Madagascar",
        "id": "MG",
        "word_should_start": ["მადაგასკარ"],
    },
    {
        "iso_country_name": "Malawi",
        "id": "MW",
        "word_should_start": [
            "მალავი",
            "მალავში",
            "მალავმა",
            "მალავურ",
            "მალაველ",
        ],
    },
    {
        "iso_country_name": "Malaysia",
        "id": "MY",
        "word_should_start": ["მალაიზ"],
    },
    {
        "iso_country_name": "Maldives",
        "id": "MV",
        "word_should_start": ["მალდივ"],
    },
    {
        "iso_country_name": "Mali",
        "id": "ML",
        "word_should_start": ["მალიში", "მალურ", "მალიურ", "მალელ"],
        "possible_full_words": ["მალი", "მალიმ", "მალის"],
    },
    {
        "iso_country_name": "Malta",
        "id": "MT",
        "word_should_start": ["მალტ"],
    },
    {
        "iso_country_name": "Marshall Islands (the)",
        "id": "MH",
        "word_should_start": ["მარშალის კუნძულ"],
    },
    {
        "iso_country_name": "Martinique",
        "id": "MQ",
        "word_should_start": ["მარტინიკ"],
    },
    {
        "iso_country_name": "Mauritania",
        "id": "MR",
        "word_should_start": ["მავრიტან"],
    },
    {
        "iso_country_name": "Mauritius",
        "id": "MU",
        "word_should_start": ["მავრიკ"],
    },
    # {
    #     "iso_country_name": "Mayotte",
    #     "id": "YT",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Mexico",
        "id": "MX",
        "word_should_start": ["მექსიკ"],
    },
    {
        "iso_country_name": "Micronesia (Federated States of)",
        "id": "FM",
        "word_should_start": ["მიკრონეზ"],
    },
    {
        "iso_country_name": "Moldova (the Republic of)",
        "id": "MD",
        "word_should_start": ["მოლდოვ"],
    },
    {
        "iso_country_name": "Monaco",
        "id": "MC",
        "word_should_start": ["მონაკო"],
    },
    {
        "iso_country_name": "Mongolia",
        "id": "MN",
        "word_should_start": ["მონღოლეთ", "მონღოლურ", "მონღოლელ"],
    },
    {
        "iso_country_name": "Montenegro",
        "id": "ME",
        "word_should_start": ["მონტენეგრ"],
    },
    # {
    #     "iso_country_name": "Montserrat",
    #     "id": "MS",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Morocco",
        "id": "MA",
        "word_should_start": ["მაროკ"],
    },
    {
        "iso_country_name": "Mozambique",
        "id": "MZ",
        "word_should_start": ["მოზამბიკ"],
    },
    {
        "iso_country_name": "Myanmar",
        "id": "MM",
        "word_should_start": ["მიანმარ"],
    },
    {
        "iso_country_name": "Namibia",
        "id": "NA",
        "word_should_start": ["ნამიბ"],
    },
    {
        "iso_country_name": "Nauru",
        "id": "NR",
        "word_should_start": ["ნაურ"],
    },
    {
        "iso_country_name": "Nepal",
        "id": "NP",
        "word_should_start": ["ნეპალ"],
    },
    {
        "iso_country_name": "Netherlands (the)",
        "id": "NL",
        "word_should_start": ["ჰოლანდ", "ნიდერლანდ"],
    },
    {
        "iso_country_name": "New Caledonia",
        "id": "NC",
        "word_should_start": ["კალედონი"],
    },
    {
        "iso_country_name": "New Zealand",
        "id": "NZ",
        "word_should_start": ["ზელანდ"],
    },
    {
        "iso_country_name": "Nicaragua",
        "id": "NI",
        "word_should_start": ["ნიკარაგ"],
    },
    {
        "iso_country_name": "Niger (the)",
        "id": "NE",
        "word_should_start": [],
        "possible_full_words": [
            "ნიგერი",
            "ნიგერმა",
            "ნიგერში",
            "ნიგერს",
            "ნიგერთან",
            "ნიგერულ",
            "ნიგერელ",
        ],
    },
    {
        "iso_country_name": "Nigeria",
        "id": "NG",
        "word_should_start": ["ნიგერია", "ნიგერიულ", "ნიგერიელ"],
    },
    # {
    #     "iso_country_name": "Niue",
    #     "id": "NU",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Norfolk Island",
    #     "id": "NF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "North Macedonia",
        "id": "MK",
        "word_should_start": ["მაკედონ"],
    },
    {
        "iso_country_name": "Northern Mariana Islands (the)",
        "id": "MP",
        "word_should_start": ["მარიანას კუნძულ"],
    },
    {
        "iso_country_name": "Norway",
        "id": "NO",
        "word_should_start": ["ნორვეგ"],
    },
    {
        "iso_country_name": "Oman",
        "id": "OM",
        "word_should_start": ["ომან"],
    },
    {
        "iso_country_name": "Pakistan",
        "id": "PK",
        "word_should_start": ["პაკისტან"],
    },
    {
        "iso_country_name": "Palau",
        "id": "PW",
        "word_should_start": ["პალაუ"],
    },
    {
        "iso_country_name": "Palestine, State of",
        "id": "PS",
        "word_should_start": ["პალესტინ"],
    },
    {
        "iso_country_name": "Panama",
        "id": "PA",
        "word_should_start": ["პანამ"],
    },
    {
        "iso_country_name": "Papua New Guinea",
        "id": "PG",
        "word_should_start": ["ახალი გვინე", "ახალ გვინე"],
    },
    {
        "iso_country_name": "Paraguay",
        "id": "PY",
        "word_should_start": ["პარაგვ"],
    },
    {
        "iso_country_name": "Peru",
        "id": "PE",
        "word_should_start": ["პერუ"],
    },
    {
        "iso_country_name": "Philippines (the)",
        "id": "PH",
        "word_should_start": ["ფილიპინე"],
    },
    # {
    #     "iso_country_name": "Pitcairn",
    #     "id": "PN",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Poland",
        "id": "PL",
        "word_should_start": ["პოლონ"],
    },
    {
        "iso_country_name": "Portugal",
        "id": "PT",
        "word_should_start": ["პორტუგალ"],
    },
    {
        "iso_country_name": "Puerto Rico",
        "id": "PR",
        "word_should_start": ["პუერტო რიკ"],
    },
    {
        "iso_country_name": "Qatar",
        "id": "QA",
        "word_should_start": ["ყატარ", "კატარ"],
    },
    {
        "iso_country_name": "Romania",
        "id": "RO",
        "word_should_start": ["რუმინეთ"],
    },
    {
        "iso_country_name": "Russian Federation (the)",
        "id": "RU",
        "word_should_start": ["რუსეთ", "რუსულ", "რუსის"],
        "possible_full_words": ["რუსი", "რუს", "რუსმა", "რუსს"],
    },
    {
        "iso_country_name": "Rwanda",
        "id": "RW",
        "word_should_start": ["რუანდ"],
    },
    # {
    #     "iso_country_name": "Réunion",
    #     "id": "RE",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Barthélemy",
    #     "id": "BL",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Helena, Ascension and Tristan da Cunha",
    #     "word_should_start": [],
    #     "id": "SH",
    # },
    # {
    #     "iso_country_name": "Saint Kitts and Nevis",
    #     "id": "KN",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Lucia",
    #     "id": "LC",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Martin (French part)",
    #     "id": "MF",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Pierre and Miquelon",
    #     "id": "PM",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Vincent and the Grenadines",
    #     "id": "VC",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Samoa",
        "id": "WS",
        "word_should_start": ["სამოა", "სამოუ", "სომოელ"],
    },
    {
        "iso_country_name": "San Marino",
        "id": "SM",
        "word_should_start": ["სან მარინ"],
    },
    # {
    #     "iso_country_name": "Sao Tome and Principe",
    #     "id": "ST",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Saudi Arabia",
        "id": "SA",
        "word_should_start": ["საუდის არაბე"],
    },
    {
        "iso_country_name": "Senegal",
        "id": "SN",
        "word_should_start": ["სენეგალ"],
    },
    {
        "iso_country_name": "Serbia",
        "id": "RS",
        "word_should_start": ["სერბ"],
    },
    {
        "iso_country_name": "Seychelles",
        "id": "SC",
        "word_should_start": ["სეიშელ"],
    },
    {
        "iso_country_name": "Sierra Leone",
        "id": "SL",
        "word_should_start": ["სიერა ლეონ"],
    },
    {
        "iso_country_name": "Singapore",
        "id": "SG",
        "word_should_start": ["სინგაპ"],
    },
    # {
    #     "iso_country_name": "Sint Maarten (Dutch part)",
    #     "id": "SX",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Slovakia",
        "id": "SK",
        "word_should_start": ["სლოვაკ"],
    },
    {
        "iso_country_name": "Slovenia",
        "id": "SI",
        "word_should_start": ["სლოვენ"],
    },
    {
        "iso_country_name": "Solomon Islands",
        "id": "SB",
        "word_should_start": ["სოლომონის კუნძულ"],
    },
    {
        "iso_country_name": "Somalia",
        "id": "SO",
        "word_should_start": ["სომალ"],
    },
    {
        "iso_country_name": "South Africa",
        "id": "ZA",
        "word_should_start": ["სამხრეთ აფრიკ"],
    },
    # {
    #     "iso_country_name": "South Georgia and the South Sandwich Islands",
    #     "word_should_start": [],
    #     "id": "GS",
    # },
    {
        "iso_country_name": "South Sudan",
        "id": "SS",
        "word_should_start": ["სამხრეთ სუდან"],
    },
    {
        "iso_country_name": "Spain",
        "id": "ES",
        "word_should_start": ["ესპანეთ", "ესპანურ", "ესპანელ"],
    },
    {
        "iso_country_name": "Sri Lanka",
        "id": "LK",
        "word_should_start": ["შრი ლანკ"],
    },
    {
        "iso_country_name": "Sudan (the)",
        "id": "SD",
        "word_should_start": ["სუდან"],
    },
    {
        "iso_country_name": "Suriname",
        "id": "SR",
        "word_should_start": ["სურინამ"],
    },
    # {
    #     "iso_country_name": "Svalbard and Jan Mayen",
    #     "id": "SJ",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Sweden",
        "id": "SE",
        "word_should_start": ["შვედ"],
    },
    {
        "iso_country_name": "Switzerland",
        "id": "CH",
        "word_should_start": ["შვეიცარ"],
    },
    {
        "iso_country_name": "Syrian Arab Republic (the)",
        "id": "SY",
        "word_should_start": ["სირია"],
    },
    {
        "iso_country_name": "Taiwan (Province of China)",
        "id": "TW",
        "word_should_start": ["ტაივან"],
    },
    {
        "iso_country_name": "Tajikistan",
        "id": "TJ",
        "word_should_start": ["ტაჯიკ"],
    },
    {
        "iso_country_name": "Tanzania, the United Republic of",
        "id": "TZ",
        "word_should_start": ["ტანზან"],
    },
    {
        "iso_country_name": "Thailand",
        "id": "TH",
        "word_should_start": ["ტაილანდ"],
    },
    # {
    #     "iso_country_name": "Timor-Leste",
    #     "id": "TL",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Togo",
        "id": "TG",
        "word_should_start": [],
        "possible_full_words": [
            "ტოგო",
            "ტოგოში",
            "ტოგომ",
            "ტოგოს",
            "ტოგოური",
            "ტოგოურმა",
            "ტოგოურ",
            "ტოგოელი",
            "ტოგოელ",
            "ტოგოელმა",
        ],
    },
    # {
    #     "iso_country_name": "Tokelau",
    #     "id": "TK",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Tonga",
        "id": "TO",
        "word_should_start": ["ტონგ"],
    },
    {
        "iso_country_name": "Trinidad and Tobago",
        "id": "TT",
        "word_should_start": ["ტრინიდადი"],
    },
    {
        "iso_country_name": "Tunisia",
        "id": "TN",
        "word_should_start": ["ტუნის"],
    },
    {
        "iso_country_name": "Turkey",
        "id": "TR",
        "word_should_start": ["თურქ"],
    },
    {
        "iso_country_name": "Turkmenistan",
        "id": "TM",
        "word_should_start": ["თურქმენ"],
    },
    # {
    #     "iso_country_name": "Turks and Caicos Islands (the)",
    #     "id": "TC",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Tuvalu",
        "id": "TV",
        "word_should_start": ["ტუვალ"],
    },
    {
        "iso_country_name": "Uganda",
        "id": "UG",
        "word_should_start": ["უგანდ"],
    },
    {
        "iso_country_name": "Ukraine",
        "id": "UA",
        "word_should_start": ["უკრაინ"],
    },
    {
        "iso_country_name": "United Arab Emirates (the)",
        "id": "AE",
        "word_should_start": ["არაბეთის საემირ"],
    },
    {
        "iso_country_name": "United Kingdom of Great Britain and Northern Ireland (the)",
        "word_should_start": ["ბრიტან"],
        "id": "GB",
    },
    # {
    #     "iso_country_name": "United States Minor Outlying Islands (the)",
    #     "word_should_start": [],
    #     "id": "UM",
    # },
    {
        "iso_country_name": "United States of America (the)",
        "id": "US",
        "word_should_start": [
            "ა შ შ",
            "აშშ",
            "შეერთებული შტატებ",
            "შეერთებულმა შტატებ",
            "შეერთებულ შტატებ",
        ],
    },
    {
        "iso_country_name": "Uruguay",
        "id": "UY",
        "word_should_start": ["ურუგვ"],
    },
    {
        "iso_country_name": "Uzbekistan",
        "id": "UZ",
        "word_should_start": ["უზბეკ"],
    },
    {
        "iso_country_name": "Vanuatu",
        "id": "VU",
        "word_should_start": ["ვანუატ", "ვანვატ"],
    },
    {
        "iso_country_name": "Venezuela (Bolivarian Republic of)",
        "id": "VE",
        "word_should_start": ["ვენესუელ"],
    },
    {
        "iso_country_name": "Viet Nam",
        "id": "VN",
        "word_should_start": ["ვიეტნამ"],
    },
    # {
    #     "iso_country_name": "Virgin Islands (British)",
    #     "id": "VG",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Virgin Islands (U.S.)",
    #     "id": "VI",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Wallis and Futuna",
    #     "id": "WF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Western Sahara",
        "id": "EH",
        "word_should_start": ["დასავლეთ საჰარ"],
    },
    {
        "iso_country_name": "Yemen",
        "id": "YE",
        "word_should_start": ["იემენ"],
    },
    {
        "iso_country_name": "Zambia",
        "id": "ZM",
        "word_should_start": ["ზამბი"],
    },
    {
        "iso_country_name": "Zimbabwe",
        "id": "ZW",
        "word_should_start": ["ზიმბაბვ"],
    },
    # {
    #     "iso_country_name": "Åland Islands",
    #     "id": "AX",
    #     "word_should_start": [],
    # },
]

POPULATED_AREAS_EXTRACT_INFO = [
    {
        "id": "თბილისი",
    },
    {
        "id": "ქუთაისი",
    },
    {
        "id": "ბათუმი",
    },
    {
        "id": "რუსთავი",
        "skip_these_matches": [
            "რუსთაველი",
            "რუსთაველის",
            "რუსთაველით",
            "რუსთაველზე",
            "რუსთაველთან",
            "რუსთაველამდე",
        ],
    },
    {
        "id": "გორი",
    },
    {
        "id": "ფოთი",
    },
    {
        "id": "ზუგდიდი",
    },
    {
        "id": "სამტრედია",
    },
    {
        "id": "ხაშური",
    },
    {
        "id": "ჭიათურა",
    },
    {
        "id": "ხარაგაული",
    },
    {
        "id": "სენაკი",
    },
    {
        "id": "თელავი",
    },
    {
        "id": "მარნეული",
    },
    {
        "id": "ზესტაფონი",
    },
    {
        "id": "ახალციხე",
    },
    {
        "id": "ოზურგეთი",
    },
    {
        "id": "ტყიბული",
    },
    {
        "id": "ქობულეთი",
    },
    {
        "id": "ბორჯომი",
    },
    {
        "id": "წყალტუბო",
    },
    {
        "id": "ასპინძა",
    },
    {
        "id": "კასპი",
    },
    {
        "id": "გარდაბანი",
    },
    {
        "id": "ახალქალაქი",
    },
    {
        "id": "ბოლნისი",
    },
    {
        "id": "საგარეჯო",
    },
    {
        "id": "ხონი",
    },
    {
        "id": "გურჯაანი",
    },
    {
        "id": "ყვარელი",
    },
    {
        "id": "დედოფლისწყარო",
    },
    {
        "id": "წალენჯიხა",
    },
    {
        "id": "ლაგოდეხი",
    },
    {
        "id": "ჩოხატაური",
    },
    {
        "id": "ლანჩხუთი",
    },
    {
        "id": "ჩხოროწყუ",
    },
    {
        "id": "ახმეტა",
    },
    {
        "id": "მცხეთა",
    },
    {
        "id": "დმანისი",
    },
    {
        "id": "თეთრი წყარო",
        "word_should_start": [
            "თეთრიწყარო",
            "თეთრი წყარო",
        ],
    },
    {
        "id": "დუშეთი",
    },
    {
        "id": "ქარელი",
    },
    {
        "id": "წალკა",
    },
    {
        "id": "საჩხერე",
    },
    {
        "id": "აბაშა",
    },
    {
        "id": "ნინოწმინდა",
    },
    {
        "id": "ხობი",
    },
    {
        "id": "ვანი",
    },
    {
        "id": "თერჯოლა",
    },
    {
        "id": "ვალე",
    },
    {
        "id": "მარტვილი",
    },
    {
        "id": "ბაღდათი",
    },
    {
        "id": "ონი",
    },
    {
        "id": "ჯვარი",
    },
    {
        "id": "სიღნაღი",
    },
    {
        "id": "ლენტეხი",
    },
    {
        "id": "მესტია",
    },
    {
        "id": "ამბროლაური",
    },
    {
        "id": "წნორი",
    },
    {
        "id": "ცაგერი",
    },
    {
        "id": "სოხუმი",
    },
    {
        "id": "ტყვარჩელი",
    },
    {
        "id": "ოჩამჩირე",
    },
    {
        "id": "გუდაუთა",
    },
    {
        "id": "გალი",
    },
    {
        "id": "გულრიფში",
    },
    {
        "id": "ბიჭვინთა",
    },
    {
        "id": "გაგრა",
    },
    {
        "id": "ახალი ათონი",
        "word_should_start": [
            "ახალათონ",
            "ახალიათონ",
            "ახალ ათონ",
            "ახალი ათონ",
        ],
    },
    {
        "id": "ცხინვალი",
    },
    {
        "id": "აბასთუმანი",
    },
    {
        "id": "ადიგენი",
    },
    {
        "id": "ხელვაჩაური",
    },
    {
        "id": "ხულო",
    },
    {
        "id": "შუახევი",
    },
    {
        "id": "ყაზბეგი",
    },
    {
        "id": "ქედა",
    },
    {
        "id": "მანგლისი",
    },
    {
        "id": "აგარა",
    },
    {
        "id": "ფასანაური",
    },
    {
        "id": "სურამი",
    },
    {
        "id": "გუდაური",
    },
    {
        "id": "კაზრეთი",
    },
    {
        "id": "ჟინვალი",
    },
    {
        "id": "სტეფანწმინდა",
    },
    {
        "id": "ბაკურიანი",
    },
]


# to avoid lots of typing, use new helper function to generate listing for us
for info in POPULATED_AREAS_EXTRACT_INFO:
    # this method only supports one word terms for now
    if info["id"].count(" ") > 0:
        continue

    info["word_should_start"] = []
    info["possible_full_words"] = []

    skip_these_matches = info.get("skip_these_matches", set())

    for form in _get_populated_area_word_in_all_different_common_forms(info["id"]):
        if form not in skip_these_matches:
            info["possible_full_words"].append(form)


# add helper to make later steps faster
for arg in [
    COUNTRIES_EXTRACT_INFO,
    POPULATED_AREAS_EXTRACT_INFO,
]:
    for i in arg:
        i["_word_should_start_spaces_nums"] = [j.count(" ") for j in i.get("word_should_start", [])]

# this field values must not have spaces in them
for arg in [
    COUNTRIES_EXTRACT_INFO,
    POPULATED_AREAS_EXTRACT_INFO,
]:
    for i in arg:
        for j in i.get("possible_full_words", []):
            assert j.count(" ") == 0
