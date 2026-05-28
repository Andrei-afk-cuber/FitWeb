from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from fit.models import Article


# main page view
class IndexView(TemplateView):
    template_name = 'fit/index.html'

# view for get articles list
class ArticlesListView(ListView):
    model = Article
    template_name = 'fit/news.html'
    context_object_name = 'articles'