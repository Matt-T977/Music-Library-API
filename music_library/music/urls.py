from django.urls import path
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
    path('music/like/<int:pk>/', views.SongLikes.as_view()),
    path('music/dislike/<int:pk>/', views.SongDislikes.as_view())
]