from unicodedata import name
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'monster', views.MonsterViewSet, basename="monster")
router.register(r'monster-hzv', views.MonsterHZVViewSet, basename="monster-hzv")

app_name = 'monster'
urlpatterns = [
    path('monsterdata/', include(router.urls)),
    path('', views.monster_list, name='monsters'),
]

