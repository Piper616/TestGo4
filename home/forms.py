from typing import Pattern
from django import forms
from django.core.exceptions import ViewDoesNotExist
from django.db.models import fields
from django.forms import widgets

from .views import *
import datetime
from django.forms import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class evaluadoForm(forms.ModelForm):

    def clean_rut(self, rut):
        rut = self.cleaned_data["rut_evaluador"]
        existe = Evaluador.objects.filter(rut_evaluador=rut).exists()

        if existe:
            raise ValidationError("Este rut ya existe")

        return rut

    id_evaluado = forms.CharField(label='Id', widget = forms.TextInput(attrs={"placeholder":"Ingrese Id"}))
    rut_evaluado = forms.CharField(label='Rut Evaluado', widget = forms.TextInput(attrs={"placeholder":"ej: 11.111.111-1", "id":"rut"}))
    nombres = forms.CharField(label='Nombre/s', widget = forms.TextInput(attrs={"placeholder":"Ingrese Nombre/s del evaluado"}))
    apellido_p = forms.CharField(label='Apellido Paterno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido paterno"}))
    apellido_m = forms.CharField(label='Apellido Materno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido materno"}))
    num_cel = forms.CharField(label='Número de celular', widget = forms.TextInput(attrs={"placeholder":"Ej: 9 999 99 999"}))
    email_personal = forms.CharField(label='Email Personal', widget = forms.TextInput(attrs={"placeholder":"ej: persona@personal.com"}))
    empresa = forms.CharField(label='Empresa perteneciente', widget = forms.TextInput(attrs={"placeholder":"Ingrese empresa del evaluado"}))
    email_empresa = forms.CharField(label='Email contacto empresa', widget = forms.TextInput(attrs= {"placeholder":"ej: persona@empresa.cl"}))
    contraseña = forms.CharField(label='Contraseña', widget = forms.TextInput(attrs={"placeholder":"Ingrese contraseña para ingreso"}))
    nombre_jefe = forms.CharField(label='Nombre del Jefe', widget = forms.TextInput(attrs={"placeholder":"Ingrese nombre del jefe"})) 
    cel_jefe = forms.CharField(label='Celular del Jefe', widget = forms.TextInput(attrs={"placeholder":"Ingrese celular del jefe"}))
    email_jefe = forms.CharField(label='Email del Jefe', widget = forms.TextInput(attrs={"placeholder":"ej: jefe@empresa.cl"}))

    class Meta:
        model = Evaluado

        fields =[
            'id_evaluado', 
            'rut_evaluado',
            'nombres',
            'apellido_p',
            'apellido_m',
            'num_cel',
            'email_personal',
            'empresa',
            'email_empresa',
            'contraseña',
            'cargo_id_cargo',
            'nombre_jefe',
            'cel_jefe',
            'email_jefe'
        ]

        labels = {
            'cargo_id_cargo':'Cargo'
        }

        widgets = {
            'cargo_id_cargo': forms.Select(attrs={'class':'form-control'})
        }
    
class evaluadorForm(forms.ModelForm):
   
    def clean_rut(self, rut):
        rut = self.cleaned_data["rut_evaluador"]
        existe = Evaluador.objects.filter(rut_evaluador=rut).exists()

        if existe:
            raise ValidationError("Este rut ya existe")

        return rut

    id_evaluador = forms.CharField(label='Identificación', widget = forms.TextInput(attrs={"placeholder":"Ingrese Id"}))
    rut_evaluador = forms.CharField(label='Rut', widget = forms.TextInput(attrs={"placeholder":"ej: 11.111.111-1","id":"rut"}))
    nombres = forms.CharField(label='Nombres' , widget = forms.TextInput(attrs={"placeholder":"Ingrese nombre/s del evaluador"}))
    apellido_p = forms.CharField(label='Apellido Paterno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido paterno"}))
    apellido_m = forms.CharField(label='Apellido Materno', widget = forms.TextInput(attrs={"placeholder":"Ingrese apellido materno"}))
    num_cel = forms.CharField(label='Número de celular', widget = forms.NumberInput(attrs={"placeholder":"ej: 9 999 999 99"}))
    email_personal = forms.CharField(label='Email Personal', widget = forms.TextInput(attrs={"placeholder":"ej: ejemplo@ejemplo.com"}))
    email_empresa = forms.CharField(label='Email empresa', widget = forms.TextInput(attrs={"placeholder":"ej: empresa@ejemplo.com"}))
    contraseña = forms.CharField(label='Contraseña', widget = forms.TextInput(attrs={"placeholder":"Ingrese contraseña"}))

    class Meta:
        model = Evaluador

        fields = [
            'id_evaluador', 
            'rut_evaluador',
            'nombres',
            'apellido_p',
            'apellido_m',
            'num_cel',
            'email_personal',
            'email_empresa',
            'contraseña',
        ]

class actividadForm(forms.ModelForm):

    id_caso = forms.CharField(label='Identificación', widget = forms.TextInput(attrs={"placeholder":"Número de identificación"}))
    nombre = forms.CharField(label='Nombre', widget = forms.TextInput(attrs={"placeholder":"Nombre del caso"}))
    descripcion_caso = forms.CharField(label='Descripción', widget = forms.TextInput(attrs={"placeholder":"Descripción del caso"}))

    class Meta:
        model = Casos

        fields = [
            'id_caso',
            'nombre',
            'descripcion_caso'
        ]

fecha_hoy="{0}".format(datetime.datetime.now().strftime("%d/%m/%Y"))

class asignarForm(forms.ModelForm):

    id_evcaso = forms.CharField(label='Número del caso', widget = forms.TextInput(attrs={"placeholder":"Identificción del caso"}))
    fecha_asignacion = forms.DateField(label='Fecha de Asignación', widget = DateInput, initial=fecha_hoy)

    class Meta:
        model = EvaluacionCaso

        fields = [
            'id_evcaso',
            'casos_id_caso',
            'evaluado_id_evaluado',
            'fecha_asignacion',
            'evaluador_id_evaluador',
            'admin_id_admin'
        ]

        labels = {
            'casos_id_caso': 'Número del Caso',
            'evaluado_id_evaluado': 'Evaluado',
            'evaluador_id_evaluador': 'Evaluador',
            'admin_id_admin': 'Administrador'
        }

        widgets = {
            'casos_id_caso': forms.Select(attrs={'class':'form-control'}),
            'evaluado_id_evaluado': forms.Select(attrs={'class':'form-control'}),
            'evaluador_id_evaluador': forms.Select(attrs={'class':'form-control'}),
            'admin_id_admin': forms.Select(attrs={'class':'form-control'})
        }

class SubirvideoForm(forms.ModelForm):
    class meta:
        model = EvaluacionCaso
        fields = 'video_respuesta'