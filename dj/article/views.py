from django.shortcuts import render, redirect
from article.models import Article, Tag
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed
from django.contrib.auth import authenticate, login, logout
from article.forms import UserForm, ArticleForm
# Create your views here.


def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'article/home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        tags = Tag.objects.all()
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'article/detail.html', {'post': post, 'tags': tags})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'article/archives.html', {'post_list': post_list,
                                                     'error': False})


def aboutme(request):
    return render(request, 'article/aboutme.html')


def tag_search(request, tag):
    try:
        post_list = Article.objects.filter(tag__iexact=tag)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'article/tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'article/home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'article/archives.html', {"post_list": post_list,
                                                                 'error': True})
            else:
                return render(request, 'article/archives.html', {"post_list": post_list,
                                                                'error': False})

    return HttpResponseRedirect("/")


class RSSFeed(Feed):
    title = "RSS Feed - article"
    link =  "feeds/posts/"
    description = "RSS Feed - blog posts"

    def items(self):
        return Article.objects.order_by('date_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.date_time


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("Your account is unaccessable")
        else:
            return HttpResponse("Invalid login details")
    else:
        user = authenticate()
        return render(request, 'article/login.html', {'user': user})


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserForm()

    return render(request, 'article/register.html', {'form':form})


@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            #arti.content = form.content
            return detail(request, post.id)
    else:
        form = ArticleForm()
    return render(request, 'article/add_article.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
