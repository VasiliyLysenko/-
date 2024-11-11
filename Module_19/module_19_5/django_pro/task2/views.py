from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    elements_in_page = request.GET.get('elements_in_page', 3)
    paginator = Paginator(posts, per_page=elements_in_page)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'page_posts': page_posts,
        'elements_in_page': elements_in_page
    }
    return render(request, 'pagination.html', context)