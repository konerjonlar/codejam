from rest_framework import mixins, viewsets

from blog.api.serializers import BlogSerializer
from blog.models import Blog


class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
