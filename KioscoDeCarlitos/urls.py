
from django import urls
from django.urls import path, include, re_path
from .views import ActualizarCarrito, ActualizarProductoenCarrito, CarritoComprasVista, CrearCarrito, CrearProductosCarrito, DetalleCarrito, DetalleProductosCarrito, EliminarCarrito, EliminarItemEnCarrito, ListaCarritos, ListarProductosEnCarrito, LoginView, LogoutView, SignupView, ProfileView, ListarUsuarios, agregarProducto, customjsonybajarstock, retornarPagado


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
     path('actualizarstock/<int:pk>/<int:cantidad>', customjsonybajarstock.as_view(), name='customjsonybajarstock'), #
    path('carrito2/',
         CarritoComprasVista.as_view(), name='carritodecompras'),
    path('carrito/', ListaCarritos, name='listarcarritos'),
    path('carrito/<int:pk>/', DetalleCarrito.as_view(), name='detallecarrito'),
    path('carrito/crear/', CrearCarrito.as_view(), name='crearcarrito'),
    path('carrito/<int:pk>/actualizar/', ActualizarCarrito.as_view(), name='actualizarcarrito'),
    path('carrito/<int:pk>/eliminar/', EliminarCarrito.as_view(), name='eliminarcarrito'),
    path('carritoProductos/', ListarProductosEnCarrito.as_view(), name='listarproductoencarrito'),
    path('carritoProductos/<int:pk>/', DetalleProductosCarrito.as_view(), name='detalleproductoencarrito'),
    path('carritoProductos/crear/', CrearProductosCarrito.as_view(), name='crearproductoencarrito'),
    path('carritoProductos/<int:pk>/actualizar/', ActualizarProductoenCarrito.as_view(), name='actualizarproductoencarrito'),
    path('carritoProductos/<int:pk>/eliminar/', EliminarItemEnCarrito.as_view(), name='eliminarproductodelcarrito'),
]
