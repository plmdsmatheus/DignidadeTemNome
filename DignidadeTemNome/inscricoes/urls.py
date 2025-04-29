from django.urls import path
from . import views

urlpatterns = [
    path('inscricao/', views.formulario_inscricao, name='formulario_inscricao'),
    path('sucesso/', views.inscricao_sucesso, name='inscricao_sucesso'),
    path('ranking/', views.ranking_view, name='ranking'),
]
