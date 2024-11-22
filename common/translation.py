from modeltranslation.translator import TranslationOptions, register

from common import models


@register(models.Banner)
class BannerTranslationOptions(TranslationOptions):
    model = models.Banner
    fields = ['title', 'description']


@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    model = models.Service
    fields = ['title', 'description']


@register(models.Project)
class ProjectTranslationOptions(TranslationOptions):
    model = models.Project
    fields = ['name', 'description']


@register(models.ProjectBanner)
class ProjectTranslationOptions(TranslationOptions):
    model = models.Project
    fields = ['title', 'description']


@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    model = models.News
    fields = ['title', 'description']


@register(models.CustomerFeedback)
class CustomerFeedbackTranslationOptions(TranslationOptions):
    model = models.CustomerFeedback
    fields = ['user_role', 'user_full_name', 'user_feedback']

@register(models.Product)
class ProductTranslationOptions(TranslationOptions):
    model = models.Product
    fields = ['name', 'description']


@register(models.OurInfo)
class OurInfoTranslationOptions(TranslationOptions):
    model = models.OurInfo
    fields = ['title', 'text']


@register(models.InfoCompany)
class InfoCompanyTranslationOptions(TranslationOptions):
    model = models.InfoCompany
    fields = ['title', 'description',]

