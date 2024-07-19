from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_validade = models.DateField()
    estoque = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.CharField(max_length=18)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=200)
    obs = models.TextField()
    
    def __str__(self):
        return self.nome

class Endereco(models.Model):
    numero = models.IntegerField()
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.rua