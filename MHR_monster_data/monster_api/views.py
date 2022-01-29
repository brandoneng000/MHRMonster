from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MonsterHZVSerializer, MonsterSerializer
from .models import Monster, Monster_HZV

# Create your views here.
class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all().order_by('id')
    serializer_class = MonsterSerializer

class MonsterHZVViewSet(viewsets.ModelViewSet):
    queryset = Monster_HZV.objects.all().order_by('part_id')
    serializer_class = MonsterHZVSerializer