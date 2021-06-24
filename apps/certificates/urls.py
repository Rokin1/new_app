from django.urls import path, include
from rest_framework import routers
from .views import CertificateViewSet

router = routers.DefaultRouter()
router.register(r'', CertificateViewSet)
# app_name = "apps.users.urls"
urlpatterns = [
    path('', include(router.urls)),
]