from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie, Theatre, Show, Booking
from django.contrib.auth.models import User
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


def get_theatres(request):
    theatres = Theatre.objects.all()
    data = list(theatres.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def create_theatre(request):
    if request.method == "POST":
        data = json.loads(request.body)
        theatre = Theatre.objects.create(
            name=data['name'],
            location=data['location'],
            total_seats=data['total_seats']
        )
        return JsonResponse({"message": "Theatre created", "id": theatre.id})
    

@csrf_exempt
def update_theatre(request, theatre_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        theatre = get_object_or_404(Theatre, id=theatre_id)

        theatre.name = data.get('name', theatre.name)
        theatre.location = data.get('location', theatre.location)
        theatre.total_seats = data.get('total_seats', theatre.total_seats)
        theatre.save()

        return JsonResponse({"message": "Theatre updated"})

@csrf_exempt
def delete_theatre(request, theatre_id):
    if request.method == "DELETE":
        theatre = get_object_or_404(Theatre, id=theatre_id)
        theatre.delete()
        return JsonResponse({"message": "Theatre deleted"})


def get_shows(request):
    shows = Show.objects.all()
    data = list(shows.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def create_show(request):
    if request.method == "POST":
        data = json.loads(request.body)

        movie = get_object_or_404(Movie, id=data['movie_id'])
        theatre = get_object_or_404(Theatre, id=data['theatre_id'])

        show = Show.objects.create(
            movie=movie,
            theatre=theatre,
            show_time=data['show_time'],
            available_seats=data['available_seats']
        )

        return JsonResponse({"message": "Show created", "id": show.id})

@csrf_exempt
def update_show(request, show_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        show = get_object_or_404(Show, id=show_id)

        if 'movie_id' in data:
            show.movie = Movie.objects.get(id=data['movie_id'])

        if 'theatre_id' in data:
            show.theatre = Theatre.objects.get(id=data['theatre_id'])

        show.show_time = data.get('show_time', show.show_time)
        show.available_seats = data.get('available_seats', show.available_seats)
        show.save()

        return JsonResponse({"message": "Show updated"})

@csrf_exempt
def delete_show(request, show_id):
    if request.method == "DELETE":
        show = get_object_or_404(Show, id=show_id)
        show.delete()
        return JsonResponse({"message": "Show deleted"})


def get_bookings(request):
    bookings = Booking.objects.all()
    data = list(bookings.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def create_booking(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user = get_object_or_404(User, id=data['user_id'])
        show = get_object_or_404(Show, id=data['show_id'])

        if show.available_seats < data['seats_booked']:
            return JsonResponse({"error": "Not enough seats"}, status=400)

        booking = Booking.objects.create(
            user=user,
            show=show,
            seats_booked=data['seats_booked']
        )

        show.available_seats -= data['seats_booked']
        show.save()

        return JsonResponse({"message": "Booking created", "id": booking.id})

@csrf_exempt
def update_booking(request, booking_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        booking = get_object_or_404(Booking, id=booking_id)

        booking.seats_booked = data.get('seats_booked', booking.seats_booked)
        booking.save()

        return JsonResponse({"message": "Booking updated"})

@csrf_exempt
def delete_booking(request, booking_id):
    if request.method == "DELETE":
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return JsonResponse({"message": "Booking deleted"})

