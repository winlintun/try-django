from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string


# MTV System (model / template / view)
def home_view(request):
    random_id = random.randint(1, 4)

    # from database?
    article_obj = Article.objects.get(id=random_id) # 1 to 4 id 
    article_query = Article.objects.all()

    # my_list = [123, 345, 566, 1112]
    # django tameplate
    context = {
        'obj_list': article_query,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }

    HTML_STRING = render_to_string('home-view.html', context=context)
    # HTML_STRING = """
    # <h1> {title} (id: {id}!)</h1>
    # <p>{content}</p>
    # """.format(**context) # more arg using (**keyword)

    return HttpResponse(HTML_STRING)