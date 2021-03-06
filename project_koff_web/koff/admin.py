# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)


class BusinessEntityAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'active', 'address', 'location', 'e_mail', 'web_site', 'telephone_numbers',)
    list_filter = ('active',)
    raw_id_fields = ('social_references', 'tags', 'categories',)
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


class RatingAndCommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'entity', 'rating')
    list_filter = ('user', 'entity')


class SocialReferenceAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class EntitySocialReferenceAdmin(admin.ModelAdmin):

    list_display = ('id', 'reference', 'entity', 'link')
    list_filter = ('reference', 'entity')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.BusinessEntity, BusinessEntityAdmin)
_register(models.EntityCategories, EntityCategoriesAdmin)
_register(models.WorkingHours, WorkingHoursAdmin)
_register(models.RatingAndComment, RatingAndCommentAdmin)
_register(models.SocialReference, SocialReferenceAdmin)
_register(models.EntitySocialReference, EntitySocialReferenceAdmin)
