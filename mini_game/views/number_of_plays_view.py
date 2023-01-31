from .views import *

class NumberOfPlaysView(ViewSet):
    def getall(self, request):
        queryset = NumberOfPlays.objects.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        pagination = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = NumberOfPlaysSerializer(pagination, many=True, fields=['id', 'user_id', 'game_id', 'times'])
        return response_paginator(queryset.count(), paginator.page_size, serializer.data)
    
    