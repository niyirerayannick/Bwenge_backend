from django.urls import path
from .views import ( 
    dashboard, addVideo,
    video_list,
    # user_list,
    add_user,
    # delete_video,
    # edit_video,
    # delete_user,
    # edit_user,
)

urlpatterns = [

   
    path('add-video/', addVideo, name='add-video'),
    path('', dashboard, name='dashboard'),
    path('video_list/', video_list, name='video_list'),
    # path('dashiboard/user_list/', user_list, name='user_list'),
    path('add_user/', add_user, name='add_user'),
    # path('dashboard/video/<int:video_id>/edit/', edit_video, name='edit_video'),
    # path('dashboard/video/<int:video_id>/delete/', delete_video, name='delete_video'),
    # path('dashboard/user/<int:user_id>/', delete_user, name='delete_user'),
    # path('dashboard/edit_user/<int:user_id>/', edit_user, name='edit_user'),


    

]