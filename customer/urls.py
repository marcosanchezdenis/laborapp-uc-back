from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from customer.views import *
from django.urls import path

router = DefaultRouter()
router.register(r'customer',CustomerViewSet)
router.register(r'customerdata',CustomerDataViewSet)
router.register(r'testuser',UserViewSet)
#router.register(r'provider',ProviderSearch)



urlpatterns = [
    path('provider-search', ProviderSearch.as_view() ),
    path('provider-profile/<int:pk>/', ProviderProfile.as_view() ),
    path('request-provider/<int:pk>/', RequestProvider.as_view() ),
    path('comment-provider/<int:pk>/', CommentProvider.as_view() ),
    path('my-requests', MyRequests.as_view() ),
    path('request/<int:pk>/', MyRequest.as_view() ),
    path('request-message/<int:pk>/', MyRequestMessages.as_view() ),
    path('request-state', MyRequestState.as_view() )
    
]