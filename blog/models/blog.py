from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    picture_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text="URL to the blog's featured image"
    )

    class Meta:
        ordering = ['-created_at']
