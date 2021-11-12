from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import EvaluadoViewset, EvaluadorSerializer, EvaluadorViewset

router = routers.DefaultRouter()
router.register('Evaluado', EvaluadoViewset)
router.register('Evaluador', EvaluadorViewset)

urlpatterns = [
    #------Usuario-------
    path('login/', views.inicio, name='login'),
    path('loginA/', views.loginA, name='loginA'),
    path('loginE/', views.loginE, name='loginE'),
    path('index/', views.index, name='index'),
    path('caso1/', views.caso1, name="caso1"),
    path('caso2/', views.caso2, name="caso2"),
    path('vistaA/', views.vistaA, name='vistaA'),
    path('vistaE/', views.vistaE, name='vistaE'),
    path('prueba/', views.prueba, name='prueba'),
    path('', views.perfil, name="perfil"),
    path('seleccion/', views.seleccion, name='seleccion'),
    path('video/', views.video, name='video'),
    path('foto/', views.foto, name='foto'),
    path('cuestionario/', views.cuestionario, name='cuestionario'),
    path('final/', views.final, name='final'),
    path('creaEvaluado/', views.creaEvaluado, name='creaEvaluado'),
    path('creaEvaluador/', views.creaEvaluador, name='creaEvaluador'),
    path('creaActividad/', views.creaActividad, name='creaActividad'),
    path('asignarEvaluacion/', views.asignarEvaluacion, name='asignarEvaluacion'),
    path('actividadPendiente/', views.actividadPendiente, name='actividadPendiente'),
    path('revisionPendiente/', views.revisionPendiente, name='revisionPendiente'),
    path('actividadRealizada/', views.actividadRealizada, name='actividadRealizada'),
    path('api/', include(router.urls)),
    path('probar_rut/', views.probar_rut, name='probar_rut'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)