from django.urls import path
from . import views
import os
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inscricao/', views.formulario_inscricao, name='formulario_inscricao'),
    path('sucesso/', views.inscricao_sucesso, name='inscricao_sucesso'),
    path('ranking/', views.ranking_view, name='ranking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))