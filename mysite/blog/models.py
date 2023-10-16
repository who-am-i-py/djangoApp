from django.db import models
# Importing necessary modules :
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    # Status subclass:
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default= Status.DRAFT)
    # Defining a default sort order:
    class Meta:
        # ordering with reverse chonological order by adding -
        ordering = ['-publish']
        # Indexing database
        indexes = [
            models.Index(fields=["-publish"],)
        ]
    def __str__(self) :
        return f"[{self.title}]"