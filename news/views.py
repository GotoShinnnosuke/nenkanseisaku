from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import NewsPost
from django.views.generic import DetailView
# Create your views here.
class IndexView(ListView):
    template_name = "index.html"
    queryset = NewsPost.objects.order_by('-posted_at')
    paginate_by = 9

class DetailView(DetailView):
    template_name = 'news_detail.html'
    model = NewsPost

class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = NewsPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories
        
class Category_kokusaiView(ListView):
    template_name = 'kokusai.html'
    paginate_by = 9

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = NewsPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories
