#Request response
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
#Data Models
from usuarios.models import Producto
#Authentification
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
#Email Message
from django.core.mail import EmailMessage
from django.template.loader import render_to_string 
from django.conf import settings
#Regex validation
import re
#SwalAlert
import sweetify
#Messages
from django.contrib import messages

#Render Login
def loginRender(request):
    return render(request, 'login.html')

#Login Page
def loginUser(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        userPassword = request.POST['userPassword']
        
        logUser = authenticate(username = userName, password = userPassword)
        
        if logUser:
            login(request, logUser)                                
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('/')
        else:
            messages.error(request, 'No se ha encontrado el usuario, intenta nuevamente.')
            return redirect('/')

#Render Register
def registerRender(request):
    return render(request, 'register.html')

#Register Page
def register(request):

    if request.method == 'POST':
        firstName = request.POST['firstName']    
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        userEmail = request.POST['userEmail']
        userPassword = request.POST['userPassword']        
        userConfirm = request.POST['userConfirm']
        hashed_pwd = make_password(userPassword)                    
                
        #Save User
        try:            
            if User.objects.filter(username = userName):
                messages.error(request, 'El usuario ya existe dentro del sistema, intenta nuevamente.')
                return redirect('/')                    
            
            elif User.objects.filter(email = userEmail):
                messages.error(request, 'El usuario ya existe dentro del sistema, intenta nuevamente.')
                return redirect('/')                    
            
            elif User.objects.filter(password = hashed_pwd):
                messages.error(request, 'El usuario ya existe dentro del sistema, intenta nuevamente.')
                return redirect('/')                    
            
            else:
                newUser = User.objects.create(first_name = firstName, last_name = lastName, username = userName, email = userEmail, password = hashed_pwd )
                newUser.save()
                messages.success(request, 'Te has registrado correctamente.')
                return redirect('/')
        except Exception:
            messages.error(request, 'No ha sido posible registrarte dentro del sistema, intenta nuevamente.')
            return redirect('/')                

#Product's List
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

#Index View
def index_view(request):
    products = Producto.objects.all()[0:3]
    
    context = {
        'products' : products
    }
    
    return render(request, 'index.html', context)

#EmailLogic
@login_required
def contactEmail(request):
    if request.method == 'POST':
        contactFullName = request.POST['contactFullName']
        emailContact = request.POST['emailContact']
        phoneContact = request.POST['phoneContact']
        messageUser = request.POST['messageUser']

        template = render_to_string('emailTemplate.html',{
            'name' : contactFullName,
            'email' : emailContact,
            'message' : messageUser,
            'phone' : phoneContact
        })

        email = EmailMessage(
            "Sugerencias - Tejido Funji",
            template,
            settings.EMAIL_HOST_USER,
            ['palmar.ivan0205@gmail.com']
        )

        email.fail_silently = False
        
        email.send()      

        if(email.send()):
            messages.success(request, 'El correo se ha enviado correctamente')

        return redirect('index')

#Step by step
def paso_paso_view(request):
    return render(request, 'paso_paso.html')


#Capacitations view
def capacitaciones_view(request):
    return render(request, 'capacitaciones.html')

#About Us view
def conocenos_view(request):
    return render(request, 'conocenos.html')

#Blog view
def blog_view(request):
    return render(request, 'blog.html')

#ShowMoreProducts
@login_required
def showProducts(request, id):
    try:
        products = Producto.objects.get(id = id)
        context = {
            'products' : products
        }
    except:
        sweetify.error(request,'Ha ocurrido un error, por favor intenta nuevamente o inicia sesión')
    else:
        sweetify.success(request,'Podras ver la informacion del producto seleccionado')
        return render(request,'showProducts.html', context)

#Exit or logout view
def exit(request):
    logout(request)
    return redirect('index')