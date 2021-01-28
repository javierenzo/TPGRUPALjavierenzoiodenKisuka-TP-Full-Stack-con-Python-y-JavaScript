from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "secretaria.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["contras"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "index.html", {
                "mensaje": "Credenciales no validas."
            })
    else:
        return render(request, "index.html")

def logout_viewOriginal(request):
    logout(request)
    return render(request, "index.html", {
        "mensaje": "Desconectado."
    })


    #######
def inicio(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login2"))
    #if request.is_authenticated:
    
        
    try:
        if str(request.user.groups.get()) == "Secretaria":
            return render(request, 'secretaria.html')
    except:
        print("An exception occurred")
        return render(request, "index.html", {
            "mensaje": "Credenciales no validas."
        })
        
   
   #if request.user.groups.name == "Secretaria":
    '''    return render(request, 'secretaria.html')
   if request.user.groups.all() == "<QuerySet [<Group: Secretaria>]>":
        print(" ingreso", request.user.groups.name)
    print("no ingreso", request.user.groups.all() ==
          "<QuerySet [<Group: Secretaria>]>")
    print(request.user.groups.all(), request.user.groups.filter(), "grupo", request.user.groups.get())
    #print("comparando", str(request.user.groups.get()) == "Secretaria")
    print("inicio")
    print("comparando", request.user.groups.get()
          == request.user.group.DoesNotExist)
    return render(request, "ventas.html") '''


def login_view2(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["contras"]
        rol = request.POST["menuRol"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if rol == "1":
                return render(request, "secretaria.html")
            elif rol == "2":
                return render(request, "personalMedico.html")
            elif rol == "3":
                return render(request, "ventas.html")
            elif rol == "4":
                return render(request, "taller.html")
            elif rol == "5":
                return render(request, "gerencia.html")
            
            #return HttpResponseRedirect(reverse("inicio"))
        else:
            return render(request, "index.html", {
                "mensaje": "Credenciales no validas."
            })
    else:
        return render(request, "index.html")


def logout_view(request):
    logout(request)
    return render(request, "index.html", {
        "mensaje": "Desconectado."
    })
