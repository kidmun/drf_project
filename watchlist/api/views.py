from rest_framework import status
from rest_framework.exceptions import ValidationError
from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("you have already reviewed this movie")
        serializer.save(watchlist=movie, review_user=review_user)
        
    


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # overide queryset
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return  Review.objects.filter(watchlist=pk)
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAv(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':"Movie not found"}, status=status.HTTP_404_NOT_FOUND)


class StreamPlatformDetailAv(APIView):
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(id=pk)
            serializer = StreamPlatformSerializer(platform)
            return Response(serializer.data)
        except:
            raise serializers.ValidationError("platform not found")
        
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(id=pk)
        serializer = StreamPlatformSerializer(platform, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(id=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class WatchListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAv(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'error':"Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk):
        movie = WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
        
        
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
        
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie(request, pk):
#     try:
#         movie = Movie.objects.get(id=pk)
#     except Movie.DoesNotExist:
#         return Response({'error':"Movie not found"}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        

