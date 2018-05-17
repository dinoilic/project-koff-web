from haystack import indexes
from .models import BusinessEntity


class BusinessEntityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    id = indexes.IntegerField(model_attr='id')
    name = indexes.CharField(model_attr='name')
    description = indexes.NgramField(model_attr='description', null=True)

    def get_model(self):
        return BusinessEntity

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
