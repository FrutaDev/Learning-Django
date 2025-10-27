from django.contrib import admin
from .models import Post, Author, Tag, Subscriber, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date", "author")
    list_filter = ("date", "author", "tags")
    search_fields = ("title", "content", "author__first_name", "author__last_name", "tags__name")
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "date", "is_approved", "post_slug")
    list_filter = ("is_approved", "date")
    search_fields = ("user_name", "date", "is_approved")
    
    def post_slug(self, obj):
        return obj.post.slug

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Subscriber)
admin.site.register(Comment, CommentAdmin)