from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('news/<int:category>',
         views.CategoryView.as_view(),
         name = 'news_cat'),
    path('news-detail/<int:pk>',
         views.DetailView.as_view(),
         name='news_detail')
]