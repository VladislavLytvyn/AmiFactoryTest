from django import forms


class SearchMovieForm(forms.Form):
    genre = forms.IntegerField(required=False)
    src = forms.CharField(required=False, max_length=20, min_length=2)
    page = forms.IntegerField(required=False, min_value=1)


class SearchMovieIdForm(forms.Form):
    movie_id = forms.IntegerField(required=True, min_value=1)
