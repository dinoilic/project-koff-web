# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)


class BusinessEntityAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'active', 'address', 'location', 'e_mail', 'web_site')
    list_filter = ('active',)
    raw_id_fields = ('telephone_references', 'social_references', 'tags', 'categories',)
    search_fields = ('name',)


class EntityCategoriesAdmin(admin.ModelAdmin):

    list_display = ('id', 'entity', 'category')
    list_filter = ('entity', 'category')


class WorkingHoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'start_time',
        'end_time',
        'business_entity',
    )
    list_filter = ('business_entity',)
    search_fields = ('name',)


class RatingAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'entity', 'rating')
    list_filter = ('user', 'entity')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'entity', 'comment')
    list_filter = ('user', 'entity')


class TelephoneReferenceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class SocialReferenceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class EntityTelephoneReferenceAdmin(admin.ModelAdmin):

    list_display = ('id', 'reference', 'entity', 'number')
    list_filter = ('reference', 'entity')


class EntitySocialReferenceAdmin(admin.ModelAdmin):

    list_display = ('id', 'reference', 'entity', 'link')
    list_filter = ('reference', 'entity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.BusinessEntity, BusinessEntityAdmin)
_register(models.EntityCategories, EntityCategoriesAdmin)
_register(models.WorkingHours, WorkingHoursAdmin)
_register(models.Rating, RatingAdmin)
_register(models.Comment, CommentAdmin)
_register(models.TelephoneReference, TelephoneReferenceAdmin)
_register(models.SocialReference, SocialReferenceAdmin)
_register(models.EntityTelephoneReference, EntityTelephoneReferenceAdmin)
_register(models.EntitySocialReference, EntitySocialReferenceAdmin)
