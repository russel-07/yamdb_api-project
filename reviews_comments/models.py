from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from auth_and_users.models import User
from categories_genres_titles.models import Title


class Review(models.Model):
    text = models.TextField(max_length=2000)
    score = models.PositiveIntegerField(default=None, validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        ordering = ['-id']
        unique_together = ['author', 'title']


class Comment(models.Model):
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    
    class Meta:
        ordering = ['-id']   

