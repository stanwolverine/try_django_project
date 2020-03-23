from django.urls import path, include
from .views import create_article_view, article_list_view, article_details_view

urlpatterns = [
    path('', article_list_view, name='article-list'),
    path('create/', create_article_view, name='article-create'),
    path('<int:article_id>/details/',
         article_details_view, name='article-details'),
]
