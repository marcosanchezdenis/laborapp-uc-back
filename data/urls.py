from rest_framework.routers import DefaultRouter
from data.views import *
from django.conf.urls import url 
from django.urls import include


router = DefaultRouter()
router.register(r'property', PropertyViewSet)
router.register(r'propertytype',PropertyTypeViewSet)


urlpatterns = [
    
    
    url(r'^', include(router.urls) ),
    
]