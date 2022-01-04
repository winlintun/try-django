from django.http import HttpResponse
import random
from articles.models import Article

def home_view(request):
    random_id = random.randint(1, 4)

    # from database?
    article_obj = Article.objects.get(id=random_id) # 1 to 4 id 

    # django tameplate
    H1_STRING = f"""
    <h1> {article_obj.title} (id: {article_obj.id}!)
    """

    P_STRING = f"""
    <p>{article_obj.content}</p>
    """

    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)