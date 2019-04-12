from rest_framework.routers import DefaultRouter
from serviceRequest.views import *
from django.conf.urls import url
from django.urls import include

router = DefaultRouter()
router.register(r'request',RequestViewSet)
router.register(r'requeststate',RequestStateViewSet)



urlpatterns = [
    
    
    url(r'^', include(router.urls) ),
    
]