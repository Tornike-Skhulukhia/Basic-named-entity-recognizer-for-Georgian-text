import pytest
from person.get_quotes import get_quotes


# case 1
@pytest.mark.parametrize(
    "text, expected_result",
    [
        (
            """        "ტესტი", - განაცხადა გიორგი გიორგაძემ""",
            [{"person": "გიორგი გიორგაძე", "quote": "ტესტი", "match_case": 1}],
        ),
        (
            """
            "ჩვენ არ ვართ პანიკაში, ვართ ძალიან თანმიმდევრულები, 
            რომ არ ვუპასუხოთ რაიმე პროვოკაციას" - ვოლოდიმერ ზელენსკი
            """,
            [
                {
                    "person": "ვოლოდიმერ ზელენსკი",
                    "quote": """ჩვენ არ ვართ პანიკაში, ვართ ძალიან თანმიმდევრულები, რომ არ ვუპასუხოთ რაიმე პროვოკაციას""",
                    "match_case": 1,
                }
            ],
        ),
        (
            """
            მიხეილ სააკაშვილის დღევანდელი სასამართლო სხდომა დასრულდა. სახელმწიფო ბიუჯეტიდან 9 მილიონამდე ლარის გაფლანგვის საქმის განხილვა ხმაურის ფონზე მიმდინარეობდა. მოსამართლე ბადრი კოჭლამაზაშვილმა პროცესი პირველ მარტამდე გადადო. მიხეილ სააკაშვილი სხდომის დასრულებას არ დალოდებია. საკუთარი სიტყვის შემდეგ ის მხოლოდ ანზორ ჩუბინიძის ჩვენებას დაელოდა.


            სახელმწიფო დაცვის სპეციალური სამსახურის უფროსმა კი, რომელიც მიხეილ სააკაშვილისა და თეიმურაზ ჯანაშიას სისხლის სამართლის საქმეზე დაცვის ინიციატივით მოწმედ იყო წარდგენილი, ჩვენების მიცემაზე უარი განაცხადა და ეს რამდენიმე არგუმენტით ახსნა.


            მისი თქმით, მიმდინარე საქმეზე ბრალდება ეხება 2009-2013 წლამდე პერიოდს, რომლის განმავლობაშიც ის არ იყო სამსახურის ხელმძღვანელი და არანაირი შეხება არ ჰქონდა. ასევე მისი განმარტებით გენერალურ პროკურატურაში მიმდინარეობს გამოძიება 2013 წლის პერიოდთან დაკავშირებით, როცა უკვე ამ სამსახურს ხელმძღვანელობდა და შესაბამისად, დღეს მის მიერ ნათქვამი ნებისმიერი სიტყვა, ფრაზა და დაფიქსირებული პოზიცია შეძლება ისე იყოს ინტერპრეტირებული, რომ გამოყენებული იქნას მის საწინააღმდეგოდ მომავალში.


            ანზორ ჩუბინიძის პოზიციას მოსამართლე დაეთანხმა, რასაც დაცვის მხარის და მიხეილ სააკაშვილის  პროტესტი მოჰყვა.
            "სინდისი არ შეგაწუხებთ ბატონო ანზორ? თქვენ ხომ ზუსტად იცით, რომ ყველაფერი, რაშიც ადანაშაულებენ თქვენს კოლეგას და რაშიც შეიძლება 9 წლით გაუშვან ციხეში... არ შეახსენებენ თქვენს შვილებს და შვილიშვილებს,რომ უდანაშაულო ადამიანი ჩაასმევინეთ ციხეში?"- მიმართა მიხეილ სააკაშვილმა ანზორ ჩუბინიძეს.
            სხდომაზე სიტყვა წარმოთქვა სახელმწიფო დაცვის სპეციალური სამსახურის ყოფილმა უფროსმა თემურ ჯანაშაიამც:
            "არავის მივცემ უფლებას, რომ ჩირქი მოსცხოს სახელმწიფო დაცვის სპეციალურ სამსახურს, ეს არის ჩემი ძირითადი მოტივაცია, რის გამოც ვცდილობ დავადასტურო ის, რომ ჩემი პერიოდის განმავლობაში, ისევე როგორც ჩემამდე და ასევე ჩემს შემდეგ, სამსახურში კანონსაწინააღმდეგო ქმედება არ იყო. მე დღეს მრცხვენია, როდესაც სდსს-ს უფროსი იქცევა ასე, ზურგს აქცევს სიმართლეს, არ უდგას თავის ყოფილ თანამშრომელს გვერდში," - განაცხადა თემურ ჯანაშიამ, რაზეც მოსამართლის პასუხი იყო, რომ ანზორ ჩუბინიძეს აქვს უფლება არ მისცეს ჩვენება საკუთარი თავის ან ახლობლების წინააღმდეგ.

            ანზორ ჩუბინიძის ეპიზოდის შემდეგ დაცვის მხარემ შუამდგომლობით მიმართა მოსამართლეს, რომ მიხეილ სააკაშვილის ჯანმრთელობის მდგომარეობის შესამოწმებლად მასთან საკანში პირადი ექიმი შესულიყო, რაც მოსამართლემ ნაწილობრივ დააკმაყოფილა. მოსამართლის თქმით, ის პენიტენციურ უწყებას სპეციალური განჩინებით მიმართავს, სადაც იქნება მოწოდება, რომ ბრალდებული მიხეილ სააკაშვილის ჯანმრთელობა მაქსიმალურად იყოს დაცული.
            სხდომის დასრულების შემდეგ მედიასთან კომენტარი გააკეთა როგორც დაცვის, ასევე ბრალდების მხარემაც.
            მიხეილ სააკაშვილის ადვოკატი ბექა ბასილაია ამბობს, რომ ანზორ ჩუბინიძის ჩვენების მიცემის შემთხვევაში ცალსახად დადასტურდებოდა, რომ მიხეილ სააკაშვილს და თემურ ჯანაშიას დანაშაული არ ჩაუდენიათ.
            "სასამართლოზე რა მოხდა - ანზორ ჩუბინიძის განცხადებით დადასტურდა, რომ სდსს-ს უფროსი თვლის, რომ  მას აქვს დანაშაული ჩადენილი. სხვა ხომ არაფერია. კითხვებზე პასუხი რომ გაგცეთ, ეს ნიშნავს, რომ მე ბრალს წამიყენებენო," - განაცხადა ბექა ბასილაიამ.

            ანზორ ჩუბინიძის განცხადებას ეხებოდა ბრალდების მხარის კომენტარიც.
            "ანზორ ჩუბინიძის მიერ რა ხარჯი იქნა გაწეული და რა ფორმით, არ არის გამამართლებელი მტკიცებულება დაცვის მხარისთვის, ანზორ ჩუბინიძის მიერ გაწეული დანახარჯი არ ცვლის მოცემულობას, მიხეილ სააკაშვილისა და თემურ ჯანაშიას ბრალდების საქმეზე. ჩვენ ვიხილავთ კონკრეტულ სისხლის სამართლის საქმეს, კონკრეტულ პერიოდზე, კონკრეტულ დანახარჯზე, რომელიც აშკარად არის კანონშეუსაბამო," - განაცხადა პროკურორმა ლევან ვეფხვაძემ.
            """,
            [
                {
                    "person": "მიხეილ სააკაშვილი",
                    "quote": "სინდისი არ შეგაწუხებთ ბატონო ანზორ? თქვენ ხომ ზუსტად იცით, რომ ყველაფერი, რაშიც ადანაშაულებენ თქვენს კოლეგას და რაშიც შეიძლება 9 წლით გაუშვან ციხეში... არ შეახსენებენ თქვენს შვილებს და "
                    "შვილიშვილებს,რომ უდანაშაულო ადამიანი ჩაასმევინეთ ციხეში?",
                    "match_case": 1,
                },
                {
                    "person": "თემურ ჯანაშია",
                    "quote": "არავის მივცემ უფლებას, რომ ჩირქი მოსცხოს სახელმწიფო დაცვის სპეციალურ სამსახურს, ეს არის ჩემი ძირითადი მოტივაცია, რის გამოც ვცდილობ დავადასტურო ის, რომ ჩემი პერიოდის განმავლობაში, ისევე "
                    "როგორც ჩემამდე და ასევე ჩემს შემდეგ, სამსახურში კანონსაწინააღმდეგო ქმედება არ იყო. მე დღეს მრცხვენია, როდესაც სდსს-ს უფროსი იქცევა ასე, ზურგს აქცევს სიმართლეს, არ უდგას თავის ყოფილ "
                    "თანამშრომელს გვერდში,",
                    "match_case": 1,
                },
                {
                    "person": "ბექა ბასილაია",
                    "quote": "სასამართლოზე რა მოხდა - ანზორ ჩუბინიძის განცხადებით დადასტურდა, რომ სდსს-ს უფროსი თვლის, რომ მას აქვს დანაშაული ჩადენილი. სხვა ხომ არაფერია. კითხვებზე პასუხი რომ გაგცეთ, ეს ნიშნავს, რომ "
                    "მე ბრალს წამიყენებენო,",
                    "match_case": 1,
                },
            ],
        ),
    ],
)
def test_1(text, expected_result):
    assert get_quotes(text) == expected_result


# case 2
@pytest.mark.parametrize(
    "text, expected_result",
    [
        (
            """
                გუშინ გიორგი გიორგაძემ რაღაც გააკეთა.
                "მე გუშინ გავაკეთე რაღაც" - ნათქვამია მის განცხადებაში.
                "გუშინ წინაც ვფიქრობდი, მაგრამ გადავიფიქრე", დაამატა გიორგიმ.
            """,
            [
                {
                    "person": "გიორგი გიორგაძე",
                    "quote": "მე გუშინ გავაკეთე რაღაც",
                    "match_case": 2,
                },
                {
                    "person": "გიორგი გიორგაძე",
                    "quote": "გუშინ წინაც ვფიქრობდი, მაგრამ გადავიფიქრე",
                    "match_case": 2,
                },
            ],
        ),
        #####
        (
            """
            უკრაინის პრეზიდენტის, ვოლოდიმერ ზელენსკის თქმით, ის მიუნხენში, 
            უსაფრთხოების კონფერენციაზე ჩავიდა, რათა შეხვედრაზე უკრაინის ხმა გაჟღერებულიყო.
            ამის შესახებ ვოლოდიმერ ზელენსკიმ CNN-ს გერმანიაში განუცხადა.

            "მე ვარ პრეზიდენტი, ძალიან მნიშვნელოვანია ყველა ჩვენი პარტნიორისა
             და მეგობრისთვის, რომ არ მოხდეს შეთანხმება ჩვენს ზურგს უკან. ჩვენ არ ვართ პანიკაში, 
             ჩვენ ძალიან თანმიმდევრულები ვართ, რომ არ ვუპასუხოთ რაიმე პროვოკაციას," - თქვა ზელენსიმ.
            
            მანამდე, ვოლოდიმერ ზელენსკიმ კონფერენციის წევრები შესაძლო 
            ფართომასშტაბიანი ომის შესახებ გააფრთხილა - "მოისმენს ჩემს ხმას მსოფლიო 2022 წელს?" - იკითხა მან. 
            """,
            [
                {
                    "person": "ვოლოდიმერ ზელენსკი",
                    "quote": """მე ვარ პრეზიდენტი, ძალიან მნიშვნელოვანია ყველა ჩვენი პარტნიორისა და მეგობრისთვის, რომ არ მოხდეს შეთანხმება ჩვენს ზურგს უკან. ჩვენ არ ვართ პანიკაში, ჩვენ ძალიან თანმიმდევრულები ვართ, რომ არ ვუპასუხოთ რაიმე პროვოკაციას,""",
                    "match_case": 2,
                },
                {
                    "person": "ვოლოდიმერ ზელენსკი",
                    "quote": "მოისმენს ჩემს ხმას მსოფლიო 2022 წელს?",
                    "match_case": 2,
                },
            ],
        ),
        #####
        (
            """
            უკრაინის პრეზიდენტმა ვლადიმერ ზელენსკიმ მიუნხენის უსაფრთხოების კონფერენციაზე სიტყვით
             გამოსვლისას იმ ვითარებაზე ისაუბრა, რომელიც ქვეყნის შიგნით მიმდინარეობს. როგორც ზელენსკი 
            აღნიშნავს, უკრაინა ყველაფრისთვის მზად არის. 

            "კუბოებში ჩაწოლას და რუსი სამხედროების ლოდინს არ ვაპირებთ. ჩვენ არავისზე თავდასხმას არ ვაპირებთ, 
            თუმცა ყველაფრისთვის მზად ვართ." - ამბობს უკრაინის პრეზიდენტი.
             
            ომის ზღვარზე მყოფი ქვეყნის პრეზიდენტმა კონფერენციის წევრებს კითხვით მიმართა -
            წარმოუდგენიათ თუ არა იმ სახელმწიფოში ცხოვრება, რომელსაც ყოველ დღე ეუბნებიან, რომ ხვალ ომია.

            "ჩვენ არ შეგვიძლია ვიყოთ პასიურები, არ შეგვიძლია ყოველ დღე ვთქვათ, 
            რომ ხვალ ომია. რომელ ეკონომიკაზე შეიძლება იყოს ამის შემდეგ საუბარი. 
            როგორ შეიძლება ცხოვრება სახელმწიფოში, როდესაც ყოველ დღე გეუბნებიან, 
            რომ ხვალ თავს დაგესხმებიან. მაშინ ხდება ეროვნული ვალუტის ჩამოშლა, 
            გააქვთ ფული, ბიზნესი გადის ქვეყნიდან. როგორ ფიქრობთ: შეიძლება ასეთ სახელმწიფოში ცხოვრება? 
            შეიძლება ასეთ სახელმწიფოში სტაბილურობა იყოს? არა!"- განაცხადა ზელენსკიმ.

            მისი თქმით, უკრაინელები არ ნებდებიან, მათ სურთ რომ იცხოვრონ ყოველ დღე და დაიცვან საკუთარი ქვეყანა. 
            "მათ სურთ, რომ უკრაინა სუსტი იყოს, ჰქონდეს სუსტი ეკონომიკა, ჰყავდეს 
            სუსტი ჯარი - მაშინ ჩვენზე თავდასხმა შესაძლებელი იქნება. 
            ჩვენ ვერ შევძლებთ, ვერც ჩვენი ხალხის დაცვას, ვერც ეკონომიკის, 
            ამიტომ ჩვენ მშვიდად ვრეაგირებთ ამა თუ იმ ინფორმაციაზე. ჩვენ ჰიბრიდული ომის პირობებში ვართ. 
            ამიტომ უკრაინელები არ ნებდებიან ამ სიტყვის ყველა მნიშვნელობით. 
            ჩვენ გვსურს ვიცხოვროთ ყოველ დღე და ვიცავდეთ ჩვენს სახელმწიფოს. 
            ჩვენ უბრალოდ გვსურს ვიცხოვროთ, როგორც ძლიერმა სახელმწიფომ,"- განაცხადა ზელენსკიმ. 
            
            """,
            [
                {
                    "person": "ვლადიმერ ზელენსკი",
                    "quote": """კუბოებში ჩაწოლას და რუსი სამხედროების ლოდინს არ ვაპირებთ. ჩვენ არავისზე თავდასხმას არ ვაპირებთ, თუმცა ყველაფრისთვის მზად ვართ.""",
                    "match_case": 2,
                },
                {
                    "person": "ვლადიმერ ზელენსკი",
                    "quote": """ჩვენ არ შეგვიძლია ვიყოთ პასიურები, არ შეგვიძლია ყოველ დღე ვთქვათ, რომ ხვალ ომია. რომელ ეკონომიკაზე შეიძლება იყოს ამის შემდეგ საუბარი. როგორ შეიძლება ცხოვრება სახელმწიფოში, როდესაც ყოველ დღე გეუბნებიან, რომ ხვალ თავს დაგესხმებიან. მაშინ ხდება ეროვნული ვალუტის ჩამოშლა, გააქვთ ფული, ბიზნესი გადის ქვეყნიდან. როგორ ფიქრობთ: შეიძლება ასეთ სახელმწიფოში ცხოვრება? შეიძლება ასეთ სახელმწიფოში სტაბილურობა იყოს? არა!""",
                    "match_case": 2,
                },
                {
                    "person": "ვლადიმერ ზელენსკი",
                    "quote": """მათ სურთ, რომ უკრაინა სუსტი იყოს, ჰქონდეს სუსტი ეკონომიკა, ჰყავდეს სუსტი ჯარი - მაშინ ჩვენზე თავდასხმა შესაძლებელი იქნება. ჩვენ ვერ შევძლებთ, ვერც ჩვენი ხალხის დაცვას, ვერც ეკონომიკის, ამიტომ ჩვენ მშვიდად ვრეაგირებთ ამა თუ იმ ინფორმაციაზე. ჩვენ ჰიბრიდული ომის პირობებში ვართ. ამიტომ უკრაინელები არ ნებდებიან ამ სიტყვის ყველა მნიშვნელობით. ჩვენ გვსურს ვიცხოვროთ ყოველ დღე და ვიცავდეთ ჩვენს სახელმწიფოს. ჩვენ უბრალოდ გვსურს ვიცხოვროთ, როგორც ძლიერმა სახელმწიფომ,""",
                    "match_case": 2,
                },
            ],
        ),
        #####
    ],
)
def test_2(text, expected_result):
    assert get_quotes(text) == expected_result


# weird cases
@pytest.mark.parametrize(
    "text, expected_result",
    [
        (
            """
            "შეგახსენებთ, რომ რუსეთი მთელი თავისი ისტორიის განმავლობაში არასდროს 
            არავის დასხმია თავს.რუსეთი, რომელმაც ამდენი ომი გადაიტანა, 
            უკანასკნელი ქვეყანაა ევროპაში, რომელსაც საერთოდ სიტყვა "ომის" წარმოთქმა
            სურს" – განაცხადა დმიტრი პესკოვმა.

            """,
            [
                {
                    "person": "დმიტრი პესკოვი",
                    "quote": 'შეგახსენებთ, რომ რუსეთი მთელი თავისი ისტორიის განმავლობაში არასდროს არავის დასხმია თავს.რუსეთი, რომელმაც ამდენი ომი გადაიტანა, უკანასკნელი ქვეყანაა ევროპაში, რომელსაც საერთოდ სიტყვა "ომის" წარმოთქმა სურს',
                    "match_case": 1,
                }
            ],
        ),
        #####
        (
            """
            უკრაინის პრეზიდენტის, ვოლოდიმერ ზელენსკის თქმით, ის მიუნხენში, 
            უსაფრთხოების კონფერენციაზე ჩავიდა, რათა შეხვედრაზე უკრაინის ხმა გაჟღერებულიყო.
            ამის შესახებ ვოლოდიმერ ზელენსკიმ CNN-ს გერმანიაში განუცხადა.

            "მე ვარ პრეზიდენტი, ძალიან მნიშვნელოვანია ყველა ჩვენი პარტნიორისა
             და მეგობრისთვის, რომ არ მოხდეს შეთანხმება ჩვენს ზურგს უკან. ჩვენ არ ვართ პანიკაში, 
             ჩვენ ძალიან თანმიმდევრულები ვართ, რომ არ ვუპასუხოთ რაიმე პროვოკაციას," - თქვა ზელენსიმ.
            
            მანამდე, ვოლოდიმერ ზელენსკიმ კონფერენციის წევრები შესაძლო 
            ფართომასშტაბიანი ომის შესახებ გააფრთხილა - "მოისმენს ჩემს ხმას მსოფლიო 2022 წელს?" - იკითხა მან. 
            """,
            [
                {
                    "person": "ვოლოდიმერ ზელენსკი",
                    "quote": """მე ვარ პრეზიდენტი, ძალიან მნიშვნელოვანია ყველა ჩვენი პარტნიორისა და მეგობრისთვის, რომ არ მოხდეს შეთანხმება ჩვენს ზურგს უკან. ჩვენ არ ვართ პანიკაში, ჩვენ ძალიან თანმიმდევრულები ვართ, რომ არ ვუპასუხოთ რაიმე პროვოკაციას,""",
                    "match_case": 2,
                },
                {
                    "person": "ვოლოდიმერ ზელენსკი",
                    "quote": "მოისმენს ჩემს ხმას მსოფლიო 2022 წელს?",
                    "match_case": 2,
                },
            ],
        ),
        #####
        (
            """
            უკრაინის პრეზიდენტმა ვლადიმერ ზელენსკიმ მიუნხენის უსაფრთხოების კონფერენციაზე სიტყვით
             გამოსვლისას იმ ვითარებაზე ისაუბრა, რომელიც ქვეყნის შიგნით მიმდინარეობს. როგორც ზელენსკი 
            აღნიშნავს, უკრაინა ყველაფრისთვის მზად არის. 

            "კუბოებში ჩაწოლას და რუსი სამხედროების ლოდინს არ ვაპირებთ. ჩვენ არავისზე თავდასხმას არ ვაპირებთ, 
            თუმცა ყველაფრისთვის მზად ვართ." - ამბობს უკრაინის პრეზიდენტი.
             
            ომის ზღვარზე მყოფი ქვეყნის პრეზიდენტმა კონფერენციის წევრებს კითხვით მიმართა -
            წარმოუდგენიათ თუ არა იმ სახელმწიფოში ცხოვრება, რომელსაც ყოველ დღე ეუბნებიან, რომ ხვალ ომია.

            "ჩვენ არ შეგვიძლია ვიყოთ პასიურები, არ შეგვიძლია ყოველ დღე ვთქვათ, 
            რომ ხვალ ომია. რომელ ეკონომიკაზე შეიძლება იყოს ამის შემდეგ საუბარი. 
            როგორ შეიძლება ცხოვრება სახელმწიფოში, როდესაც ყოველ დღე გეუბნებიან, 
            რომ ხვალ თავს დაგესხმებიან. მაშინ ხდება ეროვნული ვალუტის ჩამოშლა, 
            გააქვთ ფული, ბიზნესი გადის ქვეყნიდან. როგორ ფიქრობთ: შეიძლება ასეთ სახელმწიფოში ცხოვრება? 
            შეიძლება ასეთ სახელმწიფოში სტაბილურობა იყოს? არა!"- განაცხადა ზელენსკიმ.

            მისი თქმით, უკრაინელები არ ნებდებიან, მათ სურთ რომ იცხოვრონ ყოველ დღე და დაიცვან საკუთარი ქვეყანა. 
            "მათ სურთ, რომ უკრაინა სუსტი იყოს, ჰქონდეს სუსტი ეკონომიკა, ჰყავდეს 
            სუსტი ჯარი - მაშინ ჩვენზე თავდასხმა შესაძლებელი იქნება. 
            ჩვენ ვერ შევძლებთ, ვერც ჩვენი ხალხის დაცვას, ვერც ეკონომიკის, 
            ამიტომ ჩვენ მშვიდად ვრეაგირებთ ამა თუ იმ ინფორმაციაზე. ჩვენ ჰიბრიდული ომის პირობებში ვართ. 
            ამიტომ უკრაინელები არ ნებდებიან ამ სიტყვის ყველა მნიშვნელობით. 
            ჩვენ გვსურს ვიცხოვროთ ყოველ დღე და ვიცავდეთ ჩვენს სახელმწიფოს. 
            ჩვენ უბრალოდ გვსურს ვიცხოვროთ, როგორც ძლიერმა სახელმწიფომ,"- განაცხადა ზელენსკიმ. 
            
            """,
            [
                {
                    "person": "ვლადიმერ ზელენსკი",
                    "quote": """კუბოებში ჩაწოლას და რუსი სამხედროების ლოდინს არ ვაპირებთ. ჩვენ არავისზე თავდასხმას არ ვაპირებთ, თუმცა ყველაფრისთვის მზად ვართ.""",
                    "match_case": 2,
                },
                {
                    "person": "ვლადიმერ ზელენსკი",
                    "quote": """ჩვენ არ შეგვიძლია ვიყოთ პასიურები, არ შეგვიძლია ყოველ დღე ვთქვათ, რომ ხვალ ომია. რომელ ეკონომიკაზე შეიძლება იყოს ამის შემდეგ საუბარი. როგორ შეიძლება ცხოვრება სახელმწიფოში, როდესაც ყოველ დღე გეუბნებიან, რომ ხვალ თავს დაგესხმებიან. მაშინ ხდება ეროვნული ვალუტის ჩამოშლა, გააქვთ ფული, ბიზნესი გადის ქვეყნიდან. როგორ ფიქრობთ: შეიძლება ასეთ სახელმწიფოში ცხოვრება? შეიძლება ასეთ სახელმწიფოში სტაბილურობა იყოს? არა!""",
                    "match_case": 2,
                },
                {
                    "person": "ვლადიმერ ზელენსკი",
                    "quote": """მათ სურთ, რომ უკრაინა სუსტი იყოს, ჰქონდეს სუსტი ეკონომიკა, ჰყავდეს სუსტი ჯარი - მაშინ ჩვენზე თავდასხმა შესაძლებელი იქნება. ჩვენ ვერ შევძლებთ, ვერც ჩვენი ხალხის დაცვას, ვერც ეკონომიკის, ამიტომ ჩვენ მშვიდად ვრეაგირებთ ამა თუ იმ ინფორმაციაზე. ჩვენ ჰიბრიდული ომის პირობებში ვართ. ამიტომ უკრაინელები არ ნებდებიან ამ სიტყვის ყველა მნიშვნელობით. ჩვენ გვსურს ვიცხოვროთ ყოველ დღე და ვიცავდეთ ჩვენს სახელმწიფოს. ჩვენ უბრალოდ გვსურს ვიცხოვროთ, როგორც ძლიერმა სახელმწიფომ,""",
                    "match_case": 2,
                },
            ],
        ),
        #####
        (  # digits should also work
            """
            "111, 222, 333 "444 555" 666 777" - აცხადებს მარიამ მარიამიძე
            """,
            [
                {
                    "person": "მარიამ მარიამიძე",
                    "quote": '111, 222, 333 "444 555" 666 777',
                    "match_case": 1,
                }
            ],
        )
        #####
    ],
)
def test_quote_in_quotes(text, expected_result):
    assert get_quotes(text) == expected_result


# case 3
@pytest.mark.parametrize(
    "text, expected_result",
    [
        (
            """
            ამერიკის შეერთებული შტატების ყოფილმა სახელმწიფო მდივანმა CNN-თან უკრაინაში არსებული ვითარება შეაფასა. 
            კონდოლიზა რაისმა 2008 წელს რუსეთ-საქართველოს ომზეც ისაუბრა და მიხეილ სააკაშვილთან საუბარი გაიხსენა. როგორც 
            რაისი ამბობს, საქართველოს მაშინდელ პრეზიდენტს უთხრა, რომ რუსეთის პროვოკაციას არ უნდა აჰყოლოდა.

            „ჩვენ ვეუბნებოდით სააკაშვილს, რომ რუსეთი ცდილობდა მის პროვოცირებას. ჩვენ ვაფრთხილებდით მას, არ აჰყოლოდა ამ
             პროვოკაციას, მაგრამ რუსეთმა ეს შეძლებს და ომი დაიწყო. ასეთ დროს ჩვენ ყოველთვის ცუდ მდგომარეობაში ვვარდებით. 
             შეერთებული შტატები არ იქნებოდა მზად ეომა საქართველოს გამო რუსეთთან. შეჭრის შემდეგ ლავროვი იყო კატეგორიული 
             ჩვენთან საუბრისას. ერთ-ერთ მისი მოთხოვნა სააკაშვილის წასვლა იყო“, - განაცხადა რაისმა.
        """,
            [
                {
                    "match_case": 3,
                    "person": "კონდოლიზა რაისი",
                    "quote": "ჩვენ ვეუბნებოდით სააკაშვილს, რომ რუსეთი ცდილობდა მის პროვოცირებას. ჩვენ ვაფრთხილებდით მას, არ აჰყოლოდა ამ პროვოკაციას, მაგრამ რუსეთმა ეს შეძლებს და ომი დაიწყო. ასეთ დროს ჩვენ ყოველთვის ცუდ მდგომარეობაში ვვარდებით. შეერთებული შტატები არ იქნებოდა მზად ეომა საქართველოს გამო რუსეთთან. შეჭრის შემდეგ ლავროვი იყო კატეგორიული ჩვენთან საუბრისას. ერთ-ერთ მისი მოთხოვნა სააკაშვილის წასვლა იყო",
                }
            ],
        ),
        (
            """„ლომჯარიას იდიოტური შეკითხვები ეხებოდა პოლიტიკურად ანგაჟირებულ თემებს: ახლადშექმნილი ორი ახალი სამსახურის თანამდებობის პირთა პარლამენტის მიერ არჩევის ქვორუმის თითქოსდა შემცირებას, რაც, რეალურად, სიმართლეს არ შეესაბამება და მარტივად გადამოწმებადია“, - წერს ექსპერტი დავით ქართველიშვილი, რომელიც ეხმიანება ეუთო/ოდირის დასკვნას სახელმწიფო ინსპექტორის სამსახურის რეფორმაზე.

        მისი თქმით, ლომჯარიას წუხილი იმის თაობაზე, რომ სამართალდამცველ და თავდაცვის სისტემებში „მოჭარბებული სტაჟისა და გამოცდილების“ მქონე პირები არ უნდა იკავებდნენ ახალ სტრუქტურებში სახელმძღვანელო რგოლებს, პირველ რიგში, ამ სტაჟისა და გამოცდილების მქონე „ჯერ კიდევ მოქმედ ჩინოვნიკ ლონდა თოლორაიას ურტყამს“ და, ამ კუთხით, უკვე ის ხდება ჩვენი დასაცავი ლომჯარიასაგან.

        „შულერობა და წესიერება შეუთავსებელია ერთმანეთთან, მაგრამ როდესაც ეს მანკიერი ჩვევა ყოველდღიურ ხასიათს ატარებს და შენს სახელმწიფოს აზიანებს, ეს მავნებლობა ქვეყნის ინტერესების ღალატთან არის გაიგივებული. საუბარი მიდის ე.წ. „სახალხო“ დამცველის მორიგ მიზანმიმართულ და უტიფარ საქციელზე. ფაქტების განზრახ დამახინჯების, კანონპროექტის შინაარსობრივი მხარის არგამოჩენით, სამართლებრივი ნარატივის იაფფასიანი პოლიტიკური შინაარსით ჩანაცვლებით - სახელმწიფო ინსპექტორის სამსახურის რეფორმაზე ახალ საკანონმდებლო ინიციატივას კვლავ „ლონდაზე გოდების“ შეფუთვის სახე მიეცა და საქმიან მსჯელობას საერთოდ აცდენილი და დამახინჯებული შეკითხვები გადაეგზავნა ეუთო/ოდირს. იდიოტურ შეკითხვებზე, ლოგიკურად - მსგავსი პასუხიც უნდა გაცემულიყო. და ეს ის შემთხვევაა, როდესაც პასუხის გამცემთან ნაკლები პრეტენზია გაქვს. ამიტომ ითხოვს ანრი ოხანაშვილი ლომჯარიასგან ამ იდიოტური შეკითხვების გასაჯაროებას. ლომჯარიას თუ არ აინტერესებს, რომ აღნიშნული რეფორმა ევროპის ქვეყნების კანონმდებლობის შესაბამისად, საქართველოს კონსტიტუციისა და რეგლამენტის სრული დაცვით განხორციელდა, მისი შულერობა აუცილებლად სამხილებელია. შინაარსობრივად, ეუთო/ოდირის დასკვნაში ვერ ვხდებით არგუმენტებს, თუ ინსტიტუციურად რა ხარვეზს შეიცავს რეფორმა, რაც ბუნებრივია, რადგან მსგავსი ხარვეზი უბრალოდ არ არსებობს. ლომჯარიას იდიოტური შეკითხვები ეხებოდა პოლიტიკურად ანგაჟირებულ თემებს: ახლადშექმნილი ორი ახალი სამსახურის თანამდებობის პირთა პარლამენტის მიერ არჩევის ქვორუმის თითქოსდა შემცირებას, რაც, რეალურად, სიმართლეს არ შეესაბამება და მარტივად გადამოწმებადია. დასკვნაში ასევე წერია, რომ, თითქოს, გაუქმდა ამ თანამდებობის პირთა მიმართ საპარლამენტო კონტროლის მექანიზმები, რაც ასევე არ შეესაბამება სიმართლეს საქართველოს პარლამენტის რეგლამენტის თანახმად. ხოლო ლომჯარიას წუხილი იმის თაობაზე, რომ სამართალდამცველ და თავდაცვის სისტემებში „მოჭარბებული სტაჟისა და გამოცდილების“ მქონე პირები არ უნდა იკავებდნენ ახალ სტრუქტურებში სახელმძღვანელო რგოლებს, პირველ რიგში, ამ სტაჟისა და გამოცდილების მქონე ჯერ კიდევ მოქმედ ჩინოვნიკ ლონდა თოლორაიას ურტყამს და, ამ კუთხით, უკვე ის ხდება ჩვენი დასაცავი ლომჯარიასგან“ - წერს ქართველიშვილი Facebook-ზე.""",
            [
                {
                    "match_case": 2,
                    "person": "დავით ქართველიშვილი",
                    "quote": "ლომჯარიას იდიოტური შეკითხვები ეხებოდა პოლიტიკურად ანგაჟირებულ თემებს: ახლადშექმნილი ორი ახალი სამსახურის თანამდებობის პირთა პარლამენტის მიერ არჩევის ქვორუმის თითქოსდა შემცირებას, რაც, რეალურად, სიმართლეს არ შეესაბამება და მარტივად გადამოწმებადია",
                },
                {
                    "match_case": 2,
                    "person": "დავით ქართველიშვილი",
                    "quote": "შულერობა და წესიერება შეუთავსებელია ერთმანეთთან, მაგრამ როდესაც ეს მანკიერი ჩვევა ყოველდღიურ ხასიათს ატარებს და შენს სახელმწიფოს აზიანებს, ეს მავნებლობა ქვეყნის ინტერესების ღალატთან არის გაიგივებული. საუბარი მიდის ე.წ. „სახალხო“ დამცველის მორიგ მიზანმიმართულ და უტიფარ საქციელზე. ფაქტების განზრახ დამახინჯების, კანონპროექტის შინაარსობრივი მხარის არგამოჩენით, სამართლებრივი ნარატივის იაფფასიანი პოლიტიკური შინაარსით ჩანაცვლებით - სახელმწიფო ინსპექტორის სამსახურის რეფორმაზე ახალ საკანონმდებლო ინიციატივას კვლავ „ლონდაზე გოდების“ შეფუთვის სახე მიეცა და საქმიან მსჯელობას საერთოდ აცდენილი და დამახინჯებული შეკითხვები გადაეგზავნა ეუთო/ოდირს. იდიოტურ შეკითხვებზე, ლოგიკურად - მსგავსი პასუხიც უნდა გაცემულიყო. და ეს ის შემთხვევაა, როდესაც პასუხის გამცემთან ნაკლები პრეტენზია გაქვს. ამიტომ ითხოვს ანრი ოხანაშვილი ლომჯარიასგან ამ იდიოტური შეკითხვების გასაჯაროებას. ლომჯარიას თუ არ აინტერესებს, რომ აღნიშნული რეფორმა ევროპის ქვეყნების კანონმდებლობის შესაბამისად, საქართველოს კონსტიტუციისა და რეგლამენტის სრული დაცვით განხორციელდა, მისი შულერობა აუცილებლად სამხილებელია. შინაარსობრივად, ეუთო/ოდირის დასკვნაში ვერ ვხდებით არგუმენტებს, თუ ინსტიტუციურად რა ხარვეზს შეიცავს რეფორმა, რაც ბუნებრივია, რადგან მსგავსი ხარვეზი უბრალოდ არ არსებობს. ლომჯარიას იდიოტური შეკითხვები ეხებოდა პოლიტიკურად ანგაჟირებულ თემებს: ახლადშექმნილი ორი ახალი სამსახურის თანამდებობის პირთა პარლამენტის მიერ არჩევის ქვორუმის თითქოსდა შემცირებას, რაც, რეალურად, სიმართლეს არ შეესაბამება და მარტივად გადამოწმებადია. დასკვნაში ასევე წერია, რომ, თითქოს, გაუქმდა ამ თანამდებობის პირთა მიმართ საპარლამენტო კონტროლის მექანიზმები, რაც ასევე არ შეესაბამება სიმართლეს საქართველოს პარლამენტის რეგლამენტის თანახმად. ხოლო ლომჯარიას წუხილი იმის თაობაზე, რომ სამართალდამცველ და თავდაცვის სისტემებში „მოჭარბებული სტაჟისა და გამოცდილების“ მქონე პირები არ უნდა იკავებდნენ ახალ სტრუქტურებში სახელმძღვანელო რგოლებს, პირველ რიგში, ამ სტაჟისა და გამოცდილების მქონე ჯერ კიდევ მოქმედ ჩინოვნიკ ლონდა თოლორაიას ურტყამს და, ამ კუთხით, უკვე ის ხდება ჩვენი დასაცავი ლომჯარიასგან",
                },
            ],
        ),
    ],
)
def test_3(text, expected_result):
    assert get_quotes(text) == expected_result


@pytest.mark.parametrize(
    "text",
    [
        """
            ანზორ ჩუბინიძის განცხადებას ეხებოდა ბრალდების მხარის კომენტარიც.

            "ანზორ ჩუბინიძის მიერ რა ხარჯი იქნა გაწეული და რა ფორმით, არ არის გამამართლებელი მტკიცებულება დაცვის მხარისთვის, ანზორ ჩუბინიძის მიერ გაწეული დანახარჯი არ ცვლის მოცემულობას, მიხეილ სააკაშვილისა და თემურ ჯანაშიას ბრალდების საქმეზე. ჩვენ ვიხილავთ კონკრეტულ სისხლის სამართლის საქმეს, კონკრეტულ პერიოდზე, კონკრეტულ დანახარჯზე, რომელიც აშკარად არის კანონშეუსაბამო," - განაცხადა პროკურორმა ლევან ვეფხვაძემ.
        """,
        """
            "ერთი, ორი, სამი, "რაღაც ფრაზა" აცხადებს მარიამ მარიამიძე
        """,
    ],
)
def test_must_not_matches(text):
    assert get_quotes(text) == []


# # dev mode
# from pprint import pprint as pp

# text = """

# დაწყებას ეხმაურება.

# მისი თქმით, ის არ იზიარებს მიხელ სააკაშვილის ამ გადაწყვეტილებას, ვინაიდან ეს იქნება დიდი რისკის შემცველი მისი ჯანმრთელობისთვის, რადგან მესამე პრეზიდენტს პირველი შიმშილობის შემდეგ, ჯანმრთელობა ისედაც მძიმე მდგომარეობაში აქვს.

# "დიდი რისკის შემცველი იქნება ეს იმიტომ, რომ ის პირველი შიმშილობა მძიმე იყო, მაგრამ ის იყო სრულიად ჯანმრთელი მაშინ სხვა რესურსი ჰქონდა ადამიანური და ახლა არის აბსოლუტურად სხვა რეალობა, იმიტომ რომ განახევრებული აქვს ჯანმრთელობა და ძალიან კრიტიკულია მისი მდგომარეობა, აქედან გამომდინარე არაფრის ვარაუდი არ შეგვიძლია კარგის...
# მაქვს უფლება, რომ ჩემი პოზიცია ვთქვა. სრულად არ ვიზიარებ, იმიტომ რომ მე ვიცი , წარმომიდგენია რაც შეიძლება მოყვეს ამ ყველაფერს და მართლაც ცუდ განწყობაზე ვარ იმიტომ, რომ მე არ ვიცი, ხვალ , ზეგ, მასზეგ როგორც განვითარდება მოვლენები, მას ძალიან მცირე რესურსი აქვს ჯანმრთელობის კუთხით, იმისა რომ გაძლოს ამ ვითარებაში. და ახლა  რა თქმა უნდა ყველაზე მეტად სანერვიულო ეს ფაქტორი გახლავთ ვიდრე სხვა საკითხები." - ამბობს ეკა ხერხეულიძე დღის სტუმრის ეთერში.
# """


# resp = get_quotes(text, v=1)

# pp(resp, width=500)
