from django.urls import path

from common.api_v1 import views

urlpatterns = [
    path('our_activity_number/list/', views.OurActivityNumberListApiView.as_view()),
    path('service_type/list/', views.ServiceTypeListApiView.as_view()),
    path('news/list/', views.NewsListApiView.as_view()),
    path('feedback/list/', views.FeedbackListApiView.as_view()),
    path('contact_us/', views.ContactUsCreateApiView.as_view()),
    path('product/list/', views.ProductListApiView.as_view()),
]