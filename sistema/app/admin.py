from django.contrib import admin
from .models import Endereco, Fornecedor, Produto

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'fabricante', 'estoque', 'data_validade')

class FornecedorAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'endereco', 'id')

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'rua', 'bairro')

# Register your models here.
admin.site.register(Produto, ProductAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Endereco, EnderecoAdmin)
