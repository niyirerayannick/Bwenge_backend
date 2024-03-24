# models.py

from django.conf import settings
from django.db import models
from django.forms import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    poster_image = models.ImageField(upload_to='media/posters/')
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    VIDEO_FORMATS = ['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv', 'webm']  # Add more video formats as needed

    def validate_video_file_extension(value):
        if not value.name.split('.')[-1] in Video.VIDEO_FORMATS:
            raise ValidationError(f'Unsupported file format. Please upload a file with one of the following extensions: {", ".join(Video.VIDEO_FORMATS)}')

    video_file = models.FileField(upload_to='media/videos/', validators=[validate_video_file_extension])
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster_image = models.ImageField(upload_to='media/video/posters/')
    categories = models.ManyToManyField(Category)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='article_comments', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='video_comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    reply = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

