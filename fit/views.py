from django.shortcuts import render
from django.views.generic import View, ListView

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
