from rest_framework import serializers
from .models import Hero
from .models import Villan

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        Hero = Herofields = ['name', 'alter_ego','primary_ability','secondary_ability', 'catchphrase', 'super_type']


class VillanSerializer(serializers.ModelSerializer):
    class Meta:
        Villan = Herofields = ['name', 'alter_ego','primary_ability','secondary_ability', 'catchphrase', 'super_type']
