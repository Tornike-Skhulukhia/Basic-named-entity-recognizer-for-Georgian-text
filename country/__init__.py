# country - iso 3166 2 letter code
# later we may add also english regexes and get data for both languages using one function depending on language we want data for
# later think about implementing trie which will make extraction of specific word-starting cases much easier
#

COUNTRIES_EXTRACT_INFO = [
    {
        "iso_country_name": "Afghanistan",
        "country_code": "AF",
        "word_should_start": ["ავღან"],
    },
    {
        "iso_country_name": "Albania",
        "country_code": "AL",
        "word_should_start": ["ალბან"],
    },
    {
        "iso_country_name": "Algeria",
        "country_code": "DZ",
        "word_should_start": ["ალჟირ"],
    },
    {
        "iso_country_name": "American Samoa",
        "country_code": "AS",
        "word_should_start": ["სამოა"],
    },
    {
        "iso_country_name": "Andorra",
        "country_code": "AD",
        "word_should_start": ["ანდორ"],
    },
    {
        "iso_country_name": "Angola",
        "country_code": "AO",
        "word_should_start": ["ანგოლ"],
    },
    {
        "iso_country_name": "Anguilla",
        "country_code": "AI",
        "word_should_start": ["ანგილ", "ანგვილ"],
    },
    {
        "iso_country_name": "Antarctica",
        "country_code": "AQ",
        "word_should_start": ["ანტარქტიკ"],
    },
    {
        "iso_country_name": "Antigua and Barbuda",
        "country_code": "AG",
        "word_should_start": ["ანტიგუა და ბარბუდ"],
    },
    {
        "iso_country_name": "Argentina",
        "country_code": "AR",
        "word_should_start": ["არგენტინ"],
    },
    {
        "iso_country_name": "Armenia",
        "country_code": "AM",
        "word_should_start": ["სომხეთ", "სომხურ", "სომეხ"],
    },
    {"iso_country_name": "Aruba", "country_code": "AW", "word_should_start": ["არუბ"]},
    {
        "iso_country_name": "Australia",
        "country_code": "AU",
        "word_should_start": ["ავსტრალ"],
    },
    {
        "iso_country_name": "Austria",
        "country_code": "AT",
        "word_should_start": ["ავსტრი"],
    },
    {
        "iso_country_name": "Azerbaijan",
        "country_code": "AZ",
        "word_should_start": ["აზერბაიჯან"],
    },
    {
        "iso_country_name": "Bahamas (the)",
        "country_code": "BS",
        "word_should_start": ["ბაჰამ"],
    },
    {
        "iso_country_name": "Bahrain",
        "country_code": "BH",
        "word_should_start": ["ბაჰრეინ"],
    },
    {
        "iso_country_name": "Bangladesh",
        "country_code": "BD",
        "word_should_start": ["ბანგლადეშ"],
    },
    {
        "iso_country_name": "Barbados",
        "country_code": "BB",
        "word_should_start": ["ბარბადოს"],
    },
    {
        "iso_country_name": "Belarus",
        "country_code": "BY",
        "word_should_start": ["ბელარუს"],
    },
    {
        "iso_country_name": "Belgium",
        "country_code": "BE",
        "word_should_start": ["ბელგი"],
    },
    {
        "iso_country_name": "Belize",
        "country_code": "BZ",
        "word_should_start": ["ბელიზ"],
    },
    {"iso_country_name": "Benin", "country_code": "BJ", "word_should_start": ["ბენინ"]},
    {
        "iso_country_name": "Bermuda",
        "country_code": "BM",
        "word_should_start": ["ბერმუდ"],
    },
    {
        "iso_country_name": "Bhutan",
        "country_code": "BT",
        "word_should_start": ["ბუტან"],
    },
    {
        "iso_country_name": "Bolivia (Plurinational State of)",
        "country_code": "BO",
        "word_should_start": ["ბოლივი"],
    },
    # {
    #     "iso_country_name": "Bonaire, Sint Eustatius and Saba",
    #     "country_code": "BQ",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Bosnia and Herzegovina",
        "country_code": "BA",
        "word_should_start": ["ბოსნი"],
    },
    {
        "iso_country_name": "Botswana",
        "country_code": "BW",
        "word_should_start": ["ბოცვან"],
    },
    # {
    #     "iso_country_name": "Bouvet Island",
    #     "country_code": "BV",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Brazil",
        "country_code": "BR",
        "word_should_start": ["ბრაზილ"],
    },
    # {
    #     "iso_country_name": "British Indian Ocean Territory (the)",
    #     "country_code": "IO",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Brunei Darussalam",
        "country_code": "BN",
        "word_should_start": ["ბრუნე"],
    },
    {
        "iso_country_name": "Bulgaria",
        "country_code": "BG",
        "word_should_start": ["ბულგარ"],
    },
    {
        "iso_country_name": "Burkina Faso",
        "country_code": "BF",
        "word_should_start": ["ბურკინა ფასო"],
    },
    {
        "iso_country_name": "Burundi",
        "country_code": "BI",
        "word_should_start": ["ბურუნდ"],
    },
    {
        "iso_country_name": "Cabo Verde",
        "country_code": "CV",
        "word_should_start": ["კაბო ვერდ"],
    },
    {
        "iso_country_name": "Cambodia",
        "country_code": "KH",
        "word_should_start": ["კამბოჯ"],
    },
    {
        "iso_country_name": "Cameroon",
        "country_code": "CM",
        "word_should_start": ["კამერუნ"],
    },
    {
        "iso_country_name": "Canada",
        "country_code": "CA",
        "word_should_start": ["კანად"],
    },
    {
        "iso_country_name": "Cayman Islands (the)",
        "country_code": "KY",
        "word_should_start": ["კაიმან"],
    },
    {
        "iso_country_name": "Central African Republic (the)",
        "country_code": "CF",
        "word_should_start": ["აფრიკის რესპუბლიკ"],
    },
    {"iso_country_name": "Chad", "country_code": "TD", "word_should_start": ["ჩად"]},
    {"iso_country_name": "Chile", "country_code": "CL", "word_should_start": ["ჩილე"]},
    {
        "iso_country_name": "China",
        "country_code": "CN",
        "word_should_start": ["ჩინეთ", "ჩინურ", "ჩინელ"],
    },
    # {
    #     "iso_country_name": "Christmas Island",
    #     "country_code": "CX",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Cocos (Keeling) Islands (the)",
    #     "country_code": "CC",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Colombia",
        "country_code": "CO",
        "word_should_start": ["კოლუმბია", "კოლუმბიუ", "კოლუმბიე"],
    },
    {
        "iso_country_name": "Comoros (the)",
        "country_code": "KM",
        "word_should_start": ["კომორის კუნძულ"],
    },
    {
        "iso_country_name": "Congo (the Democratic Republic of the)",
        "word_should_start": ["კონგოს დემოკრატიულ"],
        "country_code": "CD",
    },
    {
        "iso_country_name": "Congo (the)",
        "country_code": "CG",
        "word_should_start": ["კონგო"],
    },
    {
        "iso_country_name": "Cook Islands (the)",
        "country_code": "CK",
        "word_should_start": ["კუკის კუნძულ"],
    },
    {
        "iso_country_name": "Costa Rica",
        "country_code": "CR",
        "word_should_start": ["კოსტა რიკ"],
    },
    {
        "iso_country_name": "Croatia",
        "country_code": "HR",
        "word_should_start": ["ხორვატ"],
    },
    {
        "iso_country_name": "Cuba",
        "country_code": "CU",
        "word_should_start": ["კუბა", "კუბურ", "კუბელ"],
    },
    {
        "iso_country_name": "Curaçao",
        "country_code": "CW",
        "word_should_start": ["კურასაო", "კურაჩაო"],
    },
    {
        "iso_country_name": "Cyprus",
        "country_code": "CY",
        "word_should_start": ["კვიპროს"],
    },
    {
        "iso_country_name": "Czechia",
        "country_code": "CZ",
        "word_should_start": ["ჩეხეთ", "ჩეხურ", "ჩეხელ"],
    },
    {
        "iso_country_name": "Côte d'Ivoire",
        "country_code": "CI",
        "word_should_start": ["კოტ დივუარ"],
    },
    {
        "iso_country_name": "Denmark",
        "country_code": "DK",
        "word_should_start": ["დანია", "დანიურ", "დანიელ"],
    },
    {
        "iso_country_name": "Djibouti",
        "country_code": "DJ",
        "word_should_start": ["ჯიბუტ"],
    },
    {
        "iso_country_name": "Dominica",
        "country_code": "DM",
        "word_should_start": ["დომინიკ"],
    },
    {
        "iso_country_name": "Dominican Republic (the)",
        "country_code": "DO",
        "word_should_start": ["დიმინიკის რესპუბლიკ"],
    },
    {
        "iso_country_name": "Ecuador",
        "country_code": "EC",
        "word_should_start": ["ეკვადორ"],
    },
    {
        "iso_country_name": "Egypt",
        "country_code": "EG",
        "word_should_start": ["ეგვიპტ"],
    },
    {
        "iso_country_name": "El Salvador",
        "country_code": "SV",
        "word_should_start": ["ელ სალვადორ"],
    },
    {
        "iso_country_name": "Equatorial Guinea",
        "country_code": "GQ",
        "word_should_start": ["ეკვატორული გვინ", "ეკვატორულ გვინ"],
    },
    {
        "iso_country_name": "Eritrea",
        "country_code": "ER",
        "word_should_start": ["ერიტრ"],
    },
    {
        "iso_country_name": "Estonia",
        "country_code": "EE",
        "word_should_start": ["ესტონეთ"],
    },
    {
        "iso_country_name": "Eswatini",
        "country_code": "SZ",
        "word_should_start": ["ესვატინ", "სვაზილენდ"],
    },
    {
        "iso_country_name": "Ethiopia",
        "country_code": "ET",
        "word_should_start": ["ეთიოპ"],
    },
    {
        "iso_country_name": "Falkland Islands (the) [Malvinas]",
        "country_code": "FK",
        "word_should_start": ["ფოლკლენდის კუნძულ", "მალვინის კუნძულ"],
    },
    {
        "iso_country_name": "Faroe Islands (the)",
        "country_code": "FO",
        "word_should_start": ["ფარერის კუნძულ"],
    },
    {"iso_country_name": "Fiji", "country_code": "FJ", "word_should_start": ["ფიჯი"]},
    {
        "iso_country_name": "Finland",
        "country_code": "FI",
        "word_should_start": ["ფინეთ", "ფინურ", "ფინელ"],
    },
    {
        "iso_country_name": "France",
        "country_code": "FR",
        "word_should_start": ["საფრანგეთ", "ფრანგ"],
    },
    # {
    #     "iso_country_name": "French Guiana",
    #     "country_code": "GF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "French Polynesia",
        "country_code": "PF",
        "word_should_start": ["პოლინეზი"],
    },
    # {
    #     "iso_country_name": "French Southern Territories (the)",
    #     "country_code": "TF",
    #     "word_should_start": [],
    # },
    {"iso_country_name": "Gabon", "country_code": "GA", "word_should_start": ["გაბონ"]},
    {
        "iso_country_name": "Gambia (the)",
        "country_code": "GM",
        "word_should_start": ["გამბი"],
    },
    {
        "iso_country_name": "Georgia",
        "country_code": "GE",
        "word_should_start": ["საქართველო", "ქართულ", "ქართველ"],
    },
    {
        "iso_country_name": "Germany",
        "country_code": "DE",
        "word_should_start": ["გერმან"],
    },
    {
        "iso_country_name": "Ghana",
        "country_code": "GH",
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
        "country_code": "GI",
        "word_should_start": ["გიბრალტარ"],
    },
    {
        "iso_country_name": "Greece",
        "country_code": "GR",
        "word_should_start": ["საბერძნეთ", "ბერძნ"],
    },
    {
        "iso_country_name": "Greenland",
        "country_code": "GL",
        "word_should_start": ["გრელანდ"],
    },
    {
        "iso_country_name": "Grenada",
        "country_code": "GD",
        "word_should_start": ["გრენად"],
    },
    {
        "iso_country_name": "Guadeloupe",
        "country_code": "GP",
        "word_should_start": ["გუადალუპ", "გვადალუპ"],
    },
    {"iso_country_name": "Guam", "country_code": "GU", "word_should_start": ["გუამ"]},
    {
        "iso_country_name": "Guatemala",
        "country_code": "GT",
        "word_should_start": ["გვატემალ"],
    },
    {
        "iso_country_name": "Guernsey",
        "country_code": "GG",
        "word_should_start": ["გერნს"],
    },
    {
        "iso_country_name": "Guinea",
        "country_code": "GN",
        "word_should_start": ["გვინე"],
    },
    {
        "iso_country_name": "Guinea-Bissau",
        "country_code": "GW",
        "word_should_start": ["გვინეა ბისაუ"],
    },
    {
        "iso_country_name": "Guyana",
        "country_code": "GY",
        "word_should_start": ["გაიან"],
    },
    {"iso_country_name": "Haiti", "country_code": "HT", "word_should_start": ["ჰაიტ"]},
    # {
    #     "iso_country_name": "Heard Island and McDonald Islands",
    #     "country_code": "HM",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Holy See (the)",
    #     "country_code": "VA",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Honduras",
        "country_code": "HN",
        "word_should_start": ["ჰონდურას"],
    },
    {
        "iso_country_name": "Hong Kong",
        "country_code": "HK",
        "word_should_start": ["ჰონგ კონგ", "ჰონგკონგ"],
    },
    {
        "iso_country_name": "Hungary",
        "country_code": "HU",
        "word_should_start": ["უნგრეთ", "უნგრულ", "უნგრელ"],
    },
    {
        "iso_country_name": "Iceland",
        "country_code": "IS",
        "word_should_start": ["ისლანდ"],
    },
    {
        "iso_country_name": "India",
        "country_code": "IN",
        "word_should_start": ["ინდოეთ", "ინდურ", "ინდოელ"],
    },
    {
        "iso_country_name": "Indonesia",
        "country_code": "ID",
        "word_should_start": ["ინდონეზი"],
    },
    {
        "iso_country_name": "Iran (Islamic Republic of)",
        "country_code": "IR",
        "word_should_start": ["ირან"],
    },
    {"iso_country_name": "Iraq", "country_code": "IQ", "word_should_start": ["ერაყ"]},
    {
        "iso_country_name": "Ireland",
        "country_code": "IE",
        "word_should_start": ["ირლანდ"],
    },
    # {
    #     "iso_country_name": "Isle of Man",
    #     "country_code": "IM",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Israel",
        "country_code": "IL",
        "word_should_start": ["ისრაელ", "ისრაულ"],
    },
    {"iso_country_name": "Italy", "country_code": "IT", "word_should_start": ["იტალ"]},
    {
        "iso_country_name": "Jamaica",
        "country_code": "JM",
        "word_should_start": ["იამაიკ"],
    },
    {"iso_country_name": "Japan", "country_code": "JP", "word_should_start": ["იაპონ"]},
    # {
    #     "iso_country_name": "Jersey",
    #     "country_code": "JE",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Jordan",
        "country_code": "JO",
        "word_should_start": ["იორდან"],
    },
    {
        "iso_country_name": "Kazakhstan",
        "country_code": "KZ",
        "word_should_start": ["ყაზახ"],
    },
    {
        "iso_country_name": "Kenya",
        "country_code": "KE",
        "word_should_start": ["კენია", "კენიურ", "კენიელ"],
    },
    {
        "iso_country_name": "Kiribati",
        "country_code": "KI",
        "word_should_start": ["კირიბატ"],
    },
    {
        "iso_country_name": "Korea (the Democratic People's Republic of)",
        "word_should_start": ["ჩრდილოეთ კორე", "ჩრდილო კორე"],
        "country_code": "KP",
    },
    {
        "iso_country_name": "Korea (the Republic of)",
        "country_code": "KR",
        "word_should_start": ["სამხრეთ კორე"],
    },
    {
        "iso_country_name": "Kuwait",
        "country_code": "KW",
        "word_should_start": ["ქუვეით"],
    },
    {
        "iso_country_name": "Kyrgyzstan",
        "country_code": "KG",
        "word_should_start": ["ყირგიზეთ"],
    },
    {
        "iso_country_name": "Lao People's Democratic Republic (the)",
        "word_should_start": ["ლაოს"],
        "country_code": "LA",
    },
    {
        "iso_country_name": "Latvia",
        "country_code": "LV",
        "word_should_start": ["ლატვი"],
    },
    {
        "iso_country_name": "Lebanon",
        "country_code": "LB",
        "word_should_start": ["ლიბან"],
    },
    # {
    #     "iso_country_name": "Lesotho",
    #     "country_code": "LS",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Liberia",
        "country_code": "LR",
        "word_should_start": ["ლიბერი"],
    },
    {
        "iso_country_name": "Libya",
        "country_code": "LY",
        "word_should_start": ["ლიბია", "ლიბიი", "ლიბიურ", "ლიბიელ"],
    },
    {
        "iso_country_name": "Liechtenstein",
        "country_code": "LI",
        "word_should_start": ["ლიხტენშტაინ"],
    },
    {
        "iso_country_name": "Lithuania",
        "country_code": "LT",
        "word_should_start": ["ლიტვ", "ლიეტუვ"],
    },
    {
        "iso_country_name": "Luxembourg",
        "country_code": "LU",
        "word_should_start": ["ლუქსემბურგ"],
    },
    {"iso_country_name": "Macao", "country_code": "MO", "word_should_start": ["მაკაო"]},
    {
        "iso_country_name": "Madagascar",
        "country_code": "MG",
        "word_should_start": ["მადაგასკარ"],
    },
    {
        "iso_country_name": "Malawi",
        "country_code": "MW",
        "word_should_start": ["მალავი", "მალავში", "მალავმა", "მალავურ", "მალაველ"],
    },
    {
        "iso_country_name": "Malaysia",
        "country_code": "MY",
        "word_should_start": ["მალაიზ"],
    },
    {
        "iso_country_name": "Maldives",
        "country_code": "MV",
        "word_should_start": ["მალდივ"],
    },
    {
        "iso_country_name": "Mali",
        "country_code": "ML",
        "word_should_start": ["მალიში", "მალურ", "მალიურ", "მალელ"],
        "possible_full_words": ["მალი", "მალიმ", "მალის"],
    },
    {"iso_country_name": "Malta", "country_code": "MT", "word_should_start": ["მალტ"]},
    {
        "iso_country_name": "Marshall Islands (the)",
        "country_code": "MH",
        "word_should_start": ["მარშალის კუნძულ"],
    },
    {
        "iso_country_name": "Martinique",
        "country_code": "MQ",
        "word_should_start": ["მარტინიკ"],
    },
    {
        "iso_country_name": "Mauritania",
        "country_code": "MR",
        "word_should_start": ["მავრიტან"],
    },
    {
        "iso_country_name": "Mauritius",
        "country_code": "MU",
        "word_should_start": ["მავრიკ"],
    },
    # {
    #     "iso_country_name": "Mayotte",
    #     "country_code": "YT",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Mexico",
        "country_code": "MX",
        "word_should_start": ["მექსიკ"],
    },
    {
        "iso_country_name": "Micronesia (Federated States of)",
        "country_code": "FM",
        "word_should_start": ["მიკრონეზ"],
    },
    {
        "iso_country_name": "Moldova (the Republic of)",
        "country_code": "MD",
        "word_should_start": ["მოლდოვ"],
    },
    {
        "iso_country_name": "Monaco",
        "country_code": "MC",
        "word_should_start": ["მონაკო"],
    },
    {
        "iso_country_name": "Mongolia",
        "country_code": "MN",
        "word_should_start": ["მონღოლეთ", "მონღოლურ", "მონღოლელ"],
    },
    {
        "iso_country_name": "Montenegro",
        "country_code": "ME",
        "word_should_start": ["მონტენეგრ"],
    },
    # {
    #     "iso_country_name": "Montserrat",
    #     "country_code": "MS",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Morocco",
        "country_code": "MA",
        "word_should_start": ["მაროკ"],
    },
    {
        "iso_country_name": "Mozambique",
        "country_code": "MZ",
        "word_should_start": ["მოზამბიკ"],
    },
    {
        "iso_country_name": "Myanmar",
        "country_code": "MM",
        "word_should_start": ["მიანმარ"],
    },
    {
        "iso_country_name": "Namibia",
        "country_code": "NA",
        "word_should_start": ["ნამიბ"],
    },
    {"iso_country_name": "Nauru", "country_code": "NR", "word_should_start": ["ნაურ"]},
    {"iso_country_name": "Nepal", "country_code": "NP", "word_should_start": ["ნეპალ"]},
    {
        "iso_country_name": "Netherlands (the)",
        "country_code": "NL",
        "word_should_start": ["ჰოლანდ", "ნიდერლანდ"],
    },
    {
        "iso_country_name": "New Caledonia",
        "country_code": "NC",
        "word_should_start": ["კალედონი"],
    },
    {
        "iso_country_name": "New Zealand",
        "country_code": "NZ",
        "word_should_start": ["ზელანდ"],
    },
    {
        "iso_country_name": "Nicaragua",
        "country_code": "NI",
        "word_should_start": ["ნიკარაგ"],
    },
    {
        "iso_country_name": "Niger (the)",
        "country_code": "NE",
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
        "country_code": "NG",
        "word_should_start": ["ნიგერია", "ნიგერიულ", "ნიგერიელ"],
    },
    # {
    #     "iso_country_name": "Niue",
    #     "country_code": "NU",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Norfolk Island",
    #     "country_code": "NF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "North Macedonia",
        "country_code": "MK",
        "word_should_start": ["მაკედონ"],
    },
    {
        "iso_country_name": "Northern Mariana Islands (the)",
        "country_code": "MP",
        "word_should_start": ["მარიანას კუნძულ"],
    },
    {
        "iso_country_name": "Norway",
        "country_code": "NO",
        "word_should_start": ["ნორვეგ"],
    },
    {"iso_country_name": "Oman", "country_code": "OM", "word_should_start": ["ომან"]},
    {
        "iso_country_name": "Pakistan",
        "country_code": "PK",
        "word_should_start": ["პაკისტან"],
    },
    {"iso_country_name": "Palau", "country_code": "PW", "word_should_start": ["პალაუ"]},
    {
        "iso_country_name": "Palestine, State of",
        "country_code": "PS",
        "word_should_start": ["პალესტინ"],
    },
    {
        "iso_country_name": "Panama",
        "country_code": "PA",
        "word_should_start": ["პანამ"],
    },
    {
        "iso_country_name": "Papua New Guinea",
        "country_code": "PG",
        "word_should_start": ["ახალი გვინე", "ახალ გვინე"],
    },
    {
        "iso_country_name": "Paraguay",
        "country_code": "PY",
        "word_should_start": ["პარაგვ"],
    },
    {"iso_country_name": "Peru", "country_code": "PE", "word_should_start": ["პერუ"]},
    {
        "iso_country_name": "Philippines (the)",
        "country_code": "PH",
        "word_should_start": ["ფილიპინებ"],
    },
    # {
    #     "iso_country_name": "Pitcairn",
    #     "country_code": "PN",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Poland",
        "country_code": "PL",
        "word_should_start": ["პოლონ"],
    },
    {
        "iso_country_name": "Portugal",
        "country_code": "PT",
        "word_should_start": ["პორტუგალ"],
    },
    {
        "iso_country_name": "Puerto Rico",
        "country_code": "PR",
        "word_should_start": ["პუერტო რიკ"],
    },
    {
        "iso_country_name": "Qatar",
        "country_code": "QA",
        "word_should_start": ["ყატარ", "კატარ"],
    },
    {
        "iso_country_name": "Romania",
        "country_code": "RO",
        "word_should_start": ["რუმინეთ"],
    },
    {
        "iso_country_name": "Russian Federation (the)",
        "country_code": "RU",
        "word_should_start": ["რუსეთ", "რუსულ", "რუსის"],
        "possible_full_words": ["რუსი", "რუს", "რუსმა", "რუსს"],
    },
    {
        "iso_country_name": "Rwanda",
        "country_code": "RW",
        "word_should_start": ["რუანდ"],
    },
    # {
    #     "iso_country_name": "Réunion",
    #     "country_code": "RE",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Barthélemy",
    #     "country_code": "BL",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Helena, Ascension and Tristan da Cunha",
    #     "word_should_start": [],
    #     "country_code": "SH",
    # },
    # {
    #     "iso_country_name": "Saint Kitts and Nevis",
    #     "country_code": "KN",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Lucia",
    #     "country_code": "LC",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Martin (French part)",
    #     "country_code": "MF",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Pierre and Miquelon",
    #     "country_code": "PM",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Saint Vincent and the Grenadines",
    #     "country_code": "VC",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Samoa",
        "country_code": "WS",
        "word_should_start": ["სამოა", "სამოუ", "სომოელ"],
    },
    {
        "iso_country_name": "San Marino",
        "country_code": "SM",
        "word_should_start": ["სან მარინ"],
    },
    # {
    #     "iso_country_name": "Sao Tome and Principe",
    #     "country_code": "ST",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Saudi Arabia",
        "country_code": "SA",
        "word_should_start": ["საუდის არაბე"],
    },
    {
        "iso_country_name": "Senegal",
        "country_code": "SN",
        "word_should_start": ["სენეგალ"],
    },
    {"iso_country_name": "Serbia", "country_code": "RS", "word_should_start": ["სერბ"]},
    {
        "iso_country_name": "Seychelles",
        "country_code": "SC",
        "word_should_start": ["სეიშელ"],
    },
    {
        "iso_country_name": "Sierra Leone",
        "country_code": "SL",
        "word_should_start": ["სიერა ლეონ"],
    },
    {
        "iso_country_name": "Singapore",
        "country_code": "SG",
        "word_should_start": ["სინგაპ"],
    },
    # {
    #     "iso_country_name": "Sint Maarten (Dutch part)",
    #     "country_code": "SX",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Slovakia",
        "country_code": "SK",
        "word_should_start": ["სლოვაკ"],
    },
    {
        "iso_country_name": "Slovenia",
        "country_code": "SI",
        "word_should_start": ["სლოვენ"],
    },
    {
        "iso_country_name": "Solomon Islands",
        "country_code": "SB",
        "word_should_start": ["სოლომონის კუნძულ"],
    },
    {
        "iso_country_name": "Somalia",
        "country_code": "SO",
        "word_should_start": ["სომალ"],
    },
    {
        "iso_country_name": "South Africa",
        "country_code": "ZA",
        "word_should_start": ["სამხრეთ აფრიკ"],
    },
    # {
    #     "iso_country_name": "South Georgia and the South Sandwich Islands",
    #     "word_should_start": [],
    #     "country_code": "GS",
    # },
    {
        "iso_country_name": "South Sudan",
        "country_code": "SS",
        "word_should_start": ["სამხრეთ სუდან"],
    },
    {
        "iso_country_name": "Spain",
        "country_code": "ES",
        "word_should_start": ["ესპანეთ", "ესპანურ", "ესპანელ"],
    },
    {
        "iso_country_name": "Sri Lanka",
        "country_code": "LK",
        "word_should_start": ["შრი ლანკ"],
    },
    {
        "iso_country_name": "Sudan (the)",
        "country_code": "SD",
        "word_should_start": ["სუდან"],
    },
    {
        "iso_country_name": "Suriname",
        "country_code": "SR",
        "word_should_start": ["სურინამ"],
    },
    # {
    #     "iso_country_name": "Svalbard and Jan Mayen",
    #     "country_code": "SJ",
    #     "word_should_start": [],
    # },
    {"iso_country_name": "Sweden", "country_code": "SE", "word_should_start": ["შვედ"]},
    {
        "iso_country_name": "Switzerland",
        "country_code": "CH",
        "word_should_start": ["შვეიცარ"],
    },
    {
        "iso_country_name": "Syrian Arab Republic (the)",
        "country_code": "SY",
        "word_should_start": ["სირია"],
    },
    {
        "iso_country_name": "Taiwan (Province of China)",
        "country_code": "TW",
        "word_should_start": ["ტაივან"],
    },
    {
        "iso_country_name": "Tajikistan",
        "country_code": "TJ",
        "word_should_start": ["ტაჯიკ"],
    },
    {
        "iso_country_name": "Tanzania, the United Republic of",
        "country_code": "TZ",
        "word_should_start": ["ტანზან"],
    },
    {
        "iso_country_name": "Thailand",
        "country_code": "TH",
        "word_should_start": ["ტაილანდ"],
    },
    # {
    #     "iso_country_name": "Timor-Leste",
    #     "country_code": "TL",
    #     "word_should_start": [],
    # },
    {"iso_country_name": "Togo", "country_code": "TG", "word_should_start": ["ტოგო"]},
    # {
    #     "iso_country_name": "Tokelau",
    #     "country_code": "TK",
    #     "word_should_start": [],
    # },
    {"iso_country_name": "Tonga", "country_code": "TO", "word_should_start": ["ტონგ"]},
    {
        "iso_country_name": "Trinidad and Tobago",
        "country_code": "TT",
        "word_should_start": ["ტრინიდადი"],
    },
    {
        "iso_country_name": "Tunisia",
        "country_code": "TN",
        "word_should_start": ["ტუნის"],
    },
    {"iso_country_name": "Turkey", "country_code": "TR", "word_should_start": ["თურქ"]},
    {
        "iso_country_name": "Turkmenistan",
        "country_code": "TM",
        "word_should_start": ["თურქმენ"],
    },
    # {
    #     "iso_country_name": "Turks and Caicos Islands (the)",
    #     "country_code": "TC",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Tuvalu",
        "country_code": "TV",
        "word_should_start": ["ტუვალ"],
    },
    {
        "iso_country_name": "Uganda",
        "country_code": "UG",
        "word_should_start": ["უგანდ"],
    },
    {
        "iso_country_name": "Ukraine",
        "country_code": "UA",
        "word_should_start": ["უკრაინ"],
    },
    {
        "iso_country_name": "United Arab Emirates (the)",
        "country_code": "AE",
        "word_should_start": ["არაბეთის საემირ"],
    },
    {
        "iso_country_name": "United Kingdom of Great Britain and Northern Ireland (the)",
        "word_should_start": ["ბრიტან"],
        "country_code": "GB",
    },
    # {
    #     "iso_country_name": "United States Minor Outlying Islands (the)",
    #     "word_should_start": [],
    #     "country_code": "UM",
    # },
    {
        "iso_country_name": "United States of America (the)",
        "country_code": "US",
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
        "country_code": "UY",
        "word_should_start": ["ურუგვ"],
    },
    {
        "iso_country_name": "Uzbekistan",
        "country_code": "UZ",
        "word_should_start": ["უზბეკ"],
    },
    {
        "iso_country_name": "Vanuatu",
        "country_code": "VU",
        "word_should_start": ["ვანუატ", "ვანვატ"],
    },
    {
        "iso_country_name": "Venezuela (Bolivarian Republic of)",
        "country_code": "VE",
        "word_should_start": ["ვენესუელ"],
    },
    {
        "iso_country_name": "Viet Nam",
        "country_code": "VN",
        "word_should_start": ["ვიეტნამ"],
    },
    # {
    #     "iso_country_name": "Virgin Islands (British)",
    #     "country_code": "VG",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Virgin Islands (U.S.)",
    #     "country_code": "VI",
    #     "word_should_start": [],
    # },
    # {
    #     "iso_country_name": "Wallis and Futuna",
    #     "country_code": "WF",
    #     "word_should_start": [],
    # },
    {
        "iso_country_name": "Western Sahara*",
        "country_code": "EH",
        "word_should_start": ["დასავლეთ საჰარ", "დასავლეთ საჰარ"],
    },
    {"iso_country_name": "Yemen", "country_code": "YE", "word_should_start": ["იემენ"]},
    {
        "iso_country_name": "Zambia",
        "country_code": "ZM",
        "word_should_start": ["ზამბი"],
    },
    {
        "iso_country_name": "Zimbabwe",
        "country_code": "ZW",
        "word_should_start": ["ზიმბაბვ"],
    },
    # {
    #     "iso_country_name": "Åland Islands",
    #     "country_code": "AX",
    #     "word_should_start": [],
    # },
]

# add helper to make later steps faster
for i in COUNTRIES_EXTRACT_INFO:
    i["_word_should_start_spaces_nums"] = [
        j.count(" ") for j in i.get("word_should_start", [])
    ]

