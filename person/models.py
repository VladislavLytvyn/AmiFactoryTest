from django.db import models

from genre.models import Genre

TYPES = (
    ('director', 'Director'),
    ('writer', 'Writer'),
    ('actor', 'Actor'),
)


class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    types = models.CharField(choices=TYPES, max_length=10, blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name