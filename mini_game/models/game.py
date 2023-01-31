from .soft_delete import *

class Game(SoftDeleteModel):
    class Meta:
        db_table = 'game'
    id = models.BigAutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()