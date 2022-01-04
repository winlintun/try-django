from django.http import HttpResponse
import random
from articles.models import Article

def home_view(request):
    random_id = random.randint(1, 4)

    # from database?
    article_obj = Article.objects.get(id=random_id) # 1 to 4 id 

    # django tameplate
    context = {
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }
    HTML_STRING = """
    <h1> {title} (id: {id}!)</h1>
    <p>{content}</p>
    """.format(**context) # more arg using (**keyword)

    return HttpResponse(HTML_STRING)