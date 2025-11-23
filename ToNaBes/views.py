from django.shortcuts import render

def index (request):
    """Página inicial do projeto ToNaBe"""
    return render(request, 'ToNaBes/index.html')
