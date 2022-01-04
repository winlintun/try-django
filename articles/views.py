from django.shortcuts import render
from .models import Article
# Create your views here.


def article_search_view(request):
    # print(request.GET)   
    query_dict = request.GET # this is a dictionary
    query = query_dict.get('q') # <input type="text" name="q">

    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        'object': article_obj,
    }
    return render(request, 'articles/search.html', context=context)


def article_home_view(request, id=None):
    article_obj = None
    if id is not None:
            article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, 'articles/detail.html', context=context)


def article_create_view(request):
    # print(request.POST)
    
    context = {}
    if request.method == "POST":
        title = request.POST.get('title')  # tuple
        content = request.POST.get('content')
        article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request, 'articles/create.html', context=context)