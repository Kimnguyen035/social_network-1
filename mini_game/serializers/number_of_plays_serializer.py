from rest_framework import serializers
# from ..models.user import User
from .action_seralizer import ActionSerializer
from configs.variable_response import *
from ..models.number_of_plays import *

class NumberOfPlaysSerializer(serializers.ModelSerializer, ActionSerializer):
    user_id = serializers.IntegerField(allow_null = True)
    game_id = serializers.IntegerField(allow_null=True)
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
    # ============================== end contructor ===========================
    
    # def validate_user_id(self, value):
    #     queryset = User.objects.filter(id=value)
    #     if not queryset.exists():
    #         raise serializers.ValidationError(ERROR['not_exists'])
    #     return value
    
    class Meta:
        model = NumberOfPlays
        fields = ['id','user_id','game_id','times','created_at','updated_at','deleted_at']