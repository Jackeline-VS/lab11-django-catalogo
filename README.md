# TechStore – Catálogo de productos con Django

Práctica de laboratorio **Semana 11** del curso **Desarrollo de Aplicaciones Web (IS093A)**
Universidad Nacional del Centro del Perú – Facultad de Ingeniería de Sistemas

**Autora:** Jackeline Vivanco Solano

---

## Descripción

Aplicación web construida con **Django 5.2** que aplica el patrón **MTV (Model-Template-View)**.
Muestra un catálogo de productos electrónicos almacenados en **SQLite** y permite filtrarlos por categoría.

La práctica cubre:

- Enrutamiento con `urls.py`, `include()` y rutas con nombre (`name`).
- Vistas basadas en función (**FBV**) y en clase (**CBV – `ListView`**).
- Plantillas con herencia (`{% extends %}`), bloques, etiquetas (`for`, `if`, `empty`, `url`) y filtros (`title`, `date`).
- Modelos con el **ORM** de Django, migraciones y consultas (`all()`, `filter()`).

## Tecnologías

| Herramienta | Versión |
|---|---|
| Python | 3.13 |
| Django | 5.2.19 |
| Base de datos | SQLite |
| Estilos | Bootstrap 5.3 (CDN) |

## Estructura del proyecto

```
SEMANA 11/
├── manage.py
├── requirements.txt
├── tienda/                     # Proyecto (configuración)
│   ├── settings.py
│   └── urls.py                 # Incluye las rutas de la app
└── catalogo/                   # App
    ├── models.py               # Modelo Producto
    ├── views.py                # FBV home + CBV ProductoListView
    ├── urls.py                 # Rutas de la app (app_name = 'catalogo')
    ├── migrations/
    │   └── 0001_initial.py
    └── templates/
        └── catalogo/
            ├── base.html       # Plantilla padre (bloques, navbar, footer)
            ├── home.html       # Página de inicio
            └── catalogo.html   # Listado de productos
```

## Instalación y ejecución (Windows)

```powershell
# 1. Clonar el repositorio
git clone https://github.com/Jackeline-VS/lab11-django-catalogo.git
cd lab11-django-catalogo

# 2. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar y crear la base de datos
python manage.py check
python manage.py migrate

# 5. Levantar el servidor
python manage.py runserver
```

Abrir en el navegador: <http://127.0.0.1:8000/>

> `db.sqlite3` no se incluye en el repositorio. Después de `migrate` la base está vacía; para cargar datos de prueba, ver la siguiente sección.

### Datos de prueba

```powershell
python manage.py shell
```

```python
from catalogo.models import Producto

Producto.objects.create(nombre="laptop lenovo ideapad", categoria="laptops", precio=2499.90, stock=5)
Producto.objects.create(nombre="laptop hp pavilion", categoria="laptops", precio=3199.00, stock=0)
Producto.objects.create(nombre="samsung galaxy a55", categoria="celulares", precio=1399.00, stock=8)
Producto.objects.create(nombre="iphone 15", categoria="celulares", precio=3899.00, stock=2)
Producto.objects.create(nombre="audifonos sony", categoria="accesorios", precio=299.90, stock=0)
Producto.objects.create(nombre="mouse logitech", categoria="accesorios", precio=89.90, stock=15)

# Consultas con el ORM
Producto.objects.all()
Producto.objects.filter(categoria="laptops")
Producto.objects.filter(precio__lt=1000)
Producto.objects.filter(stock=0)
exit()
```

## Rutas

| URL | Nombre | Vista | Tipo |
|---|---|---|---|
| `/` | `catalogo:home` | `home` | FBV |
| `/productos/` | `catalogo:lista` | `ProductoListView` | CBV (`ListView`) |
| `/productos/?categoria=laptops` | `catalogo:lista` | `ProductoListView` | Filtro por categoría |
| `/admin/` | – | Admin de Django | – |

## Modelo `Producto`

| Campo | Tipo | Detalle |
|---|---|---|
| `nombre` | `CharField(100)` | Nombre del producto |
| `categoria` | `CharField(20)` | `laptops`, `celulares`, `accesorios` (choices) |
| `precio` | `DecimalField(8, 2)` | Precio en soles |
| `stock` | `PositiveIntegerField` | Unidades disponibles (0 = agotado) |
| `fecha_registro` | `DateTimeField` | Se asigna automáticamente (`auto_now_add`) |

Incluye `__str__` y `Meta.ordering = ['nombre']`.

## Funcionalidades

- **Inicio (FBV):** muestra el total de productos y cuántos están agotados, usando `count()` y `filter()`.
- **Catálogo (CBV):** lista los productos en tarjetas de Bootstrap.
  - `get_queryset()` filtra por categoría según el parámetro `?categoria=` de la URL.
  - `get_context_data()` agrega al contexto las categorías y la categoría seleccionada.
- **Plantillas:**
  - `{% extends %}` y bloques `titulo` / `contenido`.
  - `{% for %}` con `{% empty %}` para el listado.
  - `{% if %}` para mostrar "Stock" o "Agotado".
  - Filtros `title` (nombre) y `date:"d/m/Y H:i"` (fecha de registro).
  - Todas las URLs se generan con `{% url %}`; no hay rutas escritas a mano.

## Uso controlado de IA

Según la regla de laboratorio, los errores resueltos con ayuda de IA están documentados en el código:

| Archivo | Problema | Solución manual |
|---|---|---|
| `catalogo/urls.py` | `AttributeError: module 'catalogo.views' has no attribute 'home'` | La función `home` no estaba guardada en `views.py`; se definió y se guardó el archivo. |
| `catalogo/templates/catalogo/catalogo.html` | `TemplateSyntaxError` (`endblock` / `else` inválidos) | La extensión Prettier partía las etiquetas `{% %}` en varias líneas al guardar; se desactivó en el workspace y se reescribieron las plantillas. |

## Historial de commits

1. Inicio del proyecto: `.gitignore`
2. Paso 1: entorno virtual, Django 5.2, proyecto `tienda` y app `catalogo`
3. Paso 2: rutas de la app con `include()` y `name`
4. Paso 5: modelo `Producto`, migraciones y consultas ORM
5. Pasos 3 y 4: vistas FBV/ListView y plantillas con herencia, tags y filtros
6. Notas de uso de IA
