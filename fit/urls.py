from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("news/", views.ArticlesListView.as_view(), name="news-page"),
]
