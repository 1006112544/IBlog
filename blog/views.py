from django.shortcuts import render, render_to_response, HttpResponseRedirect
from blog.models import *
from django import forms
from django.contrib.auth.models import User
# Create your views here.


class LoginForm(forms.Form):
    email = forms.CharField(label="email", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput)


def login(requset):
    if ('email' or 'password') not in requset.GET:
        lf = LoginForm()
        return render_to_response('login.html', {'lf': lf})
    lf = LoginForm(requset.GET)
    email = lf.data['email']
    password = lf.data['password']
    try:
        user = User.objects.get(email=email)
        pass
    except User.DoesNotExist:
        pass
    else:
        if user.check_password(password):
            return HttpResponseRedirect("/")  # 重定向
    return HttpResponseRedirect("/login/")  # 重定向


def index(requset):
    articles = Article.objects.all()  # 读取数据库中的所有文章
    return render(requset, 'index.html', locals())


def article(requset, pid):
    article = Article.objects.get(id=pid)  # 根据id读取数据库中的文章
    return render(requset, 'article.html', locals())
