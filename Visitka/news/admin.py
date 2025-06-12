from django.contrib import admin
from .models import NewsPost
from django.contrib.auth.models import User



@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'post_author', 'is_published')
    list_filter = ('is_published', 'pub_date', 'post_author')
    search_fields = ('title', 'content')

    def save_model(self, request, obj, form, change):
        if not obj.post_author_id:  # Если автор не установлен
            obj.post_author = request.user  # Устанавливаем текущего пользователя
        super().save_model(request, obj, form, change)





# Register your models here.
