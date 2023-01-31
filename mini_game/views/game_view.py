from .views import *

class GameView(ViewSet):
    def getall(self, request):
        queryset = Game.objects.filter(deleted_at__isnull=True)
        all_data = GameSerializer(queryset,many=True)
        return response_data(all_data.data)
    
    def get_detail(self, request, id):
        validate = IdGetGameValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = Game.objects.get(id=validate.data['id'])
        if detail is None:
            return response_data(
                ERROR['id_not_exists'],
                STATUS['NO_DATA']
            )
        result = GameSerializer(detail)
        return response_data(
            result.data
        )
    
    def post(self, request):
        data = request.data.copy()
        data_save = GameSerializer(data=data)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(
            message=SUCCESS['post_game'],
            data=data_save.data
        )
        
    def put(self, request, id):
        data = request.data.copy()
        validate = IdGetGameValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = Game.objects.get(id=validate.data['id'])
        data_save = GameSerializer(detail,data=data,partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(
            message=SUCCESS['put_game'],
            data=data_save.data
        )
        
    def delete(self, request, id):
        validate = IdGetGameValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = Game.objects.get(id=validate.data['id'])
        detail.soft_delete()
        return response_data(message=SUCCESS['delete_game'])
    
    def restore(self, request, id):
        validate = IdGetGameValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        detail = Game.objects.get(id=validate.data['id'])
        detail.restore()
        return response_data(message=SUCCESS['restore_game'])
    
    def drop(self, request, id):
        validate = IdGetGameValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        Game.objects.get(id=validate.data['id']).delete()
        return response_data(message=SUCCESS['drop_number_of_plays'])