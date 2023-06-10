
from django import urls
from django.urls import path, include, re_path
from .views import LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios, agregarProducto, customjsonybajarstock, retornarPagado


urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
     path('auth/registro/',
         SignupView.as_view(), name='auth_signup'),
     path('user/profile/',
         ProfileView.as_view(), name='user_profile'),
     path('usuarios/',
         ListarUsuarios.as_view(), name='listar_usuarios'),
     path('agregarproducto/',
         agregarProducto.as_view(), name='agregar_producto'),
    path('retornarPagado/',
         retornarPagado.as_view(), name='retornarPagado'),
     path('actualizarstock/<int:pk>/<int:cantidad>', customjsonybajarstock.as_view(), name='customjsonybajarstock'),

]
