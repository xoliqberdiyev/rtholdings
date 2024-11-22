from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from modeltranslation.admin import TranslationStackedInline

from common import models

admin.site.unregister(Group)

class ProjectBannerInline(TranslationStackedInline):
    model = models.ProjectBanner
    extra = 0


    def has_add_permission(self, request, obj=None):
        try:
            models.ProjectBanner.objects.get(project=obj)
            return False
        except models.ProjectBanner.DoesNotExist:
            return True


class ContactPhoneInline(admin.StackedInline):
    model = models.ContactPhoneNumber
    extra = 0


@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    inlines = [ContactPhoneInline]


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("banner", "type")}),
        (_("Uzbek tilida"), {"fields": ("title_uz", "description_uz")}),
        (_("Ingliz tilida"), {"fields": ("title_en", "description_en")}),
        (_("Rus tilida"), {"fields": ("title_ru", "description_ru")}),
        (_("Kores tilida"), {"fields": ("title_ko", "description_ko")}),
    )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image',)}),
        (_("Uzbek tilida"), {"fields": ("title_uz", 'description_uz')}),
        (_("Ingliz tilida"), {"fields": ("title_en", 'description_en')}),
        (_("Rus tilida"), {"fields": ("title_ru", 'description_ru')}),
        (_("Kores tilida"), {"fields": ("title_ko", 'description_ko')}),
    )


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectBannerInline]
    fieldsets = (
        (None, {'fields': ('image', 'service', 'link')}),
        (_("Uzbek tilida"), {"fields": ("name_uz", 'description_uz')}),
        (_("Ingliz tilida"), {"fields": ("name_en", 'description_en')}),
        (_("Rus tilida"), {"fields": ("name_ru", 'description_ru')}),
        (_("Kores tilida"), {"fields": ("name_ko", 'description_ko')}),
    )


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ('image',)}),
        (_("Uzbek tilida"), {"fields": ("title_uz", 'description_uz')}),
        (_("Ingliz tilida"), {"fields": ("title_en", 'description_en')}),
        (_("Rus tilida"), {"fields": ("title_ru", 'description_ru')}),
        (_("Kores tilida"), {"fields": ("title_ko", 'description_ko')}),
    )

@admin.register(models.CustomerFeedback)
class CustomerFeedbackAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ('image',)}),
        (_("Uzbek tilida"), {"fields": ("user_role_uz", 'user_full_name_uz', 'user_feedback_uz')}),
        (_("Ingliz tilida"), {"fields": ("user_role_en", 'user_full_name_en', 'user_feedbakc_en')}),
        (_("Rus tilida"), {"fields": ("user_role_ru", 'user_full_name_ru')}),
        (_("Kores tilida"), {"fields": ("user_role_ko", 'user_full_name_ko', 'user_feedback_ko')}),
    )


@admin.register(models.UserContactApplication)
class UserContactApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'is_contacted']
    list_filter = ['is_contacted']
    ordering = ['is_contacted']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProductMediaInline(admin.StackedInline):
    model = models.ProductMedia
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('main_image',)}),
        (_("Uzbek tilida"), {'fields': ('name_uz', 'description_uz')}),
        (_("Ingliz tilida"), {'fields': ('name_en', 'description_en')}),
        (_("Rus tilida"), {'fields': ('name_ru', 'description_ru')}),
        (_("Kores tilida"), {'fields': ('name_ko', 'description_ko')}),
    )
    inlines = [ProductMediaInline]
    list_display = ['id', 'name']
    list_display_links = list_display


@admin.register(models.OurInfo)
class OurInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('banner', 'image1', 'image2', 'image3')}),
        (_("Uzbek tilida"), {'fields': ('title_uz', 'text_uz')}),
        (_("Ingliz tilida"), {'fields': ('title_en', 'text_en')}),
        (_("Rus tilida"), {'fields': ('title_ru', 'text_ru')}),
        (_("Kores tilida"), {'fields': ('title_ko', 'text_ko')}),
    )


@admin.register(models.InfoCompany)
class InfoCompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'project_count', 'customers_count', 'grateful_customers_count')}),
        (_("Uzbek tilida"), {'fields': ('title_uz', 'description_uz')}),
        (_("Ingliz tilida"), {'fields': ('title_en', 'description_en')}),
        (_("Rus tilida"), {'fields': ('title_ru', 'description_ru')}),
        (_("Kores tilida"), {'fields': ('title_ko', 'description_ko')}),
    )


