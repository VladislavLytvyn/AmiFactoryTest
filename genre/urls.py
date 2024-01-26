from django.urls import path
from .views import GenresAPIView

urlpatterns = [
    path('genres/', GenresAPIView.as_view(), name="genres"),
]
