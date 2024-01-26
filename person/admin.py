from django.contrib import admin

from person.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """
        PersonAdmin
    """
    list_display = ["created_at", "updated_at", "first_name", "last_name", "types"]
