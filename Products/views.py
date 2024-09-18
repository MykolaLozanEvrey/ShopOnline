from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render


from .models import *

menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Акціі", 'url_name': 'promotion'},
        {'title': "Кошик", 'url_name': 'cart'},
        {'title': "Увійти", 'url_name': 'login'}
        ]

class ProductHome(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'posts'


    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Головна сторінка'

        return context
    
# def index(request):
#     posts = Product.objects.all()
#     cats = Category.objects.all()
#     context = {'posts': posts,
#                'cats': cats,
#                'menu': menu,
#                'title': 'Головна сторінка',
#                'cat_selected': 0,
#     }
    
#     return render(request, 'products/index.html', context=context)

def about(request):
    return render(request, 'products/about.html', {'menu': menu,'title': 'Про сайт'})

def promotion(request):
    return HttpResponse("Акції")

def cart(request):
    return HttpResponse("Кошик")

def login(request):
    return HttpResponse("Авторизація")

def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)
    
    context = {'post': post,
            'menu': menu,
            'title': post.name,
            'cat_selected': post_slug,
}
    return render(request, 'products/post.html', context=context)

class ProductCategory(ListView):
    model = Product
    template_name = "products/index.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Product.objects.filter(cat__slug=self.kwargs['cat_slug'])
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категорія - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = Product.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#     context = {'posts': posts,
#                'cats': cats,
#                'menu': menu,
#                'title': 'Відображення по категоріям',
#                'cat_selected': cat_id,
#     }
    
#     return render(request, 'products/index.html', context=context)

# def models_not_in_products(request, model):
#     if str(model) not in products:
#         return redirect('home,', permanent=False)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена (<h1>')