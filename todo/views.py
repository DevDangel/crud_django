from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
# Create your views here.
# Metodo para la ruta home.html
def home(request):
    tareas=Tarea.objects.all()
    context={'tareas':tareas}
    return render(request,'todo/home.html',context)

# Metodo para agregar al formulario
def agregar(request):
    if request.method=="POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    return render(request,'todo/agregar.html',{'form':form})

# Metodo para eliminar
