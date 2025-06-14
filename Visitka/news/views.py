from django.shortcuts import render, get_object_or_404
from .models import NewsPost




def index(request):
    news = NewsPost.objects.filter(is_published=True).order_by('-pub_date')
    return render(request, 'news/news.html', {'news': news})


def news_detail(request, slug):
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    return render(request, 'news/news_detail.html', {'post': post})







# Create your views here.
