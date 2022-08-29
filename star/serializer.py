from dataclasses import field, fields
from.models import Courses,Testimonials,About
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields='__all__'

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimonials
        fields='__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        fields='__all__'