from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path('gallery/', views.galleryView, name='gallery'),
    path('schedule_appointment/', views.scheduleView, name='schedule_appointment'),
    path('contact_us/', views.ContactUsView, name='contact_us'),
    path('about_us/', views.aboutUsView, name='about_us'),
    # help code customer contact/continue
    path('submit_form/', views.submit_form, name='submit_form'),
]