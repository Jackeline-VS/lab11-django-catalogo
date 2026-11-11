from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# FBV: vista basada en función
def home(request):
    contexto = {
        'total': Producto.objects.count(),
        'agotados': Producto.objects.filter(stock=0).count(),
    }
    return render(request, 'catalogo/home.html', contexto)


# CBV: vista basada en clase
class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        if categoria:
            qs = qs.filter(categoria=categoria)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Producto.CATEGORIAS
        context['categoria_actual'] = self.request.GET.get('categoria', '')
        return context