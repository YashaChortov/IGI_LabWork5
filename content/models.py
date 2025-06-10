from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    client_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Отзыв от {self.client_name}"


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(default="https://example.com")
    published_at = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title