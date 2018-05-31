from django.core.management.base import BaseCommand
from project_koff_web.koff import models
from django.contrib.auth import get_user_model
import datetime

import googlemaps  # used for geocoding
from django.contrib.gis.geos import GEOSGeometry
from django.utils import translation


class Command(BaseCommand):
    help = 'Removes old data and populates database with new test data'

    def handle(self, *args, **options):
        translation.activate('hr')
        User = get_user_model()
        if User.objects.exists() or \
            models.TelephoneReference.objects.exists() or \
            models.Category.objects.exists() or \
            models.BusinessEntity.objects.exists() or \
            models.WorkingHours.objects.exists() or \
            models.RatingAndComment.objects.exists():

            User.objects.all().delete()
            models.TelephoneReference.objects.all().delete()
            models.Category.objects.all().delete()
            models.BusinessEntity.objects.all().delete()
            models.WorkingHours.objects.all().delete()
            models.RatingAndComment.objects.all().delete()

        User.objects.create_superuser(username='superuser',email='admin@example.com',password='superuser', first_name="Super", last_name="Mario")
        User.objects.create_user(username='john', email='john@koff.com', password='john', first_name="Ivo", last_name="Čokolino")
        User.objects.create_user(username='andrew', email='andrew@koff.com', password='andrew', first_name="Andrija", last_name="Mesarić")
        User.objects.create_user(username='tim', email='tim@koff.com', password='tim', first_name="Tim", last_name="Evidentić")
        User.objects.create_user(username='mark', email='mark@koff.com', password='mark', first_name="Marko", last_name="Veličanstveni")
        User.objects.create_user(username='mile', email='mile@koff.com', password='mile', first_name="Mile", last_name="Miletić")
        User.objects.create_user(username='dino', email='dino@koff.com', password='dino', first_name="Dino", last_name="Obersnel")

        models.TelephoneReference.objects.create(name="Tel")
        models.TelephoneReference.objects.create(name="Mob")
        models.TelephoneReference.objects.create(name="Fax")

        models.Category.objects.create(name="Auto moto i nautika", image="category_images/auspuh.gif")
        models.Category.objects.create(name="Gradnja")
        models.Category.objects.create(name="Dom i ured")
        models.Category.objects.create(name="Računala i telekomunikacije")
        models.Category.objects.create(name="Prijevoz")
        models.Category.objects.create(name="Lorem")
        models.Category.objects.create(name="Ipsum")
        models.Category.objects.create(name="Dolor Sit Amet")
        models.Category.objects.create(name="Elit")
        models.Category.objects.create(name="Lorem Ipsum Dolor")

        categories = models.Category.objects.all()

        models.Category.objects.create(name="Auspuh, Auto staklo, Auto plin", parent=categories[0])
        models.Category.objects.create(name="Auto dijelovi", parent=categories[0])
        models.Category.objects.create(name="Auto elektrika, alarm, audio-oprema", parent=categories[0])
        models.Category.objects.create(name="Auto klima", parent=categories[0])
        models.Category.objects.create(name="Automehaničar", parent=categories[0])
        models.Category.objects.create(name="Auto otpad", parent=categories[0])
        models.Category.objects.create(name="Autopraonica", parent=categories[0])

        models.Category.objects.create(name="Alarmni sustavi, video nadzor", parent=categories[1])
        models.Category.objects.create(name="Boje i lakovi", parent=categories[1])
        models.Category.objects.create(name="Čišćenje dimnjaka", parent=categories[1])
        models.Category.objects.create(name="Električar, Elektroinstalacije, Elektro servis", parent=categories[1])
        models.Category.objects.create(name="Podne obloge", parent=categories[1])

        models.Category.objects.create(name="Audio servis, video servis, TV servis", parent=categories[2])
        models.Category.objects.create(name="Brava, ključ - izrada, ugradnja, servis", parent=categories[2])
        models.Category.objects.create(name="Čišćenje, dezinfekcija, dezinsekcija, deratizacija", parent=categories[2])
        models.Category.objects.create(name="Električar, Elektroinstalacije, Elektro servis", parent=categories[2])
        models.Category.objects.create(name="Servis kućanskih aparata", parent=categories[2])

        models.Category.objects.create(name="Elektronika - proizvodnja, prodaja, servis", parent=categories[3])
        models.Category.objects.create(name="Servis mobitela", parent=categories[3])
        models.Category.objects.create(name="Servis računala, servis kompjutera", parent=categories[3])

        models.Category.objects.create(name="Autobusni prijevoz", parent=categories[4])
        models.Category.objects.create(name="Pomoć za selidbu", parent=categories[4])
        models.Category.objects.create(name="Taxi prijevoz", parent=categories[4])

        gmaps = googlemaps.Client(key=***REMOVED***)

        current_address = 'Tometići, 51215, Kastav'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="TONI AUSPUH",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['toni@mail.hr', 'toni2@mail.hr'],
            web_site=['toni.hr', 'toni2.hr'],
            description=
            """Ja sam *TONI AUSPUH*, vodeći popravljač ~~auspuha~~ ispušnih cijevi. Popravljam sljedeće:
- auspuhe
- ispušne cijevi
- vodiče otpadnih plinova iz automobila
- može i skuter, a i podmornica ako ima auspuh"""
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Minakovo 27, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="BRTAN DARKO - SERVIS",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['darko@mail.hr'],
            web_site=['darko.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Ulica dr. Zdravka Kučića 50, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="BOLJI d.o.o.",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['bolji@mail.hr'],
            web_site=['bolji.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Heinzelova ul. 74, 10000, Zagreb'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="Auspuh M.K.",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['mk@mail.hr'],
            web_site=['mk.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Istarska ul. 92, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="Car Service Bivio",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['bivio@mail.hr'],
            web_site=['bivio.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Ul. Ante Mandića 37, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="AUTOMEHANIČAR TIHOMIR VESIĆ MLAĐI I SINOVI",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['tihomir@mail.hr'],
            web_site=['tihomir.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Ul. Milice Jadranić 7B, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="Autoservis Gordan",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['gordan@mail.hr'],
            web_site=['gordan.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Selinari 6, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="Motorsport Đumić",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['dumic@mail.hr'],
            web_site=['dumic.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        current_address = 'Ul. Tome Strižića 12A, 51000, Rijeka'
        geocode_result = gmaps.geocode(current_address)
        loc_coords = geocode_result[0]['geometry']['location']

        business = models.BusinessEntity.objects.create(
            name="Automotive Center Glavan",
            address=current_address,
            location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
            e_mail=['glavan@mail.hr'],
            web_site=['glavan.hr']
        )
        business.tags.add('auspuh', 'auto')

        category = models.Category.objects.filter(name="Auspuh, Auto staklo, Auto plin")[0]
        models.EntityCategories.objects.create(
            entity=business,
            category=category
        )

        businesses = models.BusinessEntity.objects.all()

        models.WorkingHours.objects.create(name=models.WorkingHours.Mon, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[0])
        models.WorkingHours.objects.create(name=models.WorkingHours.Tue, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[0])
        models.WorkingHours.objects.create(name=models.WorkingHours.Wed, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[0])
        models.WorkingHours.objects.create(name=models.WorkingHours.Thu, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[0])
        models.WorkingHours.objects.create(name=models.WorkingHours.Fri, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[0])
        models.WorkingHours.objects.create(name=models.WorkingHours.Sat, start_time=datetime.time(8, 0), end_time=datetime.time(13, 0), business_entity=businesses[0])
        #models.WorkingHours.objects.create(name=models.WorkingHours.Sun, start_time=datetime.time(8, 0), end_time=datetime.time(13, 0), business_entity=businesses[0]) NE RADI NED

        models.WorkingHours.objects.create(name=models.WorkingHours.Mon, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[1])
        models.WorkingHours.objects.create(name=models.WorkingHours.Tue, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[1])
        models.WorkingHours.objects.create(name=models.WorkingHours.Wed, start_time=datetime.time(8, 0), end_time=datetime.time(20, 0), business_entity=businesses[1])
        models.WorkingHours.objects.create(name=models.WorkingHours.Thu, start_time=datetime.time(8, 0), end_time=datetime.time(21, 0), business_entity=businesses[1])
        models.WorkingHours.objects.create(name=models.WorkingHours.Fri, start_time=datetime.time(8, 0), end_time=datetime.time(21, 0), business_entity=businesses[1])
        models.WorkingHours.objects.create(name=models.WorkingHours.Sat, start_time=datetime.time(8, 0), end_time=datetime.time(13, 0), business_entity=businesses[1])

        users = User.objects.all()

        models.RatingAndComment.objects.create(user=users[0], entity=businesses[0], rating=2, comment="Super biznis!")
        models.RatingAndComment.objects.create(user=users[1], entity=businesses[0], rating=3, comment="Nije loše! Mada, moglo bi to i puno bolje.")
        models.RatingAndComment.objects.create(user=users[2], entity=businesses[0], rating=2, comment="Očajna tvrtka, loša usluga. Dobio sam samo dva bombona iz zdjelice, a ne četiri kao kod Stipeta.")
        models.RatingAndComment.objects.create(user=users[3], entity=businesses[0], rating=3, comment="Šteta, šteta što ne prodaju i burek.")
        models.RatingAndComment.objects.create(user=users[4], entity=businesses[0], rating=5, comment="Nevio")
        models.RatingAndComment.objects.create(user=users[5], entity=businesses[0], rating=1, comment="Stvar je u tome da, ako netko ima auspuh, vrlo vjerojatno će ga morati jednog dana i popraviti. Eh sada, kome se obratiti za takvo nešto? Kako biti siguran da će auspuh biti dobro popravljen, a ne loše? E pa, ako želite dobro popravljeni auspuh, javite se ovom čovjeku!")

        models.RatingAndComment.objects.create(user=users[0], entity=businesses[1], rating=2)
        models.RatingAndComment.objects.create(user=users[1], entity=businesses[1], rating=1)
        models.RatingAndComment.objects.create(user=users[2], entity=businesses[1], rating=2)
        models.RatingAndComment.objects.create(user=users[3], entity=businesses[1], rating=1)

        models.RatingAndComment.objects.create(user=users[0], entity=businesses[2], rating=5)
        models.RatingAndComment.objects.create(user=users[1], entity=businesses[2], rating=4)
        models.RatingAndComment.objects.create(user=users[2], entity=businesses[2], rating=5)
        models.RatingAndComment.objects.create(user=users[3], entity=businesses[2], rating=4)

        models.RatingAndComment.objects.create(user=users[0], entity=businesses[3], rating=1)
        models.RatingAndComment.objects.create(user=users[1], entity=businesses[3], rating=2)
        models.RatingAndComment.objects.create(user=users[2], entity=businesses[3], rating=3)
        models.RatingAndComment.objects.create(user=users[3], entity=businesses[3], rating=4)
        

        
        
