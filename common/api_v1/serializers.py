from rest_framework import serializers

from common import models


class OurActivityNumberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurActivityNumber
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'title_ko', 'description_uz', 'description_ru', 'description_en', 'description_ko'
        ]


class ServiceTypeListSerializer(serializers.ModelSerializer):
    services = ServiceListSerializer(many=True)

    class Meta:
        model = models.ServiceType
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'title_ko', 'description_uz', 'description_ru', 'description_en', 'description_ko', 'image', 'services'
        ]


class NewsImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields =[
            'id', 'image'
        ]


class NewsListSerializer(serializers.ModelSerializer):
    news_images = NewsImageListSerializer(many=True)
    
    class Meta:
        model = models.News
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'title_ko', 'description_uz', 'description_ru', 'description_en', 'description_ko', 'news_images'
        ]


class FeedbackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = [
            'id', 'full_name', 'image', 'rate', 'comment_uz', 'comment_ru', 'comment_en', 'comment_ko', 'position_uz', 'position_ru', 'position_en', 'position_ko'
        ]
    

class ContactUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = [
            'full_name', 'phone_number', 'email', 'service_type', 'comment'
        ]


class ProductImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['id', 'image']


class ProductListSerializer(serializers.ModelSerializer):
    product_images = ProductImageListSerializer(many=True)
    
    class Meta:
        model = models.Product
        fields = [
            'id', 'year', 'distance', 'price', 
            'name_uz', 'name_ru', 'name_en', 'name_ko',
            'model_uz', 'model_ru', 'model_en', 'model_ko',
            'color_uz', 'color_ru', 'color_en', 'color_ko',
            'fuel_type_uz', 'fuel_type_ru', 'fuel_type_en', 'fuel_type_ko',
            'location_uz', 'location_ru', 'location_en', 'location_ko',
            'product_images'
        ]