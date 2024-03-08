# urls.py

from django.urls import path
from .views import (ArticleCreateAPIView, ArticleListAPIView, CreateVideoAPIView,
          SingleArticleAPIView, CategoryCreateAPIView, SingleCategoryAPIView, 
          CreateCommentAPIView,
          SingleCommentAPIView, SingleVideoAPIView, VideoListAPIView)

urlpatterns = [
########################################-ARTICLE URLS-######################################################
#crete,listing all and select single ARTICLES VIEWS
    path('add-categories/', CategoryCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', SingleCategoryAPIView.as_view(), name='category-detail'),

#crete,listing all and select single ARTICLES VIEWS
    path('add-article/', ArticleCreateAPIView.as_view(), name='article-list-create'),
    path('articles/', ArticleListAPIView.as_view(), name='article-list'),
    path('article/<int:pk>/', SingleArticleAPIView.as_view(), name='article-detail'),

#crete,listing all and select single ARTICLES VIEWS
    path('add-comments/', CreateCommentAPIView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', SingleCommentAPIView.as_view(), name='comment-detail'),
########################################-VIDEO urls-######################################################
    path('add-video/', CreateVideoAPIView.as_view(), name='video-list-create'),
    path('videos/', VideoListAPIView.as_view(), name='video-list'),
    path('video/<int:pk>/', SingleVideoAPIView.as_view(), name='video-detail'),

]
