from django.shortcuts import render
from .forms import ContaForm
from .models import Categoria, Conta
from django.http import HttpResponse
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from rolepermissions.decorators  import has_permission_decorator

@has_permission_decorator('cadastrar_conta')
def add_conta(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        descrição=request.GET.get('descrição')
        categoria = request.GET.get('categoria')
        preco_min = request.GET.get('preco_min')
        preco_max = request.GET.get('preco_max')
        contas = Conta.objects.all()

        if nome or categoria or preco_min or preco_max:
            
            if not preco_min:
                preco_min = 1

            if not preco_max:
                preco_max = 999

            if nome:
                contas = contas.filter(nome__icontains=nome)

            if categoria:
                contas = contas.filter(categoria=categoria)

            categorias = Categoria.objects.all()       
        return render(request, 'add_conta.html', {'categorias': categorias, 'contas': contas})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        descrição = request.POST.get('descrição')
        valor_pagamento = request.POST.get('valor_pagamento')
        valor_recebimento = request.POST.get('valor_recebimento')

        conta = Conta(nome=nome,
                      categoria_id=categoria,
                      quantidade=quantidade,
                      valor_pagamento=valor_pagamento,
                      valor_recebimento=valor_recebimento)
        
        conta.save()
        messages.add_message(request, messages.SUCCESS, 'Conta cadastrada com sucesso')
        return redirect(reverse('add_conta'))

def Conta(request, slug):
    if request.method == "GET":
        conta = Conta.objects.get(slug=slug)
        data = conta.__dict__
        data['categoria'] = conta.categoria.id
        form = ContaForm(initial=data)
        return render(request, 'conta.html', {'form': form})