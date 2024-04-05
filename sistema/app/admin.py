from django.contrib import admin
from .models import Endereco, Fornecedor, Produto

# Register your models here.
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(Endereco)
