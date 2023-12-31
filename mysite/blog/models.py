from django.db import models
# Importing necessary modules :
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# Creating Model manager
class PublishManager(models.Manager):
    def get_queryset(self) :
        return super().get_queryset()\
        .filter(status = Post.Status.PUBLISHED)
# Creating Draft manager:
class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.DRAFT)
class Post(models.Model):
    # Status subclass:
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    # Many to one relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default= Status.DRAFT)
    objects = models.Manager()
    published = PublishManager()
    drafted = DraftManager()
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