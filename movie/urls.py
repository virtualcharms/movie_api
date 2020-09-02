from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.MovieList, name='movie_list'),
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie_detail'),

]
