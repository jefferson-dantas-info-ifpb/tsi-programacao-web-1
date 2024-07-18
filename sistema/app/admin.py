from django.contrib import admin
from .models import Endereco, Fornecedor, Produto

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'fabricante', 'estoque', 'data_validade')

# Register your models here.
admin.site.register(Produto, ProductAdmin)
admin.site.register(Fornecedor)
admin.site.register(Endereco)
