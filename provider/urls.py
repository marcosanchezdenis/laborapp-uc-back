from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.urls import include
from provider.views import *



router = DefaultRouter()
router.register(r'provider',ProviderViewSet)
router.register(r'providerdata',ProviderDataViewSet)
router.register(r'problem',ProblemViewSet)
router.register(r'service',ServiceViewSet)



urlpatterns = [
    
    
    url(r'^', include(router.urls) ),
    
]