from django.contrib import admin

from .models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'score', 'title', 'pub_date')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'review', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
