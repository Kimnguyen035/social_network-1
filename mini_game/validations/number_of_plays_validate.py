from rest_framework import serializers
from ..models.number_of_plays import NumberOfPlays
from configs.variable_response import *
from ..serializers.number_of_plays_serializer import *

class IdGetNumberOfPlaysValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    def validate_id(self, value):
        queryset = NumberOfPlays.objects.filter(id=value)
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        return value