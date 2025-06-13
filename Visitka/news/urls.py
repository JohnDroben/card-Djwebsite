from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='news_index'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),

]
