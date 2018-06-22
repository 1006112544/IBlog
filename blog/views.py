from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
# Create your views here.


# def hello(request):
#     return HttpResponse("这是一个未完成的网站")

def index(requset):
    articles = Article.objects.all()  # 读取数据库中的所有文章
    return render(requset, 'index.html', locals())


def article(requset, pid):
    article = Article.objects.get(id=pid)  # 根据id读取数据库中的文章
    return render(requset, 'article.html', locals())
