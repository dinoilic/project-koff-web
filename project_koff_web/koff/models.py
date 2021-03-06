from django.db import models
from django.contrib.gis.db import models as gismodels
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django.db.models import Avg

from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Category(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name=_('Category name'),
        help_text=_('This field is used for naming the category.')
    )

    icon_name = models.CharField(
        max_length=50,
        verbose_name=_('Icon name'),
        help_text=_('This field is used for picking the icon in app.'),
        null=True,
        blank=True
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,  # SET_NULL
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='category_images/', 
        default='category_images/no_image.jpg'
    )

    def get_children(self):
        return Category.objects.filter(parent=self)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class BusinessEntity(models.Model):

    # dodati image
    name = models.CharField(
        max_length=50,
        verbose_name=_('Business Entity name'),
        help_text=_('This field is used for naming the business entity.')
    )

    active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_('This field is used to determine if a '
            'business entity is active.'),
        default=True
    )

    address = models.CharField(
        max_length=50,
        verbose_name=_('Business Entity address')
    )

    location = gismodels.PointField(
        null=True,
        blank=True,
        default=Point(0, 0),
        verbose_name="Location"
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Description in Markdown"
    )

    e_mail = ArrayField(
        models.EmailField(max_length=50),
        null=True,
        blank=True
    )

    web_site = ArrayField(
        models.URLField(max_length=200),
        null=True,
        blank=True
    )

    telephone_numbers = ArrayField(
        models.CharField(max_length=50),
        null=True,
        blank=True
    )

    social_references = models.ManyToManyField(
        'SocialReference',
        through='EntitySocialReference',
    )

    categories = models.ManyToManyField(
        'Category',
        through='EntityCategories',
    )

    tags = TaggableManager()

    @property
    def rating(self):
        rating = self.ratingandcomment_set.aggregate(Avg('rating'))['rating__avg']
        if rating is None:
            return 0.0
        else:
            return rating

    class Meta:
        verbose_name = _('Business Entity')
        verbose_name_plural = _('Business Entities')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class EntityCategories(models.Model):

    entity = models.ForeignKey(
        'BusinessEntity',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )


@python_2_unicode_compatible
class WorkingHours(models.Model):

    Mon = _('Mon')
    Tue = _('Tue')
    Wed = _('Wed')
    Thu = _('Thu')
    Fri = _('Fri')
    Sat = _('Sat')
    Sun = _('Sun')

    # ne zaboraviti da može i ne raditi određeni dan
    DAYS = (
        (Mon, _('Monday')),
        (Tue, _('Tuesday')),
        (Wed, _('Wednesday')),
        (Thu, _('Thursday')),
        (Fri, _('Friday')),
        (Sat, _('Saturday')),
        (Sun, _('Sunday')),
    )

    name = models.CharField(
        max_length=3,
        verbose_name=_('Short day name'),
        help_text=_('This field is used for short naming the day of the week.'),
        choices=DAYS
    )

    start_time = models.TimeField()
    end_time = models.TimeField()

    business_entity = models.ForeignKey(
        'BusinessEntity',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Working hours')
        verbose_name_plural = _('Working hours')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class RatingAndComment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    entity = models.ForeignKey(
        'BusinessEntity',
        on_delete=models.CASCADE
    )

    RATINGS = (
        (1, 'Very Low'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'High'),
        (5, 'Very High'),
    )

    rating = models.IntegerField(default=5, blank=True, choices=RATINGS)
    comment = models.CharField(
        max_length=500,
        blank=True,
        verbose_name=_('Comment for the entity'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# All references


class SocialReference(models.Model):

    name = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.name


class EntitySocialReference(models.Model):

    reference = models.ForeignKey(
        'SocialReference',
        on_delete=models.CASCADE
    )
    entity = models.ForeignKey(
        'BusinessEntity',
        on_delete=models.CASCADE
    )
    link = models.URLField(
        max_length=200
    )

    def __unicode__(self):
        return u"%s - %s" % (self.member, self.reference)
