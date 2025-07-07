from modeltranslation.translator import TranslationOptions, register

from common import models


@register(models.ServiceType)
class ServiceTypeTranslation(TranslationOptions):
    fields = ['title', 'description']



@register(models.Service)
class ServiceTranslation(TranslationOptions):
    fields = ['title', 'description']


@register(models.News)
class NewsTranslation(TranslationOptions):
    fields = ['title', 'description']


@register(models.Feedback)
class FeedbackTranslation(TranslationOptions):
    fields = ['comment', 'position']


@register(models.Product)
class ProductTranslation(TranslationOptions):
    fields = ['name', 'model', 'color', 'fuel_type', 'location']