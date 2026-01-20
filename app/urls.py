from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', get_movies),
    path('movies/create/', create_movie),
    path('movies/update/<int:movie_id>/', update_movie),
    path('movies/delete/<int:movie_id>/', delete_movie),
]
