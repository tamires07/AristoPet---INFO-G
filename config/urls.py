from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', login_view, name='login'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('buscar/', buscarView, name='buscar'),
    path('cadastraranimal/', cadastrarAnimalView, name='cadastraranimal'),
]