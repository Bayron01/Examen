from django.shortcuts import render
from Examen.models import Contacto
# Create your views here.
def index(request):
	data = {}
	template_name = 'contactos/index.html'
	return render(request, template_name, data)

def listar(request):
	data = {}
	data['object_list'] = Contacto.objects.all().order_by('id')
	template_name = 'contactos/listar.html'
	return render(request, template_name, data)

def detalle(request, contactos_id):
    data = {}
    data['contactos'] = Contacto.objects.get(pk=contactos_id)
    template_name = 'contactos/detalle.html'
    return render(request, template_name, data)