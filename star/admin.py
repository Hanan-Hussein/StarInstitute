from django.contrib import admin
from .models import Profile,Courses,About,Testimonials,Feedback, Assets
# Register your models here.

class courseAdmin(admin.ModelAdmin):
    list_display= ("name" ,"course_Image","duration","price")
    list_filter=("name","price")

class profileAdmin(admin.ModelAdmin):
    list_display=("user","course","profile_image")

class aboutAdmin(admin.ModelAdmin):
    list_display=("founder_name","Institute_name","tag_line","contact_email")

class testimonialsAdmin(admin.ModelAdmin):
    list_display=("username","statement","rating","created_at")

class feedbackAdmin(admin.ModelAdmin):
    list_display=("name","phoneNumber","email","language")

class assetsAdmin(admin.ModelAdmin):
    list_display=("logo","hero_desktop","about_mobile","contact")
admin.site.register(Profile,profileAdmin)
admin.site.register(Courses,courseAdmin)
admin.site.register(About,aboutAdmin)
admin.site.register(Testimonials,testimonialsAdmin)
admin.site.register(Feedback,feedbackAdmin)
admin.site.register(Assets,assetsAdmin)