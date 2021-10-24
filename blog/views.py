from django.views import generic

from blog.models import Post, Project


class PostDetailView(generic.DetailView):
    template_name = "post/post-detail.html"
    model = Post


class PostListView(generic.ListView):
    template_name = "post/post-list.html"
    model = Post
    object_list = Post.objects.filter(is_active=True)


class ProjectDetailView(generic.DetailView):
    template_name = "project/project-detail.html"
    model = Project


class ProjectListView(generic.ListView):
    template_name = "project/project-list.html"
    model = Project
    object_list = Project.objects.filter(is_active=True)
