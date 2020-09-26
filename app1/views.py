from django.http import HttpResponse
from django.shortcuts import render
from app1.models import RegistroAcesso
from .forms import FormName, ModelForm1


# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def help(request):
    return render(request, 'app1/help.html')

def sp(request):
    return render(request, 'app1/sp.html')

def calculadora(request):
    return render(request, 'app1/calculadora.html')

def acesso(request):
    lista_paginas = RegistroAcesso.objects.order_by('data')
    dict_lista2 = {"lista_acessos": lista_paginas}
    return render(request, 'app1/acesso.html', dict_lista2)

def formulario(request):
    return render(request, 'app1/formulario.html')

def form_name(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Os campos estão corretos")
            print("Nome: " + form.cleaned_data['nome'])
            print("Email: " + form.cleaned_data['email'])
            print("Texto: " + form.cleaned_data['texto'])

    return render(request, 'app1/form.html', {"form": form})


def topico_modelform(request):
    form = ModelForm1()
    return render(request, 'app1/modelform1.html', context={'modelform1': form})

def users(request):
    form = ModelForm1()

    if request.method == 'POST':
        form = ModelForm1(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERRO FORM INVALID')

    return render(request, 'app1/modelform1.html', {'form': form})
