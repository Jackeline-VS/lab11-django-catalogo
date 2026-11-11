from django.http import HttpResponse

def home(request):
    return HttpResponse("Inicio funcionando")

def catalogo(request):
    return HttpResponse("Catálogo funcionando")