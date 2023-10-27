from django import template
from women.models import *
from django.http import Http404
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.inclusion_tag('women/generate_menu.html', name='generate_menu')
def generate_menu():
    menu = [
        {'title': 'Про нас', 'url_for': 'about'},
        {'title': 'Наші досягнення', 'url_for': 'achivements'},
        {'title': 'Додати статтю', 'url_for': 'addpage'},
        {'title': 'Топ статтей', 'url_for': 'top_articles'},
        {'title': 'Контакти', 'url_for': 'contacts'},
    ]
    return {'menu': menu}
@register.simple_tag(name='articles_category')
def get_articles(cat_slug=0):
    if cat_slug == 0:
        articles = Women.objects.all()
    else:
        my_cats = Category.objects.filter(slug=cat_slug)
        search_id = my_cats[0].id
        articles = Women.objects.filter(cat_id=search_id)
        print(articles)
        if len(articles) == 0:
            raise Http404()
    return articles
@register.inclusion_tag('women/allcats.html', name='create_allcats', takes_context=True)
def generate_allcats(context, cat_slug=0):
    return {'cat_slug': cat_slug}

@register.simple_tag(name='cats')
def generate_cats():
    return Category.objects.all()

@register.filter(name='add_phone')
@stringfilter
def add_func(value):
    return f"This phone number is {value}"