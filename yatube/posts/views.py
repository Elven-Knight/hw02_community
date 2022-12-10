from django.shortcuts import render, get_object_or_404
from .models import Post, Group


COUNT_POSTS = 10


def index(request):
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    # (от больших значений к меньшим)
    posts = Post.objects.all()[:COUNT_POSTS]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': "Последние обновления на сайте"
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:COUNT_POSTS]
    context = {
        'group': group,
        'posts': posts,
        'title': group.title,
        'main_header': "Лев Толстой – зеркало русской революции."
    }
    return render(request, 'posts/group_list.html', context)
