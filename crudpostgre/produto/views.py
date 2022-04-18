from django.shortcuts import redirect, render
from produto.models import Produto
from produto.forms import ProdutoForm

def index(request):
    produto_list = Produto.objects.all()
    return render(request, "index.html", {"produto_list":produto_list})

def adicionar_produto(request):
    produtoForm = ProdutoForm()

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            preco = form.cleaned_data['preco']

            produto = Produto(None, nome, descricao, preco)
            produto.save()
    return render(request, "form.html", {"produtoForm":produtoForm})

def excluir_produto(request, id):
    produto_list = Produto.objects.all()
    if request.method == 'DELETE':
        produto = Produto.objects.get(id=id)
        produto.delete()
    return render(request, "index.html", {"produto_list":produto_list})
        


# Create your views here.
