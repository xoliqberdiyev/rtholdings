from django.contrib import admin 
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from modeltranslation.admin import TranslationAdmin

from common import models

admin.site.unregister(Group)


class NewsImageInline(admin.TabularInline):
    extra = 0
    model = models.NewsImage
    fields = ['image']


class ProductImageInline(admin.TabularInline):
    extra = 0
    model = models.ProductImage
    fields = ['image']


@admin.register(models.OurActivityNumber)
class OurActivityNumberAdmin(TranslationAdmin):
    list_display = ['id', 'number', 'title']


@admin.register(models.ServiceType)
class ServiceTypeAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'description']
    fieldsets = (
        (None, {"fields": ("image", 'banner')},),
        (("English"), {"fields": ("title_en", "description_en")},),
        (("Russian"), {"fields": ("title_ru", "description_ru")},),
        (("Uzbek"), {"fields": ("title_uz", "description_uz")},),
        (("Korean"), {"fields": ("title_ko", "description_ko")},),
        (("Links"), {"fields": (
            "instagram_link",
            "telegram_link", 
            "youtube_link", 
            "whatsup_link", 
            "tiktok_link", 
            'facebook_link',
            'phone_number',
            'website_link', 
            'email_link',
        )})
    )


@admin.register(models.Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'description']
    fieldsets = (
        (None, {"fields": ("type",)},),
        (("English"), {"fields": ("title_en", "description_en")},),
        (("Russian"), {"fields": ("title_ru", "description_ru")},),
        (("Uzbek"), {"fields": ("title_uz", "description_uz")},),
        (("Korean"), {"fields": ("title_ko", "description_ko")},),
    )

@admin.register(models.News)
class NewsAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'description']
    fieldsets = (
        (("English"), {"fields": ("title_en", "description_en")},),
        (("Russian"), {"fields": ("title_ru", "description_ru")},),
        (("Uzbek"), {"fields": ("title_uz", "description_uz")},),
        (("Korean"), {"fields": ("title_ko", "description_ko")},),
    )
    inlines = [NewsImageInline]


@admin.register(models.Feedback)
class FeedbackAdmin(TranslationAdmin):
    list_display = ['id', 'full_name', 'rate']

    fieldsets = (
        (None, {'fields': ('image', 'full_name', 'rate')},),
        (("English"), {"fields": ("comment_en", "position_en")},),
        (("Russian"), {"fields": ("comment_ru", "position_ru")},),
        (("Uzbek"), {"fields": ("comment_uz", "position_uz")},),
        (("Korean"), {"fields": ("comment_ko", "position_ko")},),
    )

@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'email', 'is_contacted']


@admin.register(models.Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name_en', 'year', 'price']
    
    fieldsets = (
        (None, {'fields': ('year', 'price', 'distance')},),
        (("English"), {"fields": ("name_en", "model_en", "color_en", "fuel_type_en", "location_en")},),
        (("Russian"), {"fields": ("name_ru", "model_ru", "color_ru", "fuel_type_ru", "location_ru")},),
        (("Uzbek"), {"fields": ("name_uz", "model_uz", "color_uz", "fuel_type_uz", "location_uz")},),
        (("Korean"), {"fields": ("name_ko", "model_ko", "color_ko", "fuel_type_ko", "location_ko")},),
    )
    inlines = [ProductImageInline]