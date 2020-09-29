from django.urls import path

from users.views import *

urlpatterns = [
    path('current-place/', current_place, name='user-current-place'),
    path('user-checkin/', user_checkin, name='user_checkin'),
    path('follow-user/', follow_user, name='follow_user'),
    path('unfollow-user/', unfollow_user, name='unfollow_user'),
    path('user-following-list/', user_following_list, name='user_following_list'),
    path('user-checked_in-location/', user_checked_in_location, name='user_checked_in_location'),
]
