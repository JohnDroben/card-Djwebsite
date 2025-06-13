from django.contrib import admin
from .models import NewsPost

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'is_published')
    list_filter = ('is_published', 'pub_date', 'author')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'excerpt', 'content', 'image')
        }),
        ('Метаданные', {
            'fields': ('author', 'is_published'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(NewsPost, NewsPostAdmin)

