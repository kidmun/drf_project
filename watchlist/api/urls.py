from django.urls import path
from watchlist.api import views
from watchlist.api.views import MovieListAV, MovieDetailAv

urlpatterns = [
   path('list/', MovieListAV.as_view(), name="movie_list"),
   path('<int:pk>/', MovieDetailAv.as_view(), name="movie")
]
