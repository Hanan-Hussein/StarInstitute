import imp
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CoursesSerializer,TestimonialsSerializer,AboutSerializer
from .models import Courses, About,Profile
# Create your views here.

class all_courses(APIView):
    def get(self,request):
        if request.method=='GET':
            courses=Courses.objects.all()
            serializer=CoursesSerializer(courses,many=True)
            return Response(serializer.data)
