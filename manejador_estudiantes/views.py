from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from.models import Colegio, Estudiante
from .forms import EstudianteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def colegio_list(request):
    if request.method == 'GET':
        colegios = Colegio.objects.all().values()
        colegios_list = list(colegios)
        return JsonResponse(colegios_list, safe=False)

def estudiante_list(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        context = {
        'estudiantes_list': estudiantes
        }
        return render(request, 'Estudiantes/estudiantes.html', context)
    
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            measurement = form.save()
            measurement.save()
            messages.add_message(request, messages.SUCCESS, 'Estudiante create successful')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    else:
        form = EstudianteForm()

    context = {
        'form': form,
    }

    return render(request, 'Estudiantes/estudianteCreate.html', context)

def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    messages.add_message(request, messages.SUCCESS, 'Estudiante eliminado exitosamente')
    return HttpResponseRedirect(reverse('estudiante_list'))
