from .views import *

class NumberOfPlaysView(ViewSet):
    def getall(seft, request):
        return response_data()