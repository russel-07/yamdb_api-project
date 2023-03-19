from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    rating = models.FloatField(default=0)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, related_name='titles', blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, related_name='titles', blank=True, null=True)

