from django.shortcuts import render

def index(request):
    receitas = {
        1:'Lasanha',
        2:'Sopa de legumes',
        3:'Sorvete',
    }
    
    dados = {
        'nome_das_receitas' :
    }
    return render(request, 'index.html')

def receita(request):
    return render(request, 'receita.html')