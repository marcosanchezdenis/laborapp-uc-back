from django.urls import path,include
from django.conf.urls import url
from network.views import *

from rest_framework.routers import DefaultRouter





""" 
router = DefaultRouter()
router.register(r'user/create', UserCreateAPIView.as_view())
router.register(r'city', CityViewSet)
router.register(r'contacttype',ContactTypeViewSet) """
























urlpatterns = [
    
    

    url(r'^user/create$', UserCreateAPIView.as_view(),name="register"),
    url(r'^user/login$', UserLoginAPIView.as_view(),name="login"),
    url(r'^user/logout$', LogoutView.as_view(),name="logout"),
    url(r'^user/info$', UserInfoView.as_view(),name="user"),
    
]