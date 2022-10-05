from django.http import HttpResponse
from django.template import Context, Template, loader
from mvt.models import Persona
from datetime import datetime
import random


def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\mariana figueras\Desktop\Código\Proyectos Python\proyectoclase17\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
        
    return HttpResponse(template_renderizado)

def hola (request):
    return HttpResponse('<h1> Buenas clase y Mari! </h1>')

def mi_template(request, nombre):
    template = loader.get_template("mi_template.html")
    template_renderizado = template.render({'persona':nombre})
    return HttpResponse(template_renderizado)

def crear_persona(request):
    persona1 = Persona(nombre='Graciela', apellido='Garcia', edad=random.randrange (1,99), fecha_nacimiento= datetime.now())
    persona2 = Persona(nombre='Carlos', apellido='Olmedo', edad=random.randrange(1,99), fecha_nacimiento= datetime.now())
    persona3 = Persona(nombre='Cecilia', apellido='Perez', edad=random.randrange(1,99), fecha_nacimiento= datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()
    template = loader.get_template("crear_persona.html")
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all()
    template = loader.get_template("ver_personas.html")
    template_renderizado = template.render({'personas':personas})
    return HttpResponse(template_renderizado)


