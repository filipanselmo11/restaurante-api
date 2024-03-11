from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Restaurante
from .serializers import RestauranteSerializer

@api_view(['GET'])
def getRestaurantes(request):
    restaurantes = Restaurante.objects.all()
    serializer = RestauranteSerializer(restaurantes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRestaurante(request, pk):
    restaurante = Restaurante.objects.get(id=pk)
    serializer = RestauranteSerializer(restaurante, many=False)
    return Response(serializer.data)