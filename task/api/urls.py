from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, ClientViewset, ProjectViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user1", UserViewSet)
router.register(r"clients", ClientViewset)
router.register(r"project", ProjectViewset)


urlpatterns = [
    path('', include(router.urls))

]