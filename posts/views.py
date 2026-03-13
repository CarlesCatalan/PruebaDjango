from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post
from .forms import ComentarioForm


def listapost(request):
    posts = Post.objects.all()
    comment_form = ComentarioForm()
    return render(request, 'posts/listaposts.html', {'posts': posts, 'comment_form': comment_form})


@login_required
def comentar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentario añadido.')
        else:
            messages.error(request, 'No se pudo añadir el comentario.')
    return redirect('posts')
