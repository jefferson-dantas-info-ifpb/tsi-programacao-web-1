from django.contrib import admin
from .models import Endereco, Produto

# Register your models here.
admin.site.register(Produto)
admin.site.register(Endereco)
