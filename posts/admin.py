from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import Post,Comment

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields =['content',]
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'is_enable','publish_date','created_time', 'update_time']
    inlines = [CommentAdminInline,]



class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'created_time']
    

# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)



