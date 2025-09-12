from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import LoginForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoa = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoa':pessoa})
    
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            pessoa = Pessoa.objects.get(email=email, senha=senha)
            return redirect('home')
        except Pessoa.DoesNotExist:
            messages.error(request, 'Email ou senha incorretos.')
            
    return render(request, 'login.html')

def buscar(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Animal.objects.filter(nome__icontains=query)  # busca no nome, exemplo
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})