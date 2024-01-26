from django.urls import path
from .views import MoviesAPIView, MovieDetailView

urlpatterns = [
    path('movies/', MoviesAPIView.as_view(), name="movies"),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name="movie"),
]

