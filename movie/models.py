from django.core.validators import FileExtensionValidator
from django.db import models

from genre.models import Genre
from person.models import Person

MPA_RATING = (
    ("g", "G"),
    ("pg", "PG"),
    ("pg-13", "PG-13"),
    ("r", "R"),
    ("nc-17", "NC-17"),
)


class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    poster = models.FileField(blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=["jpeg", "jpg"])])
    bg_picture = models.FileField(blank=True, null=True,
                                  validators=[FileExtensionValidator(allowed_extensions=["jpeg", "jpg"])])
    release_year = models.IntegerField(blank=True, null=True)
    mpa_rating = models.CharField(choices=MPA_RATING, max_length=10, blank=True, null=True)
    imdb_rating = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    directors = models.ManyToManyField(Person, blank=True, related_name="directed_movies")
    writers = models.ManyToManyField(Person, blank=True, related_name="written_movies")
    stars = models.ManyToManyField(Person, blank=True, related_name="acted_movies")
