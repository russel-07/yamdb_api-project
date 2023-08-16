from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['-id']


class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    # rating = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='titles', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='titles', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['-id']
