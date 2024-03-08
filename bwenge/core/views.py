# views.py

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Article, Comment,Category,Video
from .serializers import ArticleSerializer, CategorySerializer, CommentSerializer, VideoSerializer

########################################-ARTICLES VIEWS-######################################################

#crete,listing all and select single CATEGORIES
class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SingleCategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#crete,listing all and select single ARTICLES VIEWS
class ArticleCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class SingleArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1  # Increment views count
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

#crete,listing all and select single COMMENTS
class CreateCommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SingleCommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

########################################-VIDEO VIEWS-######################################################

class CreateVideoAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SingleVideoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1  # Increment views count
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
