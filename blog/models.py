from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


class BaseContent(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        abstract = True


class Post(BaseContent):
    author = models.ForeignKey("blog_auth.User", on_delete=models.CASCADE, default=1)
    content = RichTextField()
    image = models.ImageField(
        "Gorsel",
        upload_to="post_images",
        default="not_found.jpg",
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"


class Project(BaseContent):
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.slug = slugify(self.title)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
