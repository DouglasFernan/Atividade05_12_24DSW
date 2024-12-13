from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.CoreListView.as_view(), name="listar_produtos"),
    path("edit/<int:pk>/",  views.ProdutoUpdate.as_view(), name='editar_produtos'),
]
