from django.db import models


class Profile(models.Model):
    nickname = models.CharField(max_length=255)
    rating = models.IntegerField(default=10)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to="profile/avatars")

    steam_url = models.URLField(blank=True)
    wow_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)

    def __str__(self):
        return self.nickname


class Review(models.Model):
    author = models.ForeignKey(Profile, related_name="Author", on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, related_name="Profile", on_delete=models.CASCADE
    )
    text = models.TextField()

    review_karma = models.IntegerField(default=0)

    def __str__(self):
        return self.text, self.review_karma
