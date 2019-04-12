from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from customer.views import *

router = DefaultRouter()
router.register(r'customer',CustomerViewSet)
router.register(r'customerdata',CustomerDataViewSet)
router.register(r'testuser',UserViewSet)
router.register(r'search',SearchProviderViewSet.as_view())


urlpatterns = [
    
    
    url(r'^', include(router.urls) ),
    
]