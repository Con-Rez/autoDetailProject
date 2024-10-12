from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path('about/', views.aboutView, name='about'),
    path('gallery/', views.galleryView, name='gallery'),
    path('schedule_appointment/', views.scheduleView, name='schedule_appointment'),
]