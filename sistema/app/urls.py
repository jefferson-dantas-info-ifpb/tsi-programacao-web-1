from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("preco", views.preco, name="preco"),
    path("pesquisar", views.pesquisar, name="pesquisar"),
    path("cadastrar", views.cadastrar, name="cadastrar"),
    path("deletar", views.deletar, name="deletar"),
    path("atualizar", views.atualizar, name="atualizar"),
    ###########################################################
    path("exact", views.exact, name="exact"),
    path("iexact", views.iexact, name="iexact"),
    path("contains", views.contains, name="contains"),
    path("icontains", views.icontains, name="icontains"),
    path("inn", views.inn, name="inn"),
    path("gt", views.gt, name="gt"),
    path("gte", views.gte, name="gte"),
    path("lt", views.lt, name="lt"),
    path("lte", views.lte, name="lte"),
    path("startswith", views.startswith, name="startswith"),
    path("istartswith", views.istartswith, name="istartswith"),
    path("endswith", views.endswith, name="endswith"),
    path("iendswith", views.iendswith, name="iendswith"),
]
