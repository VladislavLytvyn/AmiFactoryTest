from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from .models import Movie
from .forms import SearchMovieForm, SearchMovieIdForm


def serialize_movie(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "release_year": movie.release_year,
        "mpa_rating": movie.mpa_rating,
        "imdb_rating": movie.imdb_rating,
        "duration": movie.duration,
        "poster": movie.poster.url if movie.poster else "",
        "bg_picture": movie.bg_picture.url if movie.bg_picture else "",
        "genres": [{"id": genre.id, "title": genre.title} for genre in movie.genres.all()],
        "directors": [{"id": director.id,
                       "first_name": director.first_name,
                       "last_name": director.last_name} for director in movie.directors.all()],
        "writers": [{"id": writer.id,
                     "first_name": writer.first_name,
                     "last_name": writer.last_name} for writer in movie.writers.all()],
        "stars": [{"id": star.id,
                   "first_name": star.first_name,
                   "last_name": star.last_name} for star in movie.stars.all()],
    }


class MoviesAPIView(View):
    def get(self, request, *args, **kwargs):
        form = SearchMovieForm(request.GET)

        if form.is_valid():
            genre = form.cleaned_data.get("genre")
            src = form.cleaned_data.get("src")
            page = form.cleaned_data.get("page") or 1

            movies = Movie.objects.all()
            movies = movies.filter(Q(genres__id=genre) & Q(title__icontains=src))

            paginator = Paginator(movies, 1)
            try:
                movies_page = paginator.page(page)
            except Exception as e:
                return JsonResponse({"error": [str(e)]}, status=400)

            movies_data = []
            for movie in movies_page:
                movies_data.append(serialize_movie(movie))

            response_data = {
                "pages": paginator.num_pages,
                "total": paginator.count,
                "results": movies_data
            }

            return JsonResponse(response_data)
        else:
            return JsonResponse({"errors": [form.errors]}, status=400)


class MovieDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        form = SearchMovieIdForm({'movie_id': pk})
        if form.is_valid():
            try:
                movie = Movie.objects.get(pk=pk)
                data = serialize_movie(movie)
                return JsonResponse(data)
            except Movie.DoesNotExist:
                return JsonResponse({"error": "movie__not_found"}, status=404)
        else:
            return JsonResponse({"errors": form.errors}, status=400)
