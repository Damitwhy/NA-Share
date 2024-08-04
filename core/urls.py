from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('share/<int:share_id>/comment/', views.comment, name='comment'),
    path('share/new/', views.create_share, name='create_share'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('stories/<int:share_id>/', views.stories_detail, name='stories_detail'),
    # Add more URL patterns here
]