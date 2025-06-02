from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text="URL to the user's profile image"
    )
