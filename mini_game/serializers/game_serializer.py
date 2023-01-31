from rest_framework import serializers
from .action_seralizer import ActionSerializer
from configs.variable_response import *
from ..models.game import *

class GameSerializer(serializers.ModelSerializer, ActionSerializer):
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            for item in not_fields:
                self.fields.pop(item)
    # ============================== end contructor ===========================
    
    class Meta:
        model = Game
        fields = ['id','game_name','created_at','updated_at','deleted_at']