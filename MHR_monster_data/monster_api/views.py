from django.shortcuts import render
from rest_framework import viewsets
import requests

from .serializers import MonsterHZVSerializer, MonsterSerializer
from .models import Monster, Monster_HZV

# Create your views here.
class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all().order_by('id')
    serializer_class = MonsterSerializer


class MonsterHZVViewSet(viewsets.ModelViewSet):
    queryset = Monster_HZV.objects.all().order_by('part_id')
    serializer_class = MonsterHZVSerializer

def monster_list(request):
    response = requests.get('http://127.0.0.1:8000/monsterdata/monster/')
    
    monsters = response.json()
    print(len(monsters))
    print("\n\n\n\n")

    return render(request, "home.html", {'monsters': monsters})
