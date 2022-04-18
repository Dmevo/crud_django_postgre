from django.shortcuts import render
from produto.models import Produto
from produto.forms import ProdutoForm

def index(request):
    produtoForm = ProdutoForm()

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            preco = form.cleaned_data['preco']

            produto = Produto(None, nome, descricao, preco)
            produto.save()
    return render(request, "index.html", {"produtoForm":produtoForm})


# Create your views here.
