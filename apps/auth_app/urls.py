from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('vendedor/', views.vendedor_dashboard, name='vendedor_dashboard'),
    path('jefe-ventas/', views.jefe_ventas_dashboard, name='jefe_ventas_dashboard'),
    path('api/estadisticas/', views.obtener_estadisticas_tiempo_real, name='estadisticas_tiempo_real'),
]
