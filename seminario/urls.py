from django.urls import path, include
from .views import listar_instituciones, InscritoViewSet, AuthorView, InscripcionView, index, InscritosListaView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inscritos', InscritoViewSet)

urlpatterns = [
    path('', index, name='index'),  # Página principal
    path('author/', AuthorView.as_view(), name='author_info'),
    path('api/', include(router.urls)),
    # seminario
    path('inscripcion/', InscripcionView.as_view(), name='inscripcion'),  # Cambiado a CBV
    path('lista_inscritos/', InscritosListaView.as_view(), name='lista_inscritos'),  # Cambiado a CBV
    path('lista_instituciones/', listar_instituciones, name='listar_instituciones'),
]
