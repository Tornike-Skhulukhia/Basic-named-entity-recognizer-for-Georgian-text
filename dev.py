"""
Some temporary scripts
"""
from pprint import pprint as pp
from person.get_quotes import get_quotes
from person.get_quotes import _encode_quotes_in_quotes

# def test_():
#     text = """
#             უკრაინის პრეზიდენტმა ვლადიმერ ზელენსკიმ მიუნხენის უსაფრთხოების კონფერენციაზე
#              სიტყვით გამოსვლისას იმ ვითარებაზე ისაუბრა, რომელიც ქვეყნის შიგნით
#               მიმდინარეობს. როგორც ზელენსკი აღნიშნავს, უკრაინა ყველაფრისთვის მზად არის.

#             "კუბოებში ჩაწოლას და რუსი "სამხედროების" ლოდინს არ ვაპირებთ. ჩვენ
#             არავისზე თავდასხმას არ ვაპირებთ, თუმცა ყველაფრისთვის მზად ვართ."
#             - ამბობს უკრაინის პრეზიდენტი.
#         """
# "111, 222, 333 "444 555" 666 777" - აცხადებს მარიამ მარიამიძე
# „ნაციონალური მოძრაობის“ თავმჯდომარის, ნიკა მელიას განცხადებით, დღეს „ერთიანი ნაციონალური მოძრაობის“ პოლიტიკური საბჭოს სხდომა გაიმართა, რომელზეც გადაწყდა, რომ პარტიის ცენტრალური საკითხი არის მიხეილ სააკაშვილის სიცოცხლის გადარჩენა. ნიკა მელიას თქმით, სააკაშვილის ჯანმრთელობის მდგომარეობა დღითიდღე მძიმდება და აღნიშნა, რომ კონსილიუმის წევრები, უცხოელი ექიმები ერთხმად აღნიშნავენ, რომ მისი მკურნალობა საქართველოში შეუძლებელია. „მოგეხსენებათ, რომ სახალხო დამცველის მიერ შექმნილი კონსილიუმი, ცენტრი „ემპათია“, უცხოელი ექიმები, მიხეილ სააკაშვილის პირადი ექიმი ერთხმად აღნიშნავენ, რომ მიხეილ სააკაშვილის მძიმე ჯანმრთელობის მდგომარეობა, რომელიც დღითიდღე მძიმდება და მძიმდება, არ ექვემდებარება საქართველოში განკურნებას. აქედან გამომდინარე, ერთადერთი გზა მიხეილ სააკაშვილის სიცოცხლის გადარჩენის არის შემდეგი – მიხეილ სააკაშვილი იყოს გადაყვანილი ქვეყნის ფარგლებს გარეთ უცხოურ კლინიკაში, შესაბამისი მკურნალობის მისაღებად. ძალიან დასანანია, რომ ამ ჰუმანიტარული საკითხის გამო გვიწევს პოლიტიკური ბრძოლა. ჰუმანიტარულია ის საკითხი, რომელიც ადამიანის, ქვეყნის მესამე პრეზიდენტის, მიხეილ სააკაშვილის სიცოცხლეს ეხება“, – აღნიშნა მელიამ. მისივე თქმით, პარტიის ყველა აქტივობა დაუკავშირდება მიხეილ სააკაშვილის სიცოცხლის გადარჩენას. „ჩვენ ვიყავით ბრძოლაში და ვრჩებით ბრძოლაში იქამდე, ვიდრე არ იქნება უზრუნველყოფილი მისი სიცოცხლე და ჯანმრთელობა, რაც მიმაჩნია, არის თითოეული ჩვენი პარტიის წევრის, ამომრჩევლის, მხარდამჭერის მთავარი ცენტრალური საკითხი“, – განაცხადა ნიკა მელიამ. მისივე თქმით, 5 მარტიდან სხვადასხვა ქალაქში საპროტესტო აქციები გაიმართება. „სხვადასხვა ფორმისა და შინაარსის საპროტესტო აქტივობები გაიმართება სხვადასხვა ქალაქში. 5 მარტს, 17:00 საათზე რუსთაველის გამზირზე ველოდებით ქვეყნის მოსახლეობის იმ ნაწილს, რომელიც თვლის, რომ ეს ისტორიული უსამართლობა უნდა დასრულდეს და ამ ბრძოლაში არიან“, – განაცხადა ნიკა მელიამ.
text = """


მაკა ბოჭორიშვილი, ევროკავშირის ეროვნული პარლამენტების ევროპულ საქმეთა კომიტეტების კონფერენციის (COSAC) პლენარულ სესიაში ევროკავშირის თავმჯდომარე ქვეყნის, საფრანგეთისა და საპრეზიდენტო ტრიოს (სლოვენია, საფრანგეთი, ჩეხეთი) სპეციალური მოწვევით მონაწილეობს.

კონფერენციაზე საფრანგეთის პრემიერ მინისტრის ჟან კასტექსის მონაწილეობით გაიმართა დებატები საფრანგეთის ევროკავშირის თავმჯდომარეობის შესახებ. ევროკავშირის წევრი ქვეყნების წარმომადგენლებმა უკრაინაში მიმდინარე მოვლენებზე ისაუბრეს.

სიტყვით გამოსვლისას, მაკა ბოჭორიშვილმა დაგმო რუსეთის აგრესია უკრაინის მიმართ. ,,ეს არის ტრაგედია, რომელიც შუაგულ ევროპაში ხდება. დღეს, როდესაც რუსეთის მიერ აბსოლუტურად გაუმართლებელი აგრესია მიმდინარეობს, უკრაინელი ხალხი იბრძვის არა მხოლოდ უკრაინისთვის, არამედ ევროპისა და მისი უსაფრთხოებისთვის. 2008 წელს საქართველოში რუსეთის შემოჭრის შემდეგ, ჩვენს პარტნიორებთან გამუდმებით ვსაუბრობდით საფრთხეზე, რომელიც რუსეთის მიერ საქართველოს რეგიონების ოკუპაციის შემდეგ ჩვენს ყოველდღიურად იქცა. სამწუხაროა, რომ საფრთხის სიმძიმე ბოლომდე ვერ იქნა გაცნობიერებული და ვერ შევძელით დღევანდელი ტრაგედიის თავიდან აცილება“, - განაცხადა მაკა ბოჭორიშვილმა.

მან ევროკავშირის წევრი ქვეყნების წარმომადგენლებს გააცნო საქართველოს გადაწყვეტილება ევროკავშირში გაწევრიანების შესახებ და მხარდაჭერისკენ მოუწოდა:

„ამ მძიმე ფონზე, უკრაინამ, საქართველომ და მოლდოვამ ევროკავშირში გაწევრიანებაზე განაცხადი გააკეთეს და თქვენ ამ საკითხზე უახლოეს პერიოდში მოგიწევთ მსჯელობა. ჩემი თხოვნა იქნება, მოუსმინეთ ჩვენს ხმას, იმისათვის, რომ ევროპა გახდეს სრულყოფილი.” - განაცხადა მაკა ბოჭორიშვილმა.

პარიზში, საფრანგეთის ეროვნულ ასამბლეაში, ევროკავშირის ეროვნული პარლამენტების ევროპულ საქმეთა კომიტეტების კონფერენციის (COSAC) პლენარული სხდომა 4-5 მარტს გრძელდება. სხდომაში ევროკავშირის 27 წევრი სახელმწიფოს და კანდიდატი ქვეყნების პარლამენტები მონაწილეობენ. საქართველოს საპარლამენტო დელეგაციას ევროპასთან ინტეგრაციის კომიტეტის თავმჯდომარე, მაკა ბოჭორიშვილი და ეკონომიკური პოლიტიკის კომიტეტის თავმჯომარე, დავით სონღულაშვილი წარმოდგენენ. 
"""

resp = get_quotes(text, v=1)
# resp = _encode_quotes_in_quotes(text)

"""
Not correct results for text on page

https://mtavari.tv/news/74759-nina-khubutia-ukrainuli-mediis-quradghebis

"""

pp(resp)
print("\n" * 4)
print(resp)