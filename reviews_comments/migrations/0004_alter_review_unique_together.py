# Generated by Django 4.1.7 on 2023-03-21 10:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories_genres_titles', '0002_rename_categorie_category_remove_title_genre_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews_comments', '0003_alter_review_score_alter_review_text'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('author', 'title')},
        ),
    ]