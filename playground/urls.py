from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello, name='blog-home'),
    path('about/', views.about_page, name='blog-about')
]
