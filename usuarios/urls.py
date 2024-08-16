from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    #Index
    path('', views.index_view, name='index'),
    #Register and login functionality
    path('login/', views.loginRender, name = 'login'),
    path('logUser/', views.loginUser, name = 'logUser'),
    path('register/', views.registerRender, name='register'),
    path('registerNewUser/', views.register, name = 'RegisterUser'),
    path('logout/', views.exit, name = 'exit'),
    #Info about the page
    path('paso_paso', views.paso_paso_view, name='paso_paso'),
    path('capacitaciones', views.capacitaciones_view, name='capacitaciones'),
    path('conocenos', views.conocenos_view, name='conocenos'),
    path('blog', views.blog_view, name='blog'),
    #Products views
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('listar_productos/showMoreProducts/<id>',views.showProducts, name='showMoreProducts'),
    path('contact', views.contactEmail, name='contact'),    
    #Manage Users
    path('manageUsers/', views.manageUser, name = 'manageUsers'),
    path('renderAddUser/', views.renderAddUser, name = 'renderAddUser'),
    path('addNewUser/', views.addNewUser, name = 'addNewUser'),
    path('renderUpdateUser/<id>', views.renderUpdateUser, name = 'renderUpdateUser'),
    path('updateUser/<id>', views.updateUser, name = 'updateUser'),
    path('deleteUsers/<id>', views.deleteUsers, name = 'deleteUsers'),
    #Manage Products
    path('manageProducts/', views.manageProducts, name = 'manageProducts'),
    path('renderAddProduct/', views.renderAddProduct, name = 'renderAddProduct'),
    path('addNewProduct/', views.addNewProduct, name = 'addNewProduct'),
    path('renderUpdateProduct/<id>', views.renderUpdateProduct, name = 'renderUpdateProduct'),
    path('updateProduct/<id>', views.updateProduct, name = 'updateProduct'),
    path('deleteProducts/<id>', views.deleteProduct, name = 'deleteProducts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)