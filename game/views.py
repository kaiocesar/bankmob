from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)