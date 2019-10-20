"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
#from oscar.apps.search.views import SearchAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('accounts/login', include('social_django.urls', namespace='social')),
    #re_path(r'^autocomplete/', SearchAutocomplete, name='autocomplete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
