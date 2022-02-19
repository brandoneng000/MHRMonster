# MHRMonsterDjangoAPI

[https://mhr-monsters.herokuapp.com/](https://mhr-monsters.herokuapp.com/)

## Overview

MHR Monster is a site deployed on Heroku using Python/Django. The website presents users with
information for the various large monsters in [Monster Hunter Rise](https://www.monsterhunter.com/rise).
Initial page shows a list of monsters and their average weakness against weapon types and elements. Each image
redirects to a full overview of that particular monster. 

The frontend uses Django Template and backend is an API designed with Django REST Framework.

## Damage Types

The types of damage player can do to monsters.

|Damage Type|Image|
|-----------|-----|
|Sever|![](/static/icons/sever.png)|
|Blunt|![](/static/icons/impact.png)|
|Ammo|![](/static/icons/ammo.png)|
|Fire|![](/static/icons/fire.png)|
|Water|![](/static/icons/water.png)|
|Thunder|![](/static/icons/thunder.png)|
|Ice|![](/static/icons/ice.png)|
|Dragon|![](/static/icons/dragon.png)|
|Stun|![](/static/icons/stun.png)|

## Tools

- [MonsterHunterRiseData](https://github.com/brandoneng000/MonsterHunterRiseData/) was used to gather values
- [Kiranico](https://mhrise.kiranico.com/data/monsters) has the monster data