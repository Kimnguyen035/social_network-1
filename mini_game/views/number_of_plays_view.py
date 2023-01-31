from .views import *

class NumberOfPlaysView(ViewSet):
    def getall(self, request):
        queryset = NumberOfPlays.objects.filter(deleted_at__isnull=True)
        paginator = StandardPagination()
        pagination = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = NumberOfPlaysSerializer(pagination, many=True, fields=['id', 'user_id', 'game_id', 'times'])
        return response_paginator(queryset.count(), paginator.page_size, serializer.data)
    
    def get_detail(self, request, id):
        validate = IdGetNumberOfPlaysValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        detail = NumberOfPlays.objects.get(id=validate.data['id'])
        if detail is None:
            return response_data(
                ERROR['id_not_exists'],
                STATUS['NO_DATA']
            )
        result = NumberOfPlaysSerializer(detail)
        return response_data(
            message=SUCCESS['post_number_of_plays'],
            data=result.data
        )
    
    def post(self, request):
        data = request.data.copy()
        post_save = NumberOfPlaysSerializer(data=data)
        if not post_save.is_valid():
            return validate_error(post_save.errors)
        post_save.save()
        return response_data(
            message=SUCCESS['post_number_of_plays'],
            data=post_save.data
        )