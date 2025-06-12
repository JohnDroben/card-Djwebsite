from django.contrib import admin
from .models import NewsPost

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'is_published')
    list_filter = ('is_published', 'pub_date', 'author')
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'author', 'is_published', 'pub_date')
    readonly_fields = ('pub_date',)

admin.site.register(NewsPost, NewsPostAdmin)

