# Generated by Django 5.0.3 on 2024-03-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='pdf_url',
            field=models.FileField(upload_to='media/COURSE/'),
        ),
    ]
