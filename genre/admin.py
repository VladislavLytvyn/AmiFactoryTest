from django.contrib import admin

from genre.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
        GenreAdmin
    """
    list_display = ["created_at", "updated_at", "title"]
