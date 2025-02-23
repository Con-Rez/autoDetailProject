"""
URL configuration for autoDetailProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings # This is for serving static files during development
from django.conf.urls.static import static # This is for serving static files during development
from django.urls import include, path # include() function allows referencing other URLconfs within the project
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls), # This is for the admin site
    path('', include('home.urls')), # This is for the home site
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# The above line is for serving static files during development