"""astro_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view

from facilities import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^schema/$', get_schema_view(title="Astrosat NASA Facilities API", permission_classes=[ AllowAny ])),

    url(r'^facilities/$', views.FacilitiesList.as_view()),
    url(r'^facilities/(?P<pk>[0-9]+)/$', views.FacilitiesDetail.as_view()),
]
