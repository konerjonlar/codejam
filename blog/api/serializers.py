from rest_framework import serializers

from blog.models import Post, Project


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "description", "tags", "is_active")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "description", "tags", "is_active")
