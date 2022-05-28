from django.urls import path
from watchlist.api import views
from watchlist.api.views import WatchListAV, WatchDetailAv, StreamPlatformAv, StreamPlatformDetailAv, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
   path('list/', WatchListAV.as_view(), name="movie_list"),
   path('<int:pk>/', WatchDetailAv.as_view(), name="movie_detail"),
   path('stream/', StreamPlatformAv.as_view(), name="stream"),
   path('stream/<int:pk>/', StreamPlatformDetailAv.as_view(), name="stream_detail"),
   path('stream/<int:pk>/review_create/', ReviewCreate.as_view(), name="review_create"),
   path('stream/reviews/<int:pk>/', ReviewDetail.as_view(), name="review_detail"),
   path('stream/<int:pk>/reviews/', ReviewList.as_view(), name="reviews")
]
