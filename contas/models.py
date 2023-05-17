from django.db import models
from django.template.defaultfilters import slugify

class Categoria(models.Model):
    choices_titulo = (('P','Paga'),
                      ('A', 'Atrasada'),
                      ('E','Pendente'),
    )
    titulo = models.CharField(max_length=1, choices=choices_titulo)

    def __str__(self):
        return self.titulo

class Conta(models.Model):
    nome = models.CharField(max_length=40, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    descrição = models.CharField(max_length=30)
    quantidade = models.FloatField()
    valor_pagamento = models.FloatField()
    valor_recebimento= models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self ) -> str:
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        return super().save(*args, **kwargs)



    def gerar_desconto(self, desconto):
        return self.valor_pagamento - ((self.valor_pagamento * desconto) / 100)