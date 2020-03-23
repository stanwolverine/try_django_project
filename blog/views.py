from django.shortcuts import render, redirect
from .forms import ArticleCreateForm
from .models import Article

# Create your views here.


def create_article_view(request):
    if (request.method == 'POST'):
        article_create_form = ArticleCreateForm(request.POST or None)
        if article_create_form.is_valid():
            Article.objects.create(**article_create_form.cleaned_data)
            return redirect('article-list')
    else:
        article_create_form = ArticleCreateForm()
    context = {
        'form': article_create_form
    }
    return render(request, 'blog/article_create.html', context)


def article_list_view(request):
    article_query_set = Article.objects.all()
    context = {
        'articles': article_query_set
    }
    return render(request, 'blog/article_list.html', context)


def article_details_view(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article': article
    }
    return render(request, 'blog/article_details.html', context)
