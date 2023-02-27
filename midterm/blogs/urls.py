from django.urls import path
from . import views

urlpatterns = [
    path('api/blogs', views.blog_list, name='blog-list'),
    path('api/blogs/<int:id>', views.blog_detail, name='blog-detail'),
]