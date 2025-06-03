from django.db import models
from django.conf import settings


class Comment(models.Model):
    content = models.TextField(max_length=5000)
    likes_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    blog = models.ForeignKey(
        'blog.Blog',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )
