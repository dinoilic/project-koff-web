from django.contrib import admin
from .models import Category
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
