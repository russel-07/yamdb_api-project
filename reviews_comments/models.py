from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from auth_and_users.models import User
from categories_genres_titles.models import Title

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=2000)
    score = models.PositiveIntegerField(default=None, validators=[MinValueValidator(1), MaxValueValidator(10)])
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    
