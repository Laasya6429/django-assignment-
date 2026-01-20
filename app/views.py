from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie
import json


def get_movies(request):
    movies = Movie.objects.all()
    data = list(movies.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def create_movie(request):
    if request.method == "POST":
        data = json.loads(request.body)
        movie = Movie.objects.create(
            title=data['title'],
            duration=data['duration'],
            language=data['language'],
            release_date=data['release_date']
        )
        return JsonResponse({"message": "Movie created", "id": movie.id})



@csrf_exempt
def update_movie(request, movie_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        movie = Movie.objects.get(id=movie_id)
        movie.title = data.get('title', movie.title)
        movie.duration = data.get('duration', movie.duration)
        movie.language = data.get('language', movie.language)
        movie.save()
        return JsonResponse({"message": "Movie updated"})

@csrf_exempt
def delete_movie(request, movie_id):
    if request.method == "DELETE":
        Movie.objects.get(id=movie_id).delete()
        return JsonResponse({"message": "Movie deleted"})
