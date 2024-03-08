# Generated by Django 4.1.2 on 2024-03-02 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(default=67, on_delete=django.db.models.deletion.CASCADE, related_name='video_comments', to='core.video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='core.article'),
        ),
    ]
