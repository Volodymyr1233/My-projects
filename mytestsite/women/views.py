from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import AddPostForm
# Create your views here.


categories = ['Акторки', 'Співачки', 'Моделі']
test_quer = Test_table.objects.all()

def show_art(request, cat_slug):
    print(cat_slug)
    return render(request, 'women/index.html', {'cat_slug': cat_slug, 'ident': 1})

def my_sales_women(request):
    return render(request, 'women/index.html', {'cat_slug': 0, 'ident': 1})

def show_more_arts(request, post_slug):
    post_res = get_object_or_404(Women, slug=post_slug)
    context = {
        'post_res': post_res,
        'cat_slug': post_res.slug,
    }
    return render(request, 'women/show_more_arts.html', context)
def addpage(request):
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                #return redirect('main')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form})




def test_temp(request):
    context = {
        'test_base': 'test_base',
        'text': '<h4>Junk food</h4>',
        'test_quer': test_quer,
    }
    return render(request, 'women/base.html',  context)

def test_func(request, name, age):
    res = Test_table.objects.filter(name=name)
    context = {
        'test_test': 'test_test',
        'name': name,
        'age': age,
        'test_quer': test_quer,
        'res': res
    }
    return render(request, 'women/test.html', context)

def pass_func(request):
    return HttpResponse('Welcome page')

def page_not_found(request, exception):
    return HttpResponseNotFound("ERROR.....")



