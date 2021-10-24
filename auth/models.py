from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    about = models.CharField(max_length=200)

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Social(models.Model):
    name = models.CharField(max_length=120)
    logo = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "social link"
        verbose_name_plural = "social links"


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    logo = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"
