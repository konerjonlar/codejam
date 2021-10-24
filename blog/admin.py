from django.contrib import admin

from blog.models import Post, Project


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "get_tags", "is_active")
    search_fields = ("title", "tags")

    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Post Information",
            {
                "fields": (
                    "author",
                    "title",
                    "description",
                    "content",
                    "tags",
                    "image",
                    "is_active",
                ),
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "tags", "is_active")
    search_fields = ("title", "tags")

    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Post Information",
            {
                "fields": (
                    "title",
                    "description",
                    "site",
                    "tags",
                    "is_active",
                ),
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
