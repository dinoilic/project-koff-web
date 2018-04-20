from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

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

    # dodati Filer za sliku BusinessEntityja (paziti, zbog nekog razloga
    # instalira Django 1.11!!)
    # dodati location
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
        verbose_name=_('Business Entity address'),
    )

    e_mail = ArrayField(
            models.EmailField(max_length=50, blank=True),
    )

    web_site = ArrayField(
            models.URLField(max_length=200),
    )

    telephone_references = models.ManyToManyField(
        'TelephoneReference',
        through='EntityTelephoneReference',
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

    DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
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
class Rating(models.Model):

    user = models.OneToOneField(
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

    rating = models.IntegerField(default=5, choices=RATINGS)


@python_2_unicode_compatible
class Comment(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    entity = models.ForeignKey(
        'BusinessEntity',
        on_delete=models.CASCADE
    )

    comment = models.CharField(
        max_length=50,
        verbose_name=_('Comment for the entity'),
    )

# All references


class TelephoneReference(models.Model):

    name = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.name


class SocialReference(models.Model):

    name = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.name


class EntityTelephoneReference(models.Model):

    reference = models.ForeignKey(
        'TelephoneReference',
        on_delete=models.CASCADE
    )
    entity = models.ForeignKey(
        'BusinessEntity',
        on_delete=models.CASCADE
    )
    # mozda dodati validator da je broj zapravo
    number = models.CharField(
        max_length=20
    )

    def __unicode__(self):
        return u"%s - %s" % (self.member, self.reference)


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
