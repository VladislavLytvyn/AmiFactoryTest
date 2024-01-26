from django.contrib import admin

from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
        MovieAdmin
    """
    list_display = ["created_at", "updated_at", "title", "description", "release_year", "mpa_rating", "imdb_rating",
                    "duration"]

