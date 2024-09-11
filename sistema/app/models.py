from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_validade = models.DateField(null=True, blank=True)
    estoque = models.IntegerField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua =  models.CharField(max_length=100)
    bairro =  models.CharField(max_length=100)
    numero =  models.IntegerField()
    cidade =  models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return self.rua

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.nome
