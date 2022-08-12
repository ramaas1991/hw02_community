from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render


from .models import Group, Post


User = get_user_model()
Pub_limit = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:Pub_limit]
    title = 'заголовок'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().order_by('-pub_date')[:Pub_limit]
    title = 'заголовок'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
