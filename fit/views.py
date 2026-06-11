from django.shortcuts import render
from django.views.generic import View, ListView
from django.core.cache import cache

from fit.models import Article


# main page view
class IndexView(View):
    def get(self, request):
        return render(request, "fit/index.html", {"request": request})


# view for get articles list
class ArticlesListView(ListView):
    model = Article
    template_name = "fit/news.html"
    context_object_name = "articles"

    def get_queryset(self):
        cache_key = "news"

        # try to get cache
        news = cache.get(cache_key)
        if news:
            return news

        # get data and create cache
        news = super().get_queryset()
        cache.set(cache_key, news, 3600)
        return news
