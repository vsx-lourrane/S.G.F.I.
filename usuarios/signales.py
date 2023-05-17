import imp
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Users)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "F":
            assign_role(instance, 'fornecedor')
        elif instance.cargo == "U":
            assign_role(instance, 'usuário')