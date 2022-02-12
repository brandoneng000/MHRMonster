from unicodedata import name
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'monster', views.MonsterViewSet, basename="monster")

app_name = 'monster'
urlpatterns = [
    path('monsterdata/', include(router.urls)),
    # path('monster-hzv/<int:pk>', views.monster_hzv),
    path('monster-hzv/', views.MonsterHZVs.as_view()),
    path('', views.monster_list, name='monsters'),
    path('<int:pk>', views.monster_detail, name='monsters-detail'),
]
