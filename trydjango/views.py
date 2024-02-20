"""
To render html web pages
"""
import random

from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def article_home_view(request):
    return HttpResponse()

def home_view(request, id=None, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response(We pict to return the response)
    """

    print("request:",request)
    # name = "Ely"
    # number = random.randint(1, 4) # API call to some rest API with python & python requests
    # article_obj = Article.objects.get(id=number)
    # article_obj = Article.objects.get(id=1)
    article_queryset = Article.objects.all()
    
    # context = {
    #     "object_list": article_queryset,
    #     "object": article_obj,
    #     "title": article_obj.title,
    #     "id": article_obj.id,
    #     "content": article_obj.content,
    # }
    context = {
        "object_list": article_queryset,
    }

    # print("HOME_VIEW_CONTEXT:", context)
    # Django Templates
    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)
    # tmpl_string2 = tmpl.render(context=context2)
    # tmpl_string3 = tmpl.render(context=context3)

    HTML_STRING = render_to_string(
        "home-view.html",
        context=context
    )

    # HTML_STRING = """
    # <h1>{title} id: ({id})</h1>
    # <p>{content}</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)

def login_view(request):
    HTML_STRING = """
    <h1>Login</h1>
    <label>Username</label>
    <label>Password</label>
    """
    return HttpResponse(HTML_STRING)