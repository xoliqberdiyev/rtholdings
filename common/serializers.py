from rest_framework import serializers

from common import models


class NumberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactPhoneNumber
        fields = [
            'phone_number',
        ]

class SettingsSerializer(serializers.ModelSerializer):
    phone_numbers = serializers.SerializerMethodField(method_name='get_phone_numbers')

    class Meta:
        model = models.Settings
        fields = [
            'id', 'email', 'phone_numbers',
            'instagram_link', 'telegram_link', 'facebook_link', 'youtube_link'
        ]

    def get_phone_numbers(self, obj):
        numbers = models.ContactPhoneNumber.objects.filter(settings=obj)
        return NumberListSerializer(numbers, many=True).data


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = [
            'id', 'title_uz', 'title_en', 'title_ru', 'title_ko',
            'description_uz', 'description_en', 'description_ru', 'description_ko', 'banner',
        ]


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = [
            'id', 'title_uz', 'title_en', 'title_ru', 'title_ko',
            'description_uz', 'description_en', 'description_ru', 'description_ko', 'image',
        ]

class ProjectServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = [
            'id', 'title_uz', 'title_en', 'title_ru', 'title_ko',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            'id', 'name', 'image', 'link', 'service'
        ]


class ProjectBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectBanner
        fields = [
            'id', 'banner', 'title_uz', 'title_en', 'title_ru', 'title_ko',
            'description_uz', 'description_en', 'description_ru', 'description_ko',
        ]


class ProjectDetailSerializer(serializers.ModelSerializer):
    banner = serializers.SerializerMethodField(method_name='get_banner')

    class Meta:
        model = models.Project
        fields = [
            'id', 'name_uz', 'name_en', 'name_ru', 'name_ko', 'image', 'link', 'service', 'banner'
        ]

    def get_banner(self, obj):
        banner = models.ProjectBanner.objects.get(project=obj)
        if banner:
            return ProjectBannerSerializer(banner).data
        return None

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = [
            'id', 'title_uz', 'title_en', 'title_ru', 'title_ko',
            'description_uz', 'description_en', 'description_ru', 'description_ko', 'image',
        ]


class CustomerFeedbackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerFeedback
        fields = [
            'id', 'user_full_name_uz','user_full_name_en','user_full_name_ru', 'user_full_name_ko',
            'user_feedback_uz', 'user_feedback_en', 'user_feedback_ru', 'user_feedback_ko',
            'user_role_uz', 'user_role_en', 'user_role_ru','user_role_ko',
            'user_image', 'rate',
        ]


class UserContactApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactApplication
        fields = [
            'name', 'email', 'phone_number', 'service', 'text'
        ]


class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMedia
        fields = ['id', 'image',]


class ProductListSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(method_name='get_images')

    class Meta:
        model = models.Product
        fields = [
            'id', 'name_uz', 'name_en', 'name_ru', 'name_ko',
            'description_uz', 'description_en', 'description_ru', 'description_ko',
            'main_image', 'images'
        ]

    def get_images(self, obj):
        images = models.ProductMedia.objects.filter(product=obj)
        return ProductMediaSerializer(images, many=True).data


class OurInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurInfo
        fields = [
            'id', 'banner', 'image1', 'image2', 'image3',
            'title_uz', 'title_en', 'title_ru', 'title_ko',
            'text_uz', 'text_en', 'text_ru', 'text_ko',
        ]


class InfoCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InfoCompany
        fields = [
            'id', 'image', 'project_count', 'customers_count', 'grateful_customers_count',
            'title_uz', 'title_en', 'title_ru', 'title_ko',
            'description_uz', 'description_en', 'description_ru', 'description_ko',
        ]
