import imp
from django.shortcuts import render
from rest_framework import generics
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import CoursesSerializer,TestimonialsSerializer,AboutSerializer
from .models import Courses, About,Profile, Testimonials
# Create your views here.

class all_courses(APIView):
    def get(self,request):
        if request.method=='GET':
            courses=Courses.objects.all()
            serializer=CoursesSerializer(courses,many=True)
            return Response(serializer.data)

class about(APIView):
    def get(self,request):
        if request.method=='GET':
            about=About.objects.all()
            serializer=AboutSerializer(about,many=True)
            return Response(serializer.data)

class testimonials(APIView):
    def get(self,request):
        if request.method=='GET':
            testimonials=Testimonials.objects.all()
            serializer=TestimonialsSerializer(testimonials,many=True)
            return Response(serializer.data)
