from django.urls import path

from blog import views

urlpatterns = [
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post-detail"),
    path("projects/", views.ProjectListView.as_view(), name="project-list"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project-detail"),
    # path("dashboard/", views.dashboard, name="dashboard") ,
    # path('article/<slug:slug>/',views.detail,name = "detail"),
]
