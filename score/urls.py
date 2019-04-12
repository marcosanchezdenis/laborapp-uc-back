from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.urls import include


from score.views import *



router = DefaultRouter()
router.register(r'skill',SkillViewSet ,base_name='Skill')
router.register(r'scoresystem', ScoreSystemViewSet ,base_name='ScoreSystem')
router.register(r'scoresystemvalue', ScoreSystemValueViewSet ,base_name='ScoreSystemValue')

urlpatterns = [
    
    
    url(r'^', include(router.urls) ),
    
]