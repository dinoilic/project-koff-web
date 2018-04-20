from django.core.management.base import BaseCommand
from django.conf import settings
from project_koff_web.koff import models
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Removes old data and populates database with new test data'

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.exists() or \
            models.Category.objects.exists():

            User.objects.all().delete()
            models.Category.objects.all().delete()

        User.objects.create_superuser(
            'superuser',
            'admin@example.com',
            'superuser'
        )

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
