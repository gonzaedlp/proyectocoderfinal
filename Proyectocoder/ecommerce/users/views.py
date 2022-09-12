from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from users.forms import User_registration_form

def login_request (request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario,password=clave)
            if usuario is not None:
                login(request,usuario)
                context={'message':f'Bienvenido {nombre_usuario} !!'}
                return render(request,'index.html',context=context)
        form=AuthenticationForm()
        context={'error':'Usuario o contraseña incorrectos','form':form}
        return render(request,'users/login.html',context=context)
        
    elif request.method == 'GET':
        form=AuthenticationForm()
        context={'form':form}
    return render(request,'users/login.html',context=context)

def register(request):
    if request.method == 'POST':
        form=User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')            
        else:
            context={'errors':form.errors}
            form=User_registration_form()
            context['form']=[form]
            return render(request, 'users/register.html',context)

    elif request.method == 'GET':
        form=User_registration_form()
        return render (request,'users/register.html',{'form':form})