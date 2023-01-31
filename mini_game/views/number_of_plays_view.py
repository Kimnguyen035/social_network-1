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
            return validate_error(validate.errors,STATUS['NO_DATA'])
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
        data_save = NumberOfPlaysSerializer(data=data)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(
            message=SUCCESS['post_number_of_plays'],
            data=data_save.data
        )
        
    def put(self, request, id):
        data = request.data.copy()
        validate = IdGetNumberOfPlaysValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = NumberOfPlays.objects.get(id=validate.data['id'])
        data_save = NumberOfPlaysSerializer(detail,data=data,partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(
            message=SUCCESS['put_number_of_plays'],
            data=data_save.data
        )
        
    def delete(self, request, id):
        validate = IdGetNumberOfPlaysValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = NumberOfPlays.objects.get(id=validate.data['id'])
        detail.soft_delete()
        return response_data(message=SUCCESS['delete_number_of_plays'])
    
    def restore(self, request, id):
        validate = IdGetNumberOfPlaysValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = NumberOfPlays.objects.get(id=validate.data['id'])
        detail.restore()
        return response_data(message=SUCCESS['restore_number_of_plays'])
    
    def drop(self, request, id):
        validate = IdGetNumberOfPlaysValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        NumberOfPlays.objects.get(id=validate.data['id']).delete()
        return response_data(message=SUCCESS['drop_number_of_plays'])