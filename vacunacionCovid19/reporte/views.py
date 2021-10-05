from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers, status

from rest_framework.parsers import JSONParser
from reporte.models import Persona, Vacuna, Vacunacion 
from reporte.serializers import PersonaSerializer, VacunaSerializer, VacunacionSerializer
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def MPersona(request):
    if request.method=="GET":
        Personas=Persona.objects.all()
        print(type(Personas))
        serializer=PersonaSerializer(Personas,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method== "POST":
        data=JSONParser().parse(request)
        serializer= PersonaSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@api_view(['GET','POST'])

def MVacuna(request):
    if request.method=="GET":
        Vacunas=Vacuna.objects.all()
        serializer=VacunaSerializer(Vacunas,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method== "POST":
        data=JSONParser().parse(request)
        serializer= VacunaSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@api_view(['GET','POST'])
def MVacunacion(request):
    if request.method=="GET":
        Vacunaciones=Vacunacion.objects.all()
        serializer=VacunacionSerializer(Vacunaciones,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method== "POST":
        data=JSONParser().parse(request)
        serializer= VacunacionSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])
def MPersona_Detailed(request,pk):
   #obtener la persona apartir del pk
    try:
        persona=Persona.objects.get(pk=pk)
        
    except Persona.DoesNotExist:
        return JsonResponse({"error": "Persona no encontrada","pk":pk},status=status.HTTP_404_NOT_FOUND)
        
    if request.method== 'GET':
        serializer= PersonaSerializer(persona)
        return JsonResponse(serializer.data,safe=False)

    elif request.method== "PUT":
        data=JSONParser().parse(request)
        serializer= PersonaSerializer(persona,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_202_ACCEPTED)
        return JsonResponse (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        persona.delete()
        return JsonResponse({"info":"persona eliminada","pk":pk},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT','DELETE'])
def MVacuna_Detailed(request,pk):
   
    try:
        vacuna=Vacuna.objects.get(pk=pk)
        
    except Vacuna.DoesNotExist:
        return JsonResponse({"error": "Vacuna no encontrada","pk":pk},status=status.HTTP_404_NOT_FOUND)
        
    if request.method== 'GET':
        serializer= VacunaSerializer(vacuna)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer= VacunaSerializer(vacuna,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_202_ACCEPTED)
        return JsonResponse (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        vacuna.delete()
        return JsonResponse({"info":"vacuna eliminada","pk":pk},status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','PUT','DELETE'])
def MVacunacion_Detailed(request,pk):
   
    try:
        vacunacion=Vacunacion.objects.get(pk=pk)
        
    except Vacunacion.DoesNotExist:
        return JsonResponse({"error": "Vacunacion no encontrada","pk":pk},status=status.HTTP_404_NOT_FOUND)
        
    if request.method== 'GET':
        serializer= VacunacionSerializer(vacunacion)
        return JsonResponse(serializer.data,safe=False)

    elif request.method== "PUT":
        data=JSONParser().parse(request)
        serializer= VacunacionSerializer(vacunacion,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_202_ACCEPTED)
        return JsonResponse (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        vacunacion.delete()
        return JsonResponse({"info":"vacunacion eliminada","pk":pk},status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def Mpersona_query_bynombre(request,nombre):
    try:
        persona= Persona.objects.all().filter(nombre__contains=nombre)
        serializer=PersonaSerializer(persona,many=True)
        return JsonResponse(serializer.data,safe=False)
    except Persona.DoesNotExist:
        return JsonResponse({"error": "Personas con nombre %0 no existe ".format(nombre)},status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def Mpersona_query_bynombreA(request,nombre,apellido):
    try:
        persona= Persona.objects.all().filter(nombre__contains=nombre,apellido__contains=apellido)
        serializer=PersonaSerializer(persona,many=True)
        return JsonResponse(serializer.data,safe=False)
    except Persona.DoesNotExist:
        return JsonResponse({"error": "Personas con nombre %0 no existe ".format(nombre)},status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def Mpersona_query_bynombreAV(request,vacunado):
    try:
        persona= Persona.objects.all().filter(vacunado=vacunado)
        serializer=PersonaSerializer(persona,many=True)
        return JsonResponse(serializer.data,safe=False)
    except Persona.DoesNotExist:
        return JsonResponse({"error": "Personas con nombre %0 no existe ".format(vacunado)},status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def Mpersona_query_bynombreAVA(request,vacunado,fecha_nacimiento):
    try:
        persona= Persona.objects.all().filter(vacunado=vacunado,fecha_nacimiento__contains=fecha_nacimiento)
        serializer=PersonaSerializer(persona,many=True)
        return JsonResponse(serializer.data,safe=False)
    except Persona.DoesNotExist:
        return JsonResponse({"error": "Personas con nombre %0 no existe ".format(vacunado)},status=status.HTTP_404_NOT_FOUND)