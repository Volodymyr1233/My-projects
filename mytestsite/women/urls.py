from django.urls import path, register_converter, re_path
from .views import *

urlpatterns = [
    path('', my_sales_women, name='main'),
    path('about/', pass_func, name='about'),
    path('achivements/', pass_func, name='achivements'),
    path('top_articles/', pass_func, name='top_articles'),
    path('contacts/', pass_func, name='contacts'),
    path('addpage/', pass_func, name='addpage'),
    path('category/<slug:cat_slug>', show_art, name='category'),
    path('post/<slug:post_slug>/', show_more_arts, name='post'),
    re_path(r'test/(?P<name>[A-Z, a-z]+)/(?P<age>[0-9]+)/', test_func, name='test'),
]
