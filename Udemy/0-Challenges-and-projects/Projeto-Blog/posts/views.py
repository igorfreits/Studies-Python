from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentarios
from django.contrib import messages

# Create your views here.


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('categoria_post')

        qs = qs.order_by('-id').filter(publicacao_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentarios__publicacao_comentario=True, then=1),

                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = (self.request.GET.get('termo'))

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(categoria_post__nome_cat__iexact=termo)

        )

        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)
        return qs


# class PostDetalhes(View):
#     template_name = 'posts/post_detalhes.html'

#     def setup(self, request, *args, **kwargs):
#         super().setup(request, *args, **kwargs)

#         pk = self.kwargs.get('pk')
#         post = get_object_or_404(Post, pk=pk, publicacao_post=True)
#         self.contexto = {
#             'post': post,
#             'comentarios': Comentarios.objects.filter(
#                 post_comentario=post,
#                 publicacao_comentario=True),
#             'form': FormComentario(request.POST or None),
#         }

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, self.contexto)

#     def post(self, request, *args, **kwargs):
#         form = self.contexto['form']
#         if not form.is_valid():
#             return render(request, self.template_name, self.contexto)
#         comentario = form.save(commit=False)
#         if request.user.is_authenticated:
#             comentario = usuario_comentario = request.user
#         comentario.post_comentario = self.contexto('post')
#         comentario.save()
#         messages.success(self.request, 'Comentário enviado com sucesso!')
#         return redirect('post_detalhes', pk=self.contexto('post').id)

class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentarios.objects.filter(
            publicacao_comentario=True, post_comentario=post.id)
        contexto['comentarios'] = comentarios

        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentarioz = Comentarios(**form.cleaned_data)
        comentarioz.post_comentario = post

        if self.request.user.is_authenticated:
            comentarioz.usuario_comentario = self.request.user

        comentarioz.save()
        messages.success(self.request, 'Comentário enviado com sucesso!')
        return redirect('post_detalhes', pk=post.id)
