from django.urls import path
from watchlist.api import views
from watchlist.api.views import WatchListAV, WatchDetailAv, StreamPlatformAv, StreamPlatformDetailAv

urlpatterns = [
   path('list/', WatchListAV.as_view(), name="movie_list"),
   path('list/<int:pk>/', WatchDetailAv.as_view(), name="movie_detail"),
   path('stream/', StreamPlatformAv.as_view(), name="stream"),
   path('stream/<int:pk>/', StreamPlatformDetailAv.as_view(), name="stream_detail")
]
