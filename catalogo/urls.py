# IA: AttributeError 'catalogo.views' has no attribute 'home' → Solución manual: la función home no estaba guardada en catalogo/views.py; se definió y se guardó el archivo.
from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.ProductoListView.as_view(), name='lista'),
]