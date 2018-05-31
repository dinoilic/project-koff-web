from django.core.management.base import BaseCommand
from project_koff_web.koff import models
from django.contrib.auth import get_user_model
import datetime

import googlemaps  # used for geocoding
from django.contrib.gis.geos import GEOSGeometry
from django.utils import translation

from .raw_data import USERS, CATEGORIES_AND_BUSINESSES


class Command(BaseCommand):
    help = 'Removes old data and populates database with new test data'

    def handle(self, *args, **options):
        translation.activate('hr')
        User = get_user_model()
        gmaps = googlemaps.Client(
            key=***REMOVED***
        )

        # Deleting everything

        if User.objects.exists() or \
            models.Category.objects.exists() or \
            models.BusinessEntity.objects.exists() or \
            models.WorkingHours.objects.exists() or \
            models.RatingAndComment.objects.exists():

            User.objects.all().delete()
            models.Category.objects.all().delete()
            models.BusinessEntity.objects.all().delete()
            models.WorkingHours.objects.all().delete()
            models.RatingAndComment.objects.all().delete()

        # Creating users

        User.objects.create_superuser(
            username='superuser',
            email='admin@example.com',
            password='superuser',
            first_name="Super",
            last_name="Mario"
        )

        for user in USERS:
            User.objects.create_user(
                username=user['username'],
                email=user['email'],
                password=user['password'],
                first_name=user['first_name'],
                last_name=user['last_name']
            )

        # Creating categories

        for category in CATEGORIES_AND_BUSINESSES:
            created_category = models.Category.objects.create(
                name=category['name'],
                image=category['image'],
            )
            for subcategory in category['subcategories']:
                created_subcategory = models.Category.objects.create(
                    name=subcategory['name'],
                    image=subcategory['image'],
                    parent=created_category
                )

                for business in subcategory['businesses']:
                    geocode_result = gmaps.geocode(business['address'])
                    loc_coords = geocode_result[0]['geometry']['location']

                    created_business = models.BusinessEntity.objects.create(
                        name=business['name'],
                        address=business['address'],
                        location=GEOSGeometry('POINT(%f %f)' % (loc_coords['lat'], loc_coords['lng'])),
                        e_mail=business['e_mail'],
                        web_site=business['web_site'],
                        telephone_numbers=business['telephone_numbers'],
                        description=business['description']
                    )

                    # Category
                    models.EntityCategories.objects.create(
                        entity=created_business,
                        category=created_subcategory
                    )

                    # Tags
                    for tag in business['tags']:
                        created_business.tags.add(tag)

                    # Working hours
                    for working_hour in business['working_hours']:
                        models.WorkingHours.objects.create(
                            name=working_hour['name'],
                            start_time=working_hour['start_time'],
                            end_time=working_hour['end_time'],
                            business_entity=created_business
                        )


        categories = models.Category.objects.all()

        businesses = models.BusinessEntity.objects.all()
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
