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
                         Evaluador)
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from rest_framework import viewsets
from .serializers import EvaluadoSerializer, EvaluadorSerializer
from .forms import *
import datetime
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


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

def enviarCorreoEvaluado(email_empresa,contraseña):
    context = {'email_empresa':email_empresa, 'contraseña': contraseña}
    template = get_template('home/correoEvaluado.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'ThinkGo',
        'Plataforma TestGo',
        settings.EMAIL_HOST_USER,
        [email_empresa]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def creaEvaluado(request):
    if request.method == 'POST':
        form = evaluadoForm(request.POST)
        email_empresa = request.POST.get('email_empresa')
        contraseña = request.POST.get('contraseña')
        enviarCorreoEvaluado(email_empresa,contraseña)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('creaEvaluado')
    else:
        form = evaluadoForm()

    return render(request, 'home/creaEvaluado.html', {'form' : form })

def enviarCorreoEvaluador(email_empresa,contraseña):
    context = {'email_empresa':email_empresa, 'contraseña': contraseña}
    template = get_template('home/correoEvaluador.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'ThinkGo',
        'Plataforma TestGo',
        settings.EMAIL_HOST_USER,
        [email_empresa]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def creaEvaluador(request):

    if request.method == 'POST':
        form = evaluadorForm(request.POST)
        email_empresa = request.POST.get('email_empresa')
        contraseña = request.POST.get('contraseña')
        enviarCorreoEvaluador(email_empresa,contraseña)

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
    revisionPendiente = EvaluacionCaso.objects.all()
    return render(request, 'home/revisionPendiente.html', {"revision" : revisionPendiente})

def actividadRealizada(request):
    actividadRealizada = EvaluacionCaso.objects.all()
    return render(request, 'home/actividadRealizada.html', {"realizada" : actividadRealizada})

def editarEvaluado(request):
    editarEvaluado = Evaluado.objects.all()
    return render(request, 'home/editarEvaluado.html', {"editarEvaluado" : editarEvaluado})

def actualizarEvaluado(request,id_evaluado):
    evaluado = Evaluado.objects.get(id_evaluado=id_evaluado)
    form = evaluadoForm(instance=evaluado)

    if request.method == 'POST':
        form = evaluadoForm(request.POST, instance=evaluado)
        email_empresa = request.POST.get('email_empresa')
        contraseña = request.POST.get('contraseña')
        enviarCorreoEvaluado(email_empresa,contraseña)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('editarEvaluado')
   
    context = {'form': form}
    return render(request, 'home/actualizarEvaluado.html',context)

def eliminarEvaluado(request, id_evaluado):
    evaluado = Evaluado.objects.get(id_evaluado=id_evaluado)
    
    if request.method == "POST": 
        evaluado.delete()
        return redirect('editarEvaluado')

    return render(request, 'home/eliminarEvaluado.html',{'evaluado':evaluado})

def editarEvaluador(request):
    editarEvaluador = Evaluador.objects.all()
    return render(request, 'home/editarEvaluador.html', {"editarEvaluador" : editarEvaluador})

def actualizarEvaluador(request,id_evaluador):
    evaluador = Evaluador.objects.get(id_evaluador=id_evaluador)
    form = evaluadorForm(instance=evaluador)

    if request.method == 'POST':
        form = evaluadorForm(request.POST, instance=evaluador)
        email_empresa = request.POST.get('email_empresa')
        contraseña = request.POST.get('contraseña')
        enviarCorreoEvaluador(email_empresa,contraseña)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('editarEvaluador')
   
    context = {'form': form}
    return render(request, 'home/actualizarEvaluador.html',context)

def eliminarEvaluador(request, id_evaluador):
    evaluador = Evaluador.objects.get(id_evaluador=id_evaluador)
    
    if request.method == "POST": 
        evaluador.delete()
        return redirect('editarEvaluador')

    return render(request, 'home/eliminarEvaluador.html',{'evaluador':evaluador})

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

def correoEvaluado(request):
    return render(request, "home/correoEvaluado.html")

def evaluacionesPendientes(request):
    evaluacion = EvaluacionCaso.objects.all()
    usuario = Evaluado.objects.all()
    return render(request, "home/evaluacionesPendientes.html",{'evaluacion':evaluacion,'usuario':usuario})

def notas(request):
    evaluacion = EvaluacionCaso.objects.all()
    usuario = Evaluado.objects.all()
    return render(request, "home/notas.html",{'evaluacion':evaluacion,'usuario':usuario})

def evaluar(request, id_evcaso):
    evalua = EvaluacionCaso.objects.get(id_evcaso=id_evcaso)
    form = evaluacionForm(instance=evalua)

    if request.method == 'POST':
        form = evaluacionForm(request.POST, instance=evalua)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Guardado Correctamente")
            return redirect('editarEvaluador')

    return render(request, 'home/eliminarEvaluador.html',{'form':form})