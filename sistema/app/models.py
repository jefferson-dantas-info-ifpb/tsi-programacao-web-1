from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    numero = models.IntegerField()
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.rua