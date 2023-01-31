from rest_framework import serializers
from ..models.game import Game
from configs.variable_response import *

class IdGetGameValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    def validate_id(self, value):
        queryset = Game.objects.filter(id=value)
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        return value