from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.registro, name='register'),
    path('', views.index_view, name='index'),
    path('paso_paso', views.paso_paso_view, name='paso_paso'),
    path('capacitaciones', views.capacitaciones_view, name='capacitaciones'),
    path('conocenos', views.conocenos_view, name='conocenos'),
    path('blog', views.blog_view, name='blog'),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('listar_productos/showMoreProducts/<id>',views.showProducts, name='showMoreProducts'),
    path('contact', views.contactEmail, name='contact'),
    path('logout/', views.exit, name = 'exit')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)