from .views import *
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
import mimetypes


class MediaView(ViewSet):
    def upload(self, request):
        data_user = hp.get_user_info(request=request)
        path_media = 'http://' + request.META['HTTP_HOST'] + '/{}/'.format(vs.FILES['download_file'])
        myfile = request.FILES.getlist('file')
        list_name = []
        for item in myfile:
            name = str(data_user['id']) + (datetime.now()).strftime('%d%m%Y%H%M%S') + '.' + str(item.name).split('.')[-1]
            fs = FileSystemStorage()
            file_name = fs.save(name, item)
            path_file = str(fs.url(file_name)).split('/')[-1]
            list_name.append(path_media + path_file)
        return response_data(list_name)
    
    def rm_upload(self, request, id):
        # validate
        validate = FileDownloadValidate(data={'id':str(id)})
        if not validate.is_valid():
            return validate_error(validate.errors)
        # file = validate.data
        os.remove(os.path.join(vs.MEDIA_ROOT, id))
        return response_data()
    
    def download_file(self, request, id):
        # validate
        validate = FileDownloadValidate(data={'id':str(id)})
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        data = validate.data.copy()
        
        # open file
        file = self.file_to_byte(data['id'], data['type'])
        
        # return file
        return StreamingHttpResponse(
            FileWrapper(file),
            content_type='application/'+
            data['type']
        )
        
    def show_file(self, request, id):
        validate = FileDownloadValidate(data={'id':str(id)})
        if not validate.is_valid():
            return validate_error(validate.errors)
        data = validate.data.copy()
        file = self.file_to_byte(data['id'], data['type'])
        return FileResponse(file)
        
    def read_file(self, request):
        data = request.data.copy()
        
        # validate
        validate = FileDownloadValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        
        type_file = validate.data.copy()
        if vs.JSON_TYPE in type_file['type']:
            result = self.file_to_byte(type_file['id'], type_file['type'])
            return response_data(json.load(result))
        if vs.EXCEL_TYPE in type_file['type']:
            return response_data()
        
        return response_data()
    
    def file_to_byte(self, id, type):
        # path file
        path_file = vs.STR_MEDIA_PATH.format(
            vs.MEDIA_ROOT,
            id,
            type
        )
        
        # open file
        file = open(path_file, 'rb')
        
        return file