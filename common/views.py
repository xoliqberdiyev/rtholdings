from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, views
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from common import models, serializers, filters, throtling


class SettingsApiView(views.APIView):
    def get(self, request):
        settings = models.Settings.objects.only('id', 'email', 'instagram_link', 'telegram_link', 'facebook_link','youtube_link').first()
        serializer = serializers.SettingsSerializer(settings)
        return Response(serializer.data)


class BannerListApiView(views.APIView):
    def get(self, request):
        banners = models.Banner.objects.only('id', 'title', 'description', 'banner', 'type')
        serializer = serializers.BannerListSerializer(banners, many=True)
        return Response(serializer.data)


class ServiceListApiView(views.APIView):
    def get(self, request):
        services = models.Service.objects.only('id', 'title', 'description', 'image')
        serializer = serializers.ServiceListSerializer(services, many=True)
        return Response(serializer.data)


class ServiceDetailApiView(views.APIView):
    def get(self, request, pk):
        try:
            service = models.Service.objects.get(pk=pk)
        except models.Service.DoesNotExist:
            return Response('Service not found')
        projects = models.Project.objects.only('id', 'name', 'image', 'link', 'service').filter(service=service)
        data = {
            'id': service.id,
            'title': service.title,
            'description': service.description,
            'image': service.image.url,
            'projects': serializers.ProjectSerializer(projects, many=True).data
        }
        return Response(data)


class ProjectCategoryListApiView(views.APIView):
    def get(self, request):
        categories = models.Service.objects.only('title', 'id')
        serializer = serializers.ProjectServiceListSerializer(categories, many=True)
        return Response(serializer.data)


class ProjectListApiView(views.APIView):
    def get(self, request):
        projects = models.Project.objects.only('id', 'name', 'image', 'link', 'service')
        serializer = serializers.ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailApiView(views.APIView):
    def get(self, request, pk):
        project = models.Project.objects.get(pk=pk)
        serializer = serializers.ProjectDetailSerializer(project)
        return Response(serializer.data)


class NewsListApiView(views.APIView):
    def get(self, request):
        news = models.News.objects.only('id', 'title', 'description', 'image')
        serializer = serializers.NewsSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailApiView(views.APIView):
    def get(self, request, pk):
        news = models.News.objects.get(pk=pk)
        serializer = serializers.NewsSerializer(news)
        return Response(serializer.data)


class CustomerFeedbackListApiView(views.APIView):
    def get(self, request):
        feedbacks = models.CustomerFeedback.objects.all()
        serializer = serializers.CustomerFeedbackListSerializer(feedbacks, many=True)
        return Response(serializer.data)


class ContactUsCreateApiView(generics.CreateAPIView):
    queryset = models.UserContactApplication
    serializer_class = serializers.UserContactApplicationCreateSerializer
    parser_classes = (MultiPartParser, FormParser)
    throttle_classes = [
        throtling.CreateUserContactApplicationIPThrottle,
        throtling.CreateUserContactApplicationPhoneThrottle,
    ]


class ProductListApiView(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ProductFilter
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    pagination_class = PageNumberPagination
    page_size = 12


class OurInfoApiView(generics.GenericAPIView):
    serializer_class = serializers.OurInfoSerializer
    def get(self, request):
        info = models.OurInfo.objects.all().first()
        serializer = serializers.OurInfoSerializer(info)
        return Response(serializer.data)


class InfoCompanyApiView(generics.GenericAPIView):
    serializer_class = serializers.InfoCompanySerializer
    def get(self, request):
        info = models.InfoCompany.objects.all().first()
        serializer = serializers.InfoCompanySerializer(info)
        return Response(serializer.data)