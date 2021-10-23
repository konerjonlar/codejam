from django.db import models
from taggit.managers import TaggableManager


class BaseContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseContent):
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"


class Project(BaseContent):
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
