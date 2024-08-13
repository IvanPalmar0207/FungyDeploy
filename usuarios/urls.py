from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.index_view, name='index'),
    path('login/', views.loginRender, name = 'login'),
    path('logUser/', views.loginUser, name = 'logUser'),
    path('register/', views.registerRender, name='register'),
    path('registerNewUser/', views.register, name = 'RegisterUser'),
    path('paso_paso', views.paso_paso_view, name='paso_paso'),
    path('capacitaciones', views.capacitaciones_view, name='capacitaciones'),
    path('conocenos', views.conocenos_view, name='conocenos'),
    path('blog', views.blog_view, name='blog'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('listar_productos/showMoreProducts/<id>',views.showProducts, name='showMoreProducts'),
    path('contact', views.contactEmail, name='contact'),
    path('logout/', views.exit, name = 'exit')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)