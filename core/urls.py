"""maddog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from  apps.events.views import EventViewSet
from  apps.menu.views import MenuViewSet
from  apps.gallery.views import ImageViewSet, AlbumViewSet
from  apps.reservation.views import ReservationAPIView


router = routers.SimpleRouter()
router.register(r'events', EventViewSet)
router.register(r'menu', MenuViewSet, base_name='api-menu')
router.register(r'images', ImageViewSet)
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/admin/', admin.site.urls),
    url(r'^api/v1/reservation/', ReservationAPIView.as_view()),
]
