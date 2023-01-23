from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hero
from super_types.models  import Villan
from super_types import HeroSerializer


@api_view(["GET"])
def hero_list(request):

    Hero = Hero.objects.all()
    
    serializer = HeroSerializer(Hero, many = True)


    return Response (serializer.data)
