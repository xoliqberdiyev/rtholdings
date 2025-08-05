import django_filters

from common.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        fields = [
            'name_uz', 'name_ru', 'name_en','name_ko'
        ]