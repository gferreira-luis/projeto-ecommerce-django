from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from . import models

# Create your views here.


class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10


class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe Produto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('AdicionarAoCarrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover Do Carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
