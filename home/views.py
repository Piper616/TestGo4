from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render, redirect
from .models import (Administrador,
                          AudAdmin,
                          AudCargo,
                          AudCasos,
                       AudEvaluado,
                      AudEvaluador,
                             Cargo,
                             Casos,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador,
                         Resultado)
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from rest_framework import viewsets
from .serializers import EvaluadoSerializer, EvaluadorSerializer
from .forms import *
import datetime


# Create your views here.
def inicio(request):
    if request.method == "POST":
        try:
         detalleUsuario=Evaluado.objects.get(email_empresa=request.POST['correo'], contraseña=request.POST['password'])
         print("usuario=", detalleUsuario)
         request.session['email']=detalleUsuario.email_empresa
         return render(request, 'home/index.html')
        except Evaluado.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicio.html')

def loginA(request):
    if request.method == "POST":
        try:
         detalleAdmin=Administrador.objects.get(email_empresa=request.POST['correoA'], contraseña=request.POST['passwordA'])
         print("usuario=", detalleAdmin)
         request.session['email']=detalleAdmin.email_empresa
         return render(request, 'home/vistaA.html')
        except Administrador.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicioA.html')

def loginE(request):
    if request.method == "POST":
        try:
         detalleEvaluador=Evaluador.objects.get(email_empresa=request.POST['correoE'], contraseña=request.POST['passwordE'])
         print("usuario=", detalleEvaluador)
         request.session['email']=detalleEvaluador.email_empresa
         return render(request, 'home/vistaE.html')
        except Evaluador.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicioE.html')    

def caso(request):
    if request.method == "POST":
        try:
         vistocaso=Casos.objects.get(pdf=request.POST['caso1'])
         print("usuario=", vistocaso)
         request['caso1']=vistocaso.pdf
         return render(request, 'home/index.html')
        except Evaluador.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o contraseña no es correcto..!')
    return render(request, 'home/inicioE.html') 

def pdf2(request):
    pdf2=Casos.objects.all()
    return render(request, 'home/caso1.html', {"pdf":pdf2})

def entry(request):
    if request.method == 'POST':
        form = SubirvideoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = SubirvideoForm()

    return render(request, "caso1.html", {
        "form": form
    })

def seleccion(request):
    return render(request,'home/seleccion.html')

def vistaA(request):
    return render(request,'home/vistaA.html')

def index(request):
    return render(request,'home/index.html')

def caso1(request):
    return render(request, 'home/caso1.html')

def caso2(request):
    return render(request, "home/caso2.html")

def perfil(request):
    return render(request, "home/perfil.html")

def vistaE(request):
    return render (request, "home/vistaE.html")

def video(request):
    return render(request,'home/video.html')

def foto(request):
    return render(request,'home/foto.html')

def cuestionario(request):
    return render(request,'home/cuestionario.html')

def final(request):
    return render(request, 'home/final.html')

def creaEvaluado(request):

    if request.method == 'POST':
        form = evaluadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('creaEvaluado')
    else:
        form = evaluadoForm()

    return render(request, 'home/creaEvaluado.html', {'form' : form})

def creaEvaluador(request):

    if request.method == 'POST':
        form = evaluadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('CreaEvaluador')
    else:
        form = evaluadorForm()

    return render(request, 'home/creaEvaluador.html',{'form':form})

def creaActividad(request):

    if request.method == 'POST':
        form = actividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('CreaActividad')
    else:
        form = actividadForm()

    return render(request, 'home/creaActividad.html',{'form':form})

def asignarEvaluacion(request):

    if request.method == 'POST':
        form = asignarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('asignarEvaluacion')
    else:
        form = asignarForm()

    fecha_actual = "{0}".format(datetime.datetime.now().strftime("%d/%m/%Y"))

    return render(request, 'home/asignarEvaluacion.html',{'form':form,"fecha_actual":fecha_actual})

def fecha_hoy(request):
    fecha_actual = "{0}".format(datetime.datetime.now().strftime("%d/%m/%Y"))
    return render(request,'TestGo/home/forms.py',{"fecha_actual":fecha_actual})

def actividadPendiente(request):
    actividadPendiente = EvaluacionCaso.objects.all()
    return render(request, 'home/actividadPendiente.html', {"pendiente" : actividadPendiente})

def revisionPendiente(request):
    revisionPendiente = Resultado.objects.all()
    return render(request, 'home/revisionPendiente.html', {"revision" : revisionPendiente})

def actividadRealizada(request):
    actividadRealizada = Resultado.objects.all()
    return render(request, 'home/actividadRealizada.html', {"realizada" : actividadRealizada})

class EvaluadoViewset(viewsets.ModelViewSet):
    queryset = Evaluado.objects.all()
    serializer_class = EvaluadoSerializer

class EvaluadorViewset(viewsets.ModelViewSet):
    queryset = Evaluador.objects.all()
    serializer_class = EvaluadorSerializer

def prueba(request):
    return render(request, "home/prueba.html")

def probar_rut(request):
    return render(request, "home/probar_rut.html")