from rest_framework import serializers

from .models import Monster, Monster_HZV

class MonsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster
        fields = ('id', 'monster_name')

class MonsterHZVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monster_HZV
        fields = '__all__'