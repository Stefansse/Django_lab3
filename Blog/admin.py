from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from Blog.models import BlogUser, Comment, Post


# Register your models here.

class BlogUserAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "user", "date_of_birth")

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(BlogUser, BlogUserAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "content_of_comment", "date_commented")

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.commented_by) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.commented_by) or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if obj and (request.user in obj.comment_by.blocked_users.all()):
            return False
        return True


admin.site.register(Comment, CommentAdmin)


class CommentPostAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

    inlines = [CommentPostAdmin]

    search_fields = ["title", "content"]

    list_filter = (('date_of_created', DateFieldListFilter),)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.author) or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if obj and (request.user in obj.author.blocked_users.all()):
            return False
        return True


admin.site.register(Post, PostAdmin)
