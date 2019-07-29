# from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# from django.http import HttpResponse

from .models import Article


class ArticleList(generic.ListView):
    """
    Article list view class
    """
    template = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('date')


class ArticleDetail(generic.DetailView):
    """
    Article detail view class
    """
    model = Article
    template_name = 'articles/article_detail.html'


class CreateArticle(generic.edit.CreateView):
    """
    Article creation view class
    """
    template_name = 'articles/create_article.html'
    model = Article
    fields = ['title', 'slug', 'body']
    success_url = reverse_lazy('articles:list')
