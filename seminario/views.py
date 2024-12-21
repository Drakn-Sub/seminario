from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from .models import Institucion, Inscrito
from .serializers import InscritoSerializer, InstitucionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from .forms import InscritoForm

# Vista para listar instituciones (función basada en vista)
def listar_instituciones(request):
    instituciones = Institucion.objects.all()
    instituciones_data = [{"id": inst.id, "nombre": inst.nombre} for inst in instituciones]
    return JsonResponse(instituciones_data, safe=False)

# Vista de inscripción (usando formularios de Django, CBV para el modelo Inscrito)
class InscripcionView(View):
    def get(self, request):
        form = InscritoForm()
        instituciones = Institucion.objects.all()
        return render(request, 'seminario/inscripcion.html', {'form': form, 'instituciones': instituciones})

    def post(self, request):
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la lista de inscritos después de guardar
        instituciones = Institucion.objects.all()
        return render(request, 'seminario/inscripcion.html', {'form': form, 'instituciones': instituciones})

# Vista para mostrar la lista de inscritos (CBV para Inscrito)
class InscritosListaView(View):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        return render(request, 'seminario/lista_inscritos.html', {'inscritos': inscritos})

# Vista principal (index) para mostrar instituciones en la página de inicio
def index(request):
    instituciones = Institucion.objects.all()
    return render(request, 'seminario/index.html', {'instituciones': instituciones})

# Vista para la API de los inscritos usando DRF (Class Based View)
class InscritoViewSet(viewsets.ModelViewSet):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class AuthorView(APIView):
    def get(self, request):
        author_info = {
            "name": "Benjamin Aguilar",
            "email": "benjaminalex174@gmail.com",
            "github": "https://github.com/benjaminaguilar"
        }
        return Response(author_info)
