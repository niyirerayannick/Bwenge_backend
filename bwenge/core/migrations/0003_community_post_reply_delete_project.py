# Generated by Django 5.0.3 on 2024-04-01 00:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administered_communities', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='joined_communities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content_type', models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('file', 'File'), ('video', 'Video'), ('url', 'URL')], default='text', max_length=10)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('file_content', models.FileField(blank=True, null=True, upload_to='post_files/')),
                ('video_content', models.FileField(blank=True, null=True, upload_to='post_videos/')),
                ('url_content', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.community')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.post')),
            ],
        ),
        migrations.DeleteModel(
            name='project',
        ),
    ]