from django.db import models
from django.contrib.auth.models import User

import datetime

REVIEW_KARMA_CHOICES = [-1, 0, 1]


class Profile(models.Model):
    nickname = models.CharField(max_length=255)
    rating = models.IntegerField(default=10)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to="profile/avatars")

    steam_url = models.URLField(blank=True)
    wow_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)

    user = models.ForeignKey(User, related_name="User", on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return self.nickname


class Review(models.Model):
    author = models.ForeignKey(Profile, related_name="Author", on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, related_name="Profile", on_delete=models.CASCADE
    )
    text = models.TextField()

    review_karma = models.IntegerField(default=0)
    review_rating = models.IntegerField(
        default=0, choices=((-1, "Bad"), (0, "Normal"), (1, "Good"))
    )
    created = models.DateTimeField(blank=True, default=datetime.datetime.now)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"{self.text}, {self.review_karma}"
