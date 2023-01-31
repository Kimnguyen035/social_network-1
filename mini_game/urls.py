from django.urls import path
from .views.number_of_plays_view import *
from .views.auth_views import *
from .views.game_view import *

all_url = {
    'number_of_plays': [
        path('getall-number-of-play', NumberOfPlaysView.as_view({'get':'getall'}), name='getall'),
        path('get-detail-number-of-play/<int:id>', NumberOfPlaysView.as_view({'get':'get_detail'}), name='getall'),
        path('post-number-of-play', NumberOfPlaysView.as_view({'post':'post'}), name='post'),
        path('put-number-of-play/<int:id>', NumberOfPlaysView.as_view({'put':'put'}), name='put'),
        path('delete-number-of-play/<int:id>', NumberOfPlaysView.as_view({'delete':'delete'}), name='delete'),
        path('restore-number-of-play/<int:id>', NumberOfPlaysView.as_view({'delete':'restore'}), name='restore'),
        path('drop-number-of-play/<int:id>', NumberOfPlaysView.as_view({'delete':'drop'}), name='drop'),
    ],
    'game': [
        path('getall-game', GameView.as_view({'get':'getall'}), name='getall'),
        path('get-detail-game/<int:id>', GameView.as_view({'get':'get_detail'}), name='getall'),
        path('post-game', GameView.as_view({'post':'post'}), name='post'),
        path('put-game/<int:id>', GameView.as_view({'put':'put'}), name='put'),
        path('delete-game/<int:id>', GameView.as_view({'delete':'delete'}), name='delete'),
        path('restore-game/<int:id>', GameView.as_view({'delete':'restore'}), name='restore'),
        path('drop-game/<int:id>', GameView.as_view({'delete':'drop'}), name='drop'),
    ],
    'url_auth':[
        path('login', AuthView.as_view({'post':'login'}), name='login'),
        path('refresh-token', AuthView.as_view({'post':'refresh_token'}), name='refresh_token'),
        path('register', AuthView.as_view({'post':'register'}), name='register'),
    ],
    'url_in_auth':[
        path('get-data-token', AuthView.as_view({'get':'get_data_token'}), name='get_data_token'),
        path('logout', AuthView.as_view({'post':'logout'}), name='logout'),
    ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]