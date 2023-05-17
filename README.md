# admin

# O.S.G.I.
Sistema de Gestão ultilizando a framework Django. Projeto realizado com ajuda do Python, HTML, CSS.
O objetivo deste foi criar um sistema financeiro simplificado que poderia ser usado internamente para gerenciar processos financeiros internos.
Instalação:
Sobre o processo de instalação será listado o passo a passo do inicio do projeto:
-Baixar o IDE escolhido( Visual Studio Code),
link:https://code.visualstudio.com/
-Baixar a linguagem Python,
link:https://www.python.org/downloads/
-Confirmando a instalação no Prompt de Comando.
O segundo passo das instalações requer as dependências:
-python.exe -m pip install --upgrade pip
-pip install virtualenv venv
-pip install Django
-pip freeze > requirements.txt
-type requirements.txt
O terceiro passo é ativar as dependências por meio :
-Scripts>activate
-Virtualenv venv
-manage.py
-python manage.py makemigratios
-python manage.py migrate
-python manage.py runserver
Implementações:
Cadastro de produtos, clientes, empresas, fornecedores e transportadoras
Login/Logout
Definição de permissões para usuários.
Portanto, também foi adicionado recursos existentes na propria framework como formulários, autenticação de usuários, sistema criptografado de segurança, sistema de administrador e suas respectivas configurações.
