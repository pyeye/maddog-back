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
from django.conf import settings
from rest_framework import routers

from apps.events.views import EventViewSet
from apps.menu.views import MenuViewSet, SetViewSet, CategoryAPIView
from apps.gallery.views import GalleryAPIView, AlbumAPIView
from apps.reservation.views import ReservationAPIView
from apps.feedback.views import FeedbackAPIView


router = routers.SimpleRouter()
router.register(r'events', EventViewSet, base_name='api-events')
router.register(r'menu', MenuViewSet, base_name='api-menu')
router.register(r'sets', SetViewSet, base_name='api-set')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/admin/', admin.site.urls),
    url(r'^api/v1/reservation/', ReservationAPIView.as_view()),
    url(r'^api/v1/feedback/', FeedbackAPIView.as_view()),
    url(r'^api/v1/albums/(?P<pk>\d+)', AlbumAPIView.as_view()),
    url(r'^api/v1/albums/', GalleryAPIView.as_view()),
    url(r'^api/v1/category/menu/', CategoryAPIView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^api/v1/__debug__/', include(debug_toolbar.urls)),
    ]
