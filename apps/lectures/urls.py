from django.urls import path, include
from rest_framework import routers
from .views import LectureViewSet

router = routers.DefaultRouter()
router.register(r'', LectureViewSet)
# app_name = "apps.users.urls"
urlpatterns = [
    path('', include(router.urls)),
]