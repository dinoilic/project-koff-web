from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from treebeard.mp_tree import MP_Node


@python_2_unicode_compatible
class Category(MP_Node):
    active = models.BooleanField(
        verbose_name=_('Active'),
        help_text=_('This field is used to determine if a '
                    'category is active.'),
        default=True
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_('Category name'),
        help_text=_('This field is used for naming the category.')
    )

    node_order_by = ['name']

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
