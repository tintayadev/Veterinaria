from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CirugiaViewSet, CitaViewSet, ConsultaViewSet, DuenoViewSet,
    EspecialidadViewSet, FacturacionViewSet, HospitalizacionViewSet,
    MascotaViewSet, TratamientoViewSet, VeterinarioViewSet,
    generar_reporte_citas
)
from . import views

router = DefaultRouter()
router.register(r'cirugias', CirugiaViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'duenos', DuenoViewSet)
router.register(r'especialidades', EspecialidadViewSet)
router.register(r'facturaciones', FacturacionViewSet)
router.register(r'hospitalizaciones', HospitalizacionViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'veterinarios', VeterinarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reportes/citas/', generar_reporte_citas, name='reporte_citas'),
]
