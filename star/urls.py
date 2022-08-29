from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns=[
    path('all_courses/',views.all_courses.as_view(),name='courses'),


]
