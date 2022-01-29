from pickle import TRUE
from django.db import models

# Create your models here.
class Monster(models.Model):
    id = models.IntegerField(primary_key=TRUE)
    monster_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.monster_name

class Monster_HZV(models.Model):
    part_id = models.IntegerField()
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE, blank=False)
    part_name = models.CharField(max_length=50)
    state = models.IntegerField()
    sever = models.IntegerField()
    impact  = models.IntegerField()
    ammo = models.IntegerField()
    fire = models.IntegerField()
    water = models.IntegerField()
    thunder = models.IntegerField()
    ice = models.IntegerField()
    dragon = models.IntegerField()
    stun = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.part_id},{self.monster_id},{self.part_name},{self.state},{self.sever},{self.impact},{self.ammo},{self.fire},"\
                 + f"{self.water},{self.ice},{self.thunder},{self.dragon},{self.stun}"