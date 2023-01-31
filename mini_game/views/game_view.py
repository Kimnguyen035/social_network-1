from .views import *

class GameView(ViewSet):
    def getall(self, request):
        queryset = Game.objects.filter(deleted_at__isnull=True)
        all_data = GameSerializer(queryset,many=True)
        return response_data(all_data.data)