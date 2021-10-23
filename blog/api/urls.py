from rest_framework import routers

from blog.api.views import PostViewSet

blog_router = routers.SimpleRouter()


blog_router.register("posts", PostViewSet, "posts")
