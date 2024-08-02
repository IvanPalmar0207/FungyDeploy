#Request response
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
#Data Models
from usuarios.models import Producto, Usuario
#Authentification
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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


#Register Page
def registro(request):

    if request.method == 'POST':
        firstName = request.POST['firstName']    
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        userEmail = request.POST['userEmail']
        userPassword = request.POST['userPassword']        
        userConfirm = request.POST['userConfirm']
        hashed_pwd = make_password(userPassword)

        #Pattern password
        patternPassword = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
        validationPassword = re.match(patternPassword,userPassword)

        #Pattern email
        patternEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validationEmail = re.fullmatch(patternEmail, userEmail)
        
        #Validation firstName 
        if(len(firstName) > 60 or len(firstName) < 8):
            sweetify.error(request, 'El nombre no puede tener más de 60 caracteres ni menos de 8 caracteres, por favor intenta nuevamente')  

        elif(firstName.isdigit()):
            sweetify.error(request, 'El nombre no puede contener numeros, intenta nuevamente')        

        #Validation lastName
        elif(len(lastName) > 60 or len(firstName) < 10):
            sweetify.error(request, 'El apellido no puede tener más de 60 caracteres ni menos de 10 caracteres, por favor intenta nuevamente')        
        
        elif(lastName.isdigit()):  
            sweetify.error(request, 'El apellido no puede contener numeros, intenta nuevamente')  

        #Validation userName
        elif(len(userName) > 100 or len(firstName) < 10):
            sweetify.error(request, 'El nombre de usuario no puede tener más de 100 caracteres ni menos de 10 caracteres, por favor intenta nuevamente')        
        
        #Validation Email
        elif(len(userEmail) > 100 or len(userEmail) < 10):
            sweetify.error(request, 'El correo electronico no puede tener más de 100 caracteres ni menos de 10 caracteres, por favor intenta nuevamente')                        

        elif(bool(validationEmail) == False):
            sweetify.error(request, 'El correo es incorrecto, ingresa un correo valido')                

        #Validation Password 
        elif(len(userPassword) > 16 or len(userPassword) < 8):
            sweetify.error(request, 'La contraseña no puede tener más de 16 caracteres ni menos de 8 caracteres, por favor intenta nuevamente')                    
        
        elif(bool(validationPassword) == False):
            sweetify.error(request, 'La contraseña debe contener una letra mayuscula, una letra minuscula y almenos un digito')        
        
        elif(userConfirm != userPassword):
            sweetify.error(request, 'Las contraseñas son diferentes, por favor ingresalas nuevamente')        

        #Save User
        else:
            newUser = User.objects.create(first_name = firstName, last_name = lastName, username = userName, email = userEmail, password = hashed_pwd )
            newUser.save()
            sweetify.success(request, 'Te has registrado correctamente')        
    else:
        sweetify.info (request, 'Bienvenido al formulario de registro')
    return render(request, 'register.html')

#Product's List
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

#Index View
def index_view(request):
    return render(request, 'index.html')

#EmailLogic
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