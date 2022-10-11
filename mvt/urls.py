from django.urls import path
from mvt import views

urlpatterns = [ 
    path('', views.index),
    path('hola/', views.hola),
    path('template/', views.mi_template),
    # path('admin/', admin.site.urls),
    path('mi_template/<str:nombre>', views.mi_template),
    path('ver_personas/', views.ver_personas),
    # path('crear_personas/', views.crear_persona)
    path('crear_persona/<str:nombre>/<str:apellido>/', views.crear_persona)
]
