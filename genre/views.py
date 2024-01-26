from django.http import JsonResponse
from django.views import View
from .models import Genre


class GenresAPIView(View):
    def get(self, request, *args, **kwargs):
        genres = Genre.objects.all()
        data = [{"id": genre.id,
                 "title": genre.title} for genre in genres]
        return JsonResponse(data, safe=False)
