from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from django.core.paginator import Paginator

count = 3


def index(request):
    global count
    posts = Post.objects.all()
    paginator = Paginator(posts, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)


def new_count(request):
    global count
    count = int(request.POST['count'])
    return HttpResponseRedirect('/')