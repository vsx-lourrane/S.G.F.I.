from curses.ascii import HT
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rolepermissions.decorators  import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_fornecedor')
def cadastrar_fornecedor(request):
    if request.method == "GET":
        fornecedores = Users.objects.filter(cargo="F")
        return render(request, 'cadastrar_fornecedor.html', {'fornecedores': fornecedores})
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        #TODO: Fazer validações dos dados
        
        user = Users.objects.filter(email=email)

        if user.exists():
            # TODO: Utilizar messages do Django
            return HttpResponse('Email já existe')

        user = Users.objects.create_user(username=email,
                                            email=email,
                                            password=senha,
                                            first_name=nome,
                                            cargo="F")

        # TODO: Redirecionar com uma mensagem
        return HttpResponse('Conta criada')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            #TODO: Redirecionar com mensagem de erro
            return HttpResponse('Usuário inválido')

        auth.login(request, user)
        return HttpResponse('Usuario logado com sucesso')

def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_fornecedor')
def excluir_usuario(request, id):
    fornecedor = get_object_or_404(Users, id=id)
    fornecedor.delete()
    messages.add_message(request, messages.SUCCESS, 'fornecedor excluid com sucesso')
    return redirect(reverse('cadastrar_fornecedor'))
