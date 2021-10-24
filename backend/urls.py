"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from taggit.models import Tag

from auth.api.urls import auth_router
from auth.models import Social, User
from blog.api.urls import blog_router
from blog.models import Post, Project

router = routers.DefaultRouter()
router.registry.extend(auth_router.registry)
router.registry.extend(blog_router.registry)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["admin"] = User.objects.first()
        context["posts"] = Post.objects.all()
        context["projects"] = Project.objects.all()
        context["tags"] = Tag.objects.all()
        context["skills"] = Social.objects.all()

        return context


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("blog/", include("blog.urls")),
    path("", IndexView.as_view(), name="index"),
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
