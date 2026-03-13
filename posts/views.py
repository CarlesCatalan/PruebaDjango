from django.shortcuts import render

from .models import Post


def listapost(request):
    posts = Post.objects.all()
    return render(request, 'posts/listaposts.html', {'posts': posts})
