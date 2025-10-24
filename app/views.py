from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .forms import *
from .models import Animal

class IndexView(View):
    def get(self, request, *args, **kwargs):
        animais = Animal.objects.all()  # pega todos os animais do banco
        return render(request, 'index.html', {'animais': animais})


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

def buscarView(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Animal.objects.filter(nome__icontains=query)  # busca no nome, exemplo
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})


def cadastrarAnimalView(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            # Aqui você define o doador (ex: o usuário logado)
            # animal.doador = request.user.pessoa  # se estiver usando autenticação com Pessoa
            animal.doador = Pessoa.objects.first() # temporário para teste
            animal.save()
            messages.success(request, 'Animal cadastrado com sucesso!')
            return redirect('index')  # ou outra rota
        else:
            messages.error(request, 'Erro no formulário. Verifique os dados.')
    else:
        form = AnimalForm()
    return render(request, 'cadastraranimal.html', {'form': form})


def deletarAnimalView(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    messages.success(request, 'Animal deletado com sucesso!')
    return redirect('index')
