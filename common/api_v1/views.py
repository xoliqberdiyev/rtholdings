from rest_framework import generics, status

from common.api_v1 import serializers
from common import models


class OurActivityNumberListApiView(generics.ListAPIView):
    pagination_class = None
    serializer_class = serializers.OurActivityNumberListSerializer
    queryset = models.OurActivityNumber.objects.all()


class ServiceTypeListApiView(generics.ListAPIView):
    queryset = models.ServiceType.objects.prefetch_related('services')
    serializer_class = serializers.ServiceTypeListSerializer


class NewsListApiView(generics.ListAPIView):
    queryset = models.News.objects.prefetch_related('news_images')
    serializer_class = serializers.NewsListSerializer


class FeedbackListApiView(generics.ListAPIView):
    pagination_class = None
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackListSerializer


class ContactUsCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.ContactUsCreateSerializer
    queryset = models.ContactUs.objects.all()


class ProductListApiView(generics.ListAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.prefetch_related('product_images')

