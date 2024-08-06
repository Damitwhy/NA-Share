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
    path('share/<int:share_id>/edit/', views.edit_share, name='edit_share'),
    path('share/<int:share_id>/delete/', views.delete_share, name='delete_share'),
    path('share/<int:share_id>/comment/', views.comment, name='add_comment'),
    path('share/<int:share_id>/comment/<int:parent_id>/', views.comment, name='reply_comment'),
    path('share/<int:share_id>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('share/<int:share_id>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    # Remove the old patterns that don't include share_id
    # path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    # path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]