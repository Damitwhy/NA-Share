from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('share/<int:share_id>/comment/', views.comment, name='comment'),
    path('share/new/', views.create_share, name='create_share'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    # Add more URL patterns here
]