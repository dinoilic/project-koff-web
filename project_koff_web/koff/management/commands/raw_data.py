from project_koff_web.koff import models
import datetime

CATEGORIES_AND_BUSINESSES = [
    {'name': 'Auto moto i nautika', 'image': "category_images/icons8-car-96.png", "subcategories": [
        {'name': 'Auspuh, Auto staklo, Auto plin', 'image': 'category_images/icons8-gas-station-96.png', 'businesses': [
            {
                'name': 'TONI AUSPUH',
                'address': 'Tometići, 51215, Kastav',
                'e_mail': ['toni@mail.hr', 'toni2@mail.hr'],
                'web_site': ['toni.hr', 'toni2.hr'],
                'telephone_numbers': ['0913319384', '051882123'],
                'description': """Ja sam *TONI AUSPUH*, vodeći popravljač ~~auspuha~~ ispušnih cijevi. Popravljam sljedeće:
- auspuhe
- ispušne cijevi
- vodiče otpadnih plinova iz automobila
- može i skuter, a i podmornica ako ima auspuh""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [
                    {'name': models.WorkingHours.Mon, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Tue, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Wed, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Thu, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Fri, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Sat, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(13, 0)},
                ]
            },
            {
                'name': 'BRTAN DARKO - SERVIS',
                'address': 'Minakovo 27, 51000, Rijeka',
                'e_mail': ['darko@mail.hr'],
                'web_site': ['darko.hr'],
                'telephone_numbers': ['051256323'],
                'description': """Moj ime je Darko i vodim svoj servis. Kako je delal moj deda tako delan i ja. Popravljam sljedeće:
- Citroen
- Volkswagen
- eksluzivni sam popravljač Trabant automobila
- u slobodno vrijeme popravljam i male motorine""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [
                    {'name': models.WorkingHours.Mon, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Tue, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Wed, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Thu, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Fri, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Sat, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(20, 0)},
                    {'name': models.WorkingHours.Sun, 'start_time': datetime.time(8, 0), 'end_time': datetime.time(13, 0)},
                ]
            },
            {
                'name': 'BOLJI d.o.o.',
                'address': 'Ulica dr. Zdravka Kučića 50, 51000, Rijeka',
                'e_mail': ['bolji@mail.hr'],
                'web_site': ['bolji.hr'],
                'telephone_numbers': ['0919030000'],
                'description': """Dobar. Bolji. Najbolji. To smo mi. Nismo ni dobri ni najbolji.

Mi smo jednostavno **bolji** d.o.o.""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            },
            {
                'name': 'Auspuh M.K.',
                'address': 'Heinzelova ul. 74, 10000, Zagreb',
                'e_mail': ['mk@mail.hr'],
                'web_site': ['mk.hr'],
                'telephone_numbers': ['08009000'],
                'description': """Specijalizirani smo za auspuhe, ali popravljamo i:
- motore
- male barke
- velike barke
- Airbus A320""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            },
            {
                'name': 'Car Service Bivio',
                'address': 'Istarska ul. 92, 51000, Rijeka',
                'e_mail': ['bivio@mail.hr'],
                'web_site': ['bivio.hr'],
                'telephone_numbers': [],
                'description': """Popravljamo aute **samo** za stanovnike Bivia!""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            },
            {
                'name': 'AUTOMEHANIČAR TIHOMIR VESIĆ MLAĐI I SINOVI',
                'address': 'Ul. Ante Mandića 37, 51000, Rijeka',
                'e_mail': ['tihomir@mail.hr', 'tihomir2@mail.hr'],
                'web_site': ['tihomir.hr', 'mehanicar.tihomir.hr'],
                'telephone_numbers': ['0915554732'],
                'description': """Aute popravljamo:
- ja
- moj sin Mihomir Vesić
- njegov brat Bihomir Vesić
- susjed Nevio""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            },
            {
                'name': 'Autoservis Gordan',
                'address': 'Ul. Milice Jadranić 7B, 51000, Rijeka',
                'e_mail': ['gordan@mail.hr', 'gordan.gordan@mail.hr'],
                'web_site': ['gordan.hr'],
                'telephone_numbers': [],
                'description': """Volim *popravke* automobila""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            }
        ]},
        {'name': 'Auto dijelovi', 'image': 'category_images/icons8-car-battery-96.png', 'businesses': [
        ]},
        {'name': 'Auto elektrika, alarm, audio-oprema', 'image': 'category_images/icons8-radio-station-96.png', 'businesses': [
        ]},
        {'name': 'Auto klima', 'image': 'category_images/icons8-air-conditioner-96.png', 'businesses': [
        ]},
        {'name': 'Automehaničar', 'image': 'category_images/icons8-maintenance-96.png', 'businesses': [
        ]},
        {'name': 'Auto otpad', 'image': 'category_images/icons8-recycle-96.png', 'businesses': [
        ]},
        {'name': 'Autopraonica', 'image': 'category_images/icons8-broom-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Gradnja', 'image': 'category_images/icons8-construction-96.png', 'subcategories': [
        {'name': 'Alarmni sustavi, video nadzor', 'image': 'category_images/icons8-bullet-camera-96.png', 'businesses': [
        ]},
        {'name': 'Boje i lakovi', 'image': 'category_images/icons8-paint-bucket-96.png', 'businesses': [
            {
                'name': 'Boje i lakovi, voze li vlakovi?',
                'address': 'Mihanovićeva ul. 35, 51000, Rijeka',
                'e_mail': ['mirko@mail.hr', 'marko@mail.hr'],
                'web_site': ['bojeilakovi.hr'],
                'telephone_numbers': [],
                'description': """Volim farbu, volim lak, kada vidim lošu farbu diže mi se tlak.""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            },
            {
                'name': 'Jupol u srcu mom',
                'address': 'Mihanovićeva ul. 5, 51000, Rijeka',
                'e_mail': ['zeljko@jupol.hr'],
                'web_site': ['jupol.hr'],
                'telephone_numbers': [],
                'description': """""",
                'tags': ['auspuh', 'auto'],
                'working_hours': [

                ]
            }
        ]},
        {'name': 'Čišćenje dimnjaka', 'image': 'category_images/icons8-roofing-96.png', 'businesses': [
        ]},
        {'name': 'Električar, Elektroinstalacije, Elektro servis', 'image': 'category_images/icons8-switchboard-96.png', 'businesses': [
        ]},
        {'name': 'Podne obloge', 'image': 'category_images/icons8-floor-plan-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Dom i ured', 'image': 'category_images/icons8-organization-96.png', 'subcategories': [
        {'name': 'Audio servis, video servis, TV servis', 'image': 'category_images/icons8-tv-96.png', 'businesses': [
        ]},
        {'name': 'Brava, ključ - izrada, ugradnja, servis', 'image': 'category_images/icons8-key-96.png', 'businesses': [
        ]},
        {'name': 'Čišćenje, dezinfekcija, dezinsekcija, deratizacija', 'image': 'category_images/icons8-rat-96.png', 'businesses': [
        ]},
        {'name': 'Električar, Elektroinstalacije, Elektro servis', 'image': 'category_images/icons8-switchboard-96.png', 'businesses': [
        ]},
        {'name': 'Servis kućanskih aparata', 'image': 'category_images/icons8-washing-machine-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Računala i telekomunikacije', 'image': 'category_images/icons8-monitor-96.png', 'subcategories': [
        {'name': 'Elektronika - proizvodnja, prodaja, servis', 'image': 'category_images/icons8-multiple-devices-96.png', 'businesses': [
        ]},
        {'name': 'Servis mobitela', 'image': 'category_images/icons8-touchscreen-96.png', 'businesses': [
        ]},
        {'name': 'Servis računala, servis kompjutera', 'image': 'category_images/icons8-system-information-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Prijevoz', 'image': 'category_images/icons8-public-transportation-96.png', 'subcategories': [
        {'name': 'Autobusni prijevoz', 'image': 'category_images/icons8-bus-96.png', 'businesses': [
        ]},
        {'name': 'Pomoć za selidbu', 'image': 'category_images/icons8-in-transit-96.png', 'businesses': [
        ]},
        {'name': 'Taxi prijevoz', 'image': 'category_images/icons8-taxi-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Slobodno vrijeme i izlasci', 'image': 'category_images/icons8-cocktail-96.png', 'subcategories': [
        {'name': 'Bazen', 'image': 'category_images/icons8-swimming-pool-96.png', 'businesses': [
        ]},
        {'name': 'Kino i kazalište', 'image': 'category_images/icons8-theatre-mask-96.png', 'businesses': [
        ]},
        {'name': 'Muzej, umjetnine', 'image': 'category_images/icons8-museum-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Usluge i servisi', 'image': 'category_images/icons8-support-96.png', 'subcategories': [
        {'name': 'Glazbeni instrumenti i oprema', 'image': 'category_images/icons8-rock-music-96.png', 'businesses': [
        ]},
        {'name': 'Tarot, astrologija', 'image': 'category_images/icons8-fortune-teller-96.png', 'businesses': [
        ]},
        {'name': 'Masaža', 'image': 'category_images/icons8-physical-therapy-96.png', 'businesses': [
        ]},
    ]},
    {'name': 'Sport i rekreacija', 'image': 'category_images/icons8-badminton-96.png', 'subcategories': [
        {'name': 'Fitness centar', 'image': 'category_images/icons8-fitness-96.png', 'businesses': [
        ]},
        {'name': 'Ski oprema, ski servis', 'image': 'category_images/icons8-skiing-96.png', 'businesses': [
        ]},
        {'name': 'Plesna škola, glazbena škola', 'image': 'category_images/icons8-dancing-96.png', 'businesses': [
        ]},
    ]},
]

USERS = [
    {'username': 'john', 'email': 'john@koff.com', 'password': 'john', 'first_name': "Ivo", 'last_name': "Čokolino"},
    {'username': 'andrew', 'email': 'andrew@koff.com', 'password': 'andrew', 'first_name': "Andrija", 'last_name': "Mesarić"},
    {'username': 'tim', 'email': 'tim@koff.com', 'password': 'tim', 'first_name': "Tim", 'last_name': "Evidentić"},
    {'username': 'mark', 'email': 'mark@koff.com', 'password': 'mark', 'first_name': "Marko", 'last_name': "Veličanstveni"},
    {'username': 'mile', 'email': 'mile@koff.com', 'password': 'mile', 'first_name': "Mile", 'last_name': "Miletić"},
    {'username': 'dino', 'email': 'dino@koff.com', 'password': 'dino', 'first_name': "Dino", 'last_name': "Obersnel"},
]
