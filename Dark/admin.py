from django.contrib import admin
from .models import Post, DarkUser
from django.utils.html import format_html

# admin.site.register(Post)
# admin.site.register(DarkUser)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['owner', 'text']

@admin.register(DarkUser)
class DarkUserAdmin(admin.ModelAdmin):
    def image_tab(self, obj):
        return format_html('<img scr="/Darkfile/{{obj.image}}>')
    
    image_tab.short_description = 'Image'

    list_display = ['last_name', 'first_name', 'image_tab',]
    list_filter = ['first_name', 'last_name']
    ordering = ['last_name']
