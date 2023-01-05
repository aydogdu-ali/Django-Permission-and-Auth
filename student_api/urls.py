from django.urls import path, include
from rest_framework import routers
from .views import (
   
    home,
    StudentMVS,
    PathMVS
)

router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)


urlpatterns = [
  
    path("", home),
    path("", include(router.urls))
]

