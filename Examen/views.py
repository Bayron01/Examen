from django.shortcuts import render

# Create your views here.
def index(request):
	data = {}
	template_name = 'contactos/index.html'
	return render(request, template_name, data)

def listar(request):
	data = {}
	template_name = 'contactos/listar.html'
	return render(request, template_name, data)