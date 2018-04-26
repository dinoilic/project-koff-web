from django.core.management.base import BaseCommand
from project_koff_web.koff import models
from django.contrib.auth import get_user_model
import datetime

import googlemaps  # used for geocoding
from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):
    help = 'Removes old data and populates database with new test data'

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.exists() or \
            models.TelephoneReference.objects.exists() or \
            models.Category.objects.exists() or \
            models.BusinessEntity.objects.exists() or \
            models.WorkingHours.objects.exists() or \
            models.Rating.objects.exists():

            User.objects.all().delete()
            models.TelephoneReference.objects.all().delete()
            models.Category.objects.all().delete()
            models.BusinessEntity.objects.all().delete()
            models.WorkingHours.objects.all().delete()
            models.Rating.objects.all().delete()

        User.objects.create_superuser('superuser','admin@example.com','superuser')
        User.objects.create_user(username='john', email='john@koff.com', password='john')
        User.objects.create_user(username='andrew', email='andrew@koff.com', password='andrew')
        User.objects.create_user(username='tim', email='tim@koff.com', password='tim')
        User.objects.create_user(username='mark', email='mark@koff.com', password='mark')
        User.objects.create_user(username='mile', email='mile@koff.com', password='mile')
        User.objects.create_user(username='dino', email='dino@koff.com', password='dino')

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
            web_site=['toni.hr', 'toni2.hr']
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

        models.Rating.objects.create(user=users[0], entity=businesses[0], rating=2)
        models.Rating.objects.create(user=users[1], entity=businesses[0], rating=3)
        models.Rating.objects.create(user=users[2], entity=businesses[0], rating=2)
        models.Rating.objects.create(user=users[3], entity=businesses[0], rating=3)

        models.Rating.objects.create(user=users[0], entity=businesses[1], rating=2)
        models.Rating.objects.create(user=users[1], entity=businesses[1], rating=1)
        models.Rating.objects.create(user=users[2], entity=businesses[1], rating=2)
        models.Rating.objects.create(user=users[3], entity=businesses[1], rating=1)

        models.Rating.objects.create(user=users[0], entity=businesses[2], rating=5)
        models.Rating.objects.create(user=users[1], entity=businesses[2], rating=4)
        models.Rating.objects.create(user=users[2], entity=businesses[2], rating=5)
        models.Rating.objects.create(user=users[3], entity=businesses[2], rating=4)

        models.Rating.objects.create(user=users[0], entity=businesses[3], rating=1)
        models.Rating.objects.create(user=users[1], entity=businesses[3], rating=2)
        models.Rating.objects.create(user=users[2], entity=businesses[3], rating=3)
        models.Rating.objects.create(user=users[3], entity=businesses[3], rating=4)
        #models.Comment.objects.create(user=users[0], entity=businesses[0], comment="Super biznis!")
