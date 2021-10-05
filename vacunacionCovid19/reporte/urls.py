from django.urls import path
from reporte import views
from rest_framework.authtoken import views as viewToken
urlpatterns=[
    path('personas',views.MPersona),
    path('personas/<pk>',views.MPersona_Detailed),
    path('personas/name/<str:nombre>',views.Mpersona_query_bynombre),
    path('personas/apellido/<str:nombre>/<str:apellido>',views.Mpersona_query_bynombreA),
    path('personas/vacunado/<vacunado>',views.Mpersona_query_bynombreAV),
    path('personas/vacunado/<vacunado>/<fecha_nacimiento>',views.Mpersona_query_bynombreAVA),
    path('vacunas',views.MVacuna),
    path('vacunas/<pk>',views.MVacuna_Detailed),
    path('vacunaciones',views.MVacunacion),
    path('vacunaciones/<pk>',views.MVacunacion_Detailed),
    path('token',viewToken.obtain_auth_token),
    
    
]
