from rest_framework import serializers
from ..models.game import Game
from configs.variable_response import *
from ..serializers.game_serializer import *

class IdGetGameValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    data = GameSerializer(required=False, allow_null=False)
    
    def validate(self, value):
        queryset = Game.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        value['data'] = queryset.values()[0]
        return value