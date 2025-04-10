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
def eliminar(resquest,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')      

# Metodo para editar
def editar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)  
    if request.method=="POST":
        form=TareaForm(request.POST,instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TareaForm(instance=tarea)
    return render(request,"todo/editar.html", {"form":form})
                                                    