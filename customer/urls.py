from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from customer.views import *
from django.urls import path

router = DefaultRouter()
router.register(r'customer',CustomerViewSet)
router.register(r'customerdata',CustomerDataViewSet)
router.register(r'testuser',UserViewSet)
#router.register(r'provider',ProviderSearch.as_view())



urlpatterns = [
    
    

    path('provider', ProviderSearch.as_view())
    
]