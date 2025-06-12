from django.shortcuts import render
from .models import NewsPost


def index(request):
    news = NewsPost.objects.filter(is_published=True).select_related('post_author').order_by('-pub_date')
    return render(request, 'news/news.html', {'news': news})




# Create your views here.
