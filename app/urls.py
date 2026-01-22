from django.urls import path
from . import views

urlpatterns = [
    # Movie
    path('movies/', views.get_movies),
    path('movies/create/', views.create_movie),
    path('movies/update/<int:movie_id>/', views.update_movie),
    path('movies/delete/<int:movie_id>/', views.delete_movie),

    # Theatre
    path('theatres/', views.get_theatres),
    path('theatres/create/', views.create_theatre),
    path('theatres/update/<int:theatre_id>/', views.update_theatre),
    path('theatres/delete/<int:theatre_id>/', views.delete_theatre),

    # Show
    path('shows/', views.get_shows),
    path('shows/create/', views.create_show),
    path('shows/update/<int:show_id>/', views.update_show),
    path('shows/delete/<int:show_id>/', views.delete_show),

    # Booking
    path('bookings/', views.get_bookings),
    path('bookings/create/', views.create_booking),
    path('bookings/update/<int:booking_id>/', views.update_booking),
    path('bookings/delete/<int:booking_id>/', views.delete_booking),
]

