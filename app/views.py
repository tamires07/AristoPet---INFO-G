from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class Caracteristica_ObjetivoView(View):
    def get(self, request, *args, **kwargs):
        caracteristica_objetivo = Caracteristica_Objetivo.objects.all()
        return render(request, 'caracteristica_objetivo.html', {'caracteristica_objetivo':Caracteristica_Objetivo})
    
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoa = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoa':Pessoa})

class AgendaView(View):
    def get(self, request, *args, **kwargs):
        agenda = Agenda.objects.all()
        return render(request, 'agenda.html', {'agenda':Agenda})

class EventoView(View):
    def get(self, request, *args, **kwargs):
        evento = Evento.objects.all()
        return render(request, 'evento.html', {'evento':Evento})

class LembreteView(View):
    def get(self, request, *args, **kwargs):
        lembrete = Lembrete.objects.all()
        return render(request, 'lembrete.html', {'lembrete':Lembrete})

class Dieta_ObjetivoView(View):
    def get(self, request, *args, **kwargs):
        dieta_objetivo = Dieta_Objetivo.objects.all()
        return render(request, 'dieta_objetivo.html', {'dieta_objetivo':Dieta_Objetivo})

class Plano_AtividadeView(View):
    def get(self, request, *args, **kwargs):
        plano_atividade = Plano_Atividade.objects.all()
        return render(request, 'plano_atividade.html', {'plano_atividade':Plano_Atividade})

class ExercicioView(View):
    def get(self, request, *args, **kwargs):
        exercicio = Exercicio.objects.all()
        return render(request, 'exercicio.html', {'exercicio':Exercicio})

class Filtrar_AtividadeView(View):
    def get(self, request, *args, **kwargs):
        filtrar_atividade = Filtrar_Atividade.objects.all()
        return render(request, 'exercicio.html', {'filtrar_atividade':Filtrar_Atividade})

class ExperienciaView(View):
    def get(self, request, *args, **kwargs):
        experiencia = Experiencia.objects.all()
        return render(request, 'experiencia.html', {'experiencia':Experiencia})

class ProgressoView(View):
    def get(self, request, *args, **kwargs):
        progresso = Progresso.objects.all()
        return render(request, 'progresso.html', {'progresso':Progresso})

class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        feedback = Feedback.objects.all()
        return render(request, 'feedback.html', {'feedback':Feedback})