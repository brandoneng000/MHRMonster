from pickle import TRUE
from django.db import models

# Create your models here.
class Monster(models.Model):
    id = models.IntegerField(primary_key=TRUE)
    monster_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.monster_name