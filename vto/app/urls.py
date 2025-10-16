from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('industries/', views.industries, name='industries'),
    path('offer/', views.offer, name='offer'),
    path('quality/', views.quality, name='quality'),
    path('choose/', views.choose, name='choose')
]