from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-id']


class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    #rating = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='titles', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='titles', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']

