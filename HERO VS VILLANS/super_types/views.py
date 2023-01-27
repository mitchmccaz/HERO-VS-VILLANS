from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hero
from .models  import Villan
from serializers import HeroSerializer
from serializers import VillanSerializer


@api_view(["GET"])
def hero_list(request):

    Hero = Hero.objects.all()
    
    serializer = HeroSerializer(Hero, many = True)


    return Response (serializer.data)



@api_view(["GET"])
def villan_list(request):

    Villan = Villan.objects.all()
    
    serializer = VillanSerializer(Villan, many = True)


    return Response (serializer.data)

