from django.shortcuts import render
from .models import Emp
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmpSerialilzer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class details(APIView): 
    def get(self, request, format=None):
        # max_salary= Emp.objects.filter(dep_id=dep_id).aggregate(max_salary=max('salary'))
        dep_id= request.GET["dep_id"]
        max_salary= Emp.objects.filter(dep_id=dep_id).order_by('-salary').first()
        serializer= EmpSerialilzer(max_salary) 
        return Response(serializer.data) 
    
