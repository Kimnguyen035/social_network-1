from django.urls import path
from .views.number_of_plays_view import *

all_url = {
    'number_of_plays': [
        path('getall', NumberOfPlaysView.as_view({'get':'getall'}), name='getall'),
    ]
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]