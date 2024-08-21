#Request response
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
#Data Models
from usuarios.models import Producto, Categoria
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
@login_required
def exit(request):
    logout(request)
    return redirect('index')

#Manage Users
@login_required
def manageUser(request):
    
    user = User.objects.all()
    
    context = {
        'users' : user
    }
    
    return render(request, 'admin/Users/manageUsers.html', context)

@login_required
#Render AddUser
def renderAddUser(request):
    if request.user.is_superuser:
        return render(request,'admin/Users/addNewUser.html')
    else:
        messages.error(request,'No cuentas con los permisos correspondientes')
        return redirect('/')
@login_required
#Add New User
def addNewUser(request):
    if request.user.is_superuser:
            
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
                    return redirect('manageUsers')                    
                
                elif User.objects.filter(email = userEmail):
                    messages.error(request, 'El usuario ya existe dentro del sistema, intenta nuevamente.')
                    return redirect('manageUsers')                    
                
                elif User.objects.filter(password = hashed_pwd):
                    messages.error(request, 'El usuario ya existe dentro del sistema, intenta nuevamente.')
                    return redirect('manageUsers')                    
                
                else:
                    newUser = User.objects.create(first_name = firstName, last_name = lastName, username = userName, email = userEmail, password = hashed_pwd)
                    newUser.save()
                    messages.success(request, 'Has agregado al usuario correctamente.')
                    return redirect('manageUsers')
            except Exception:
                messages.error(request, 'No ha sido posible agregar al usuario dentro del sistema, intenta nuevamente.')
                return redirect('manageUsers')                
    else:
        messages.error(request,'No cuentas con los permisos correspondientes')
        return redirect('/')

#render UpdateUser
@login_required
def renderUpdateUser(request, id):
    if request.user.is_superuser:
        userUpdate = User.objects.get(id = id)
        
        context = {
            'user' : userUpdate
        }
        
        return render(request,'admin/Users/updateUsers.html', context)
        
    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('/')

#UpdateUser
@login_required
def updateUser(request, id):
    if request.user.is_superuser:        
        if request.method == 'POST':
            firstName = request.POST['firstName']    
            lastName = request.POST['lastName']
            userName = request.POST['userName']
            userEmail = request.POST['userEmail']
            userPassword = request.POST['userPassword']        
            userConfirm = request.POST['userConfirm']
            hashed_pwd = make_password(userPassword)                                        
                                                
            try:                                
                updateUser = User.objects.get(id = id)
                
                updateUser.first_name = firstName
                updateUser.last_name = lastName
                updateUser.username = userName
                updateUser.email = userEmail
                updateUser.password = hashed_pwd
                
                updateUser.save()
                
                messages.success(request, 'Has actualizado al usuario correctamente.')
                return redirect('manageUsers')
            
            except Exception:
                messages.error(request, 'No ha sido posible actualizar al usuario dentro del sistema, intenta nuevamente.')
                return redirect('manageUsers')                
    else:
        messages.error(request,'No cuentas con los permisos correspondientes')
        return redirect('/')

#Delete Users
@login_required
def deleteUsers(request, id):    
    if request.user.is_superuser:
        try:
            userDelete = User.objects.get(id = id)
            userDelete.delete()
            messages.success(request, 'El usuario ha sido eliminado correctamente, gracias.')
            return redirect('/manageUsers')
        except Exception:
            messages.error(request,'No se ha podido eliminar correctamente al usuario, intenta nuevamente')
            return redirect('manageUsers')
    else:
        messages.error(request,'No tienes los permisos correspondiente.')
        return redirect('/')
    
#Manage Products
@login_required
def manageProducts(request):
    if request.user.is_superuser:
        products = Producto.objects.all()                
        
        context = {
            'products' : products
        }
        
        return render(request,'admin/Products/manageProducts.html', context)
        
    else:
        return redirect('/')
    
#renderAddProduct
@login_required
def renderAddProduct(request):
    if request.user.is_superuser:
        categories = Categoria.objects.all()
        
        context = {
            'categories' : categories
        }
        
        return render(request, 'admin/Products/addNewProduct.html', context)
        
    else:
        messages.error(request, 'No tienes los permisos correspondientes.')
        return redirect('/')

#AddProduct
@login_required
def addNewProduct(request):
    if request.user.is_superuser:
        if request.method == 'POST' and request.FILES['productImage']:
            productName = request.POST['productName']
            priceProduct = request.POST['priceProduct']
            descriptionProduct = request.POST['descriptionProduct']
            quantity = request.POST['quantity']
            categorieProduct = Categoria.objects.get(id = request.POST['categorieProduct'])
            productImage = request.FILES['productImage']            
            try:
                newProduct = Producto.objects.create(nombre = productName,precio = priceProduct, categoria = categorieProduct,descripcion = descriptionProduct, stock = quantity, imagen = productImage)                
                newProduct.save()                
                messages.success(request, 'El producto ha sido añadido correctamente, gracias.')
                return redirect('manageProducts')                
            except Exception:
                messages.error(request,'No ha sido posible agregar el producto, intenta nuevamente.')
                return redirect('manageProducts')
        else:
            pass
    else:
        messages.error(request, 'No tienes los permisos correspondientes.')
        return redirect('/')

#Render UpdateProduct
@login_required
def renderUpdateProduct(request, id):
    if request.user.is_superuser:
        updateProduct = Producto.objects.get(id = id)
        categories = Categoria.objects.all()
        
        context = {
            'product' : updateProduct,
            'categories' : categories
        }
        
        return render(request, 'admin/Products/updateProducts.html', context)
        
    else:
        messages.error(request, 'No tienes los permisos correspondientes.')
        return redirect('/')

#UpdateProduct
@login_required
def updateProduct(request, id):
    if request.user.is_superuser:
        if request.method == 'POST' and request.FILES['productImage']:
            productName = request.POST['productName']
            priceProduct = request.POST['priceProduct']
            descriptionProduct = request.POST['descriptionProduct']
            quantity = request.POST['quantity']
            categorieProduct = Categoria.objects.get(id = request.POST['categorieProduct'])
            productImage = request.FILES['productImage']            
            try:
                productUpdate = Producto.objects.get(id = id)                
                
                productUpdate.nombre = productName
                productUpdate.precio = priceProduct
                productUpdate.descripcion = descriptionProduct
                productUpdate.stock = quantity
                productUpdate.categoria = categorieProduct
                productUpdate.imagen = productImage
                
                productUpdate.save()
                
                messages.success(request, 'El producto ha sido actualizado correctamente, gracias.')
                return redirect('manageProducts')                
            except Exception:
                messages.error(request,'No ha sido posible actualizar el producto, intenta nuevamente.')
                return redirect('manageProducts')
        else:
            pass
    else:
        messages.error(request, 'No tienes los permisos correspondientes.')
        return redirect('/')


#Delete Product
def deleteProduct(request, id):
    if request.user.is_superuser:
        try:
            deleteProduct = Producto.objects.get(id = id)
            deleteProduct.delete()
            
            messages.success(request, 'El producto ha sido eliminado satisfactoriamente.')
            return redirect('manageProducts')
        except Exception:
            messages.error(request, 'No ha sido posible eliminar el producto correctamente.')
            return redirect('manageProducts')
    else:
        messages.error(request,'No tienes los permisos correspondientes.')
        return redirect('/')