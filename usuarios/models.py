from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_cargo=(('F', 'Fornecedor'),
                   ('U', 'Usuário'))
    cargo= models.CharField(max_length=1, choices=choices_cargo)
