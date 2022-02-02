from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions


from .serializers import MonsterHZVSerializer, MonsterSerializer
from .models import Monster, Monster_HZV
from monster_api.permissions import IsOwnerOrReadOnly

# Create your views here.
class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all().order_by('id')
    serializer_class = MonsterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

class MonsterHZVs(generics.ListAPIView):
    serializer_class = MonsterHZVSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Monster_HZV.objects.all()
            monster = self.request.GET.get('monster_id', None)
            part = self.request.GET.get('part_name', None)
            if monster is not None:
                queryset = queryset.filter(monster_id=monster)
            if part is not None:
                queryset = queryset.filter(part_name=part)
            return queryset


def monster_list(request):
    # response = requests.get('http://127.0.0.1:8000/monsterdata/monster/')
    # average = requests.get('http://127.0.0.1:8000/monster-hzv/?part_name=Average')
    
    # monsters = response.json()
    # monster_averages = average.json()
    # for mon in monsters:
    #     mon['monster_image'] = 'monster_api/'+ str(mon['id']) +'.png'

    # monsters += monster_averages[::-1]
    
    # return render(request, "home.html", {'monsters': monsters})
    pass

def monster_detail(request, pk):
    # response = requests.get('http://127.0.0.1:8000/monster-hzv/?monster_id=' + str(pk))
    # name = requests.get('http://127.0.0.1:8000/monsterdata/monster/' + str(pk) + '/')
    
    # monster_name = name.json()
    # image = 'monster_api/'+ str(pk) +'.png'

    # monster_hzv = response.json()
    # monster_hzv.append(image)
    # monster_hzv.append(monster_name['monster_name'])

    # return render(request, "monster_detail.html", {'monster_hzv': monster_hzv})
    pass