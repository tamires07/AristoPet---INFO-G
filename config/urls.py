from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('caracteristica_objetivo/', Caracteristica_ObjetivoView.as_view(), name='caracteristica_objetivo'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('agenda/', AgendaView.as_view(), name='agenda'),
    path('evento/', EventoView.as_view(), name='evento'),
    path('lembrete/', LembreteView.as_view(), name='lembrete'),
    path('dieta_objetivo/', Dieta_ObjetivoView.as_view(), name='dieta_objetivo'),
    path('plano_atividade/', Plano_AtividadeView.as_view(), name='plano_atividade'),
    path('exercicio/', ExercicioView.as_view(), name='exercicio'),
    path('filtrar_atividade/', Filtrar_AtividadeView.as_view(), name='filtrar_atividade'),
    path('experiencia/', ExperienciaView.as_view(), name='experiencia'),
    path('progresso/', ProgressoView.as_view(), name='progresso'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]