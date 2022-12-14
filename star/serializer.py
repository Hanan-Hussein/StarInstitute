from dataclasses import field, fields
from.models import Courses,Testimonials,About,Feedback, Assets
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

class FeedbackSerializer(serializers.ModelSerializer):
    language=serializers.PrimaryKeyRelatedField(queryset=Courses.objects.all(),many=False)

    class Meta:
        model=Feedback
        fields='__all__'


class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Assets
        fields='__all__'