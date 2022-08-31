from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns=[
    path('all_courses/',views.all_courses.as_view(),name='courses'),
    path('about',views.about.as_view(),name="about"),
    path('testimonials',views.testimonials.as_view(),name="testimonials"),
    path('feedback/',views.feedback.as_view(),name="feedback")

]
