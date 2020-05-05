from django.contrib import admin
from ajaxapp.models import Video, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3
    readonly_fields = ('likes',)

class VideoAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
    readonly_fields = ('likes',)
    prepopulated_fields = {'slug':('title', )}
    list_display = ('title', 'date', 'likes')
    list_filter = ('title', 'date', 'likes')



admin.site.register(Video, VideoAdmin)

# Register your models here.
