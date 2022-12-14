from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Courses(models.Model):
    """
    courses offered by the institute
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    course_Image = CloudinaryField("course_image", null=True, blank=True)
    duration= models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"Name: {self.name}: course_Image {self.course_Image}: duration{self.duration}: price{self.duration}"

    @classmethod
    def save_course(self,course):
        """
        saves course
        """
        self.save(course)

    @classmethod
    def delete_course(self,course):
        """
        deletes course
        """
        self.delete(id=course)

    @classmethod
    def update_course(self, name):
        """
        updates course
        """
        self.update(name=name)

    @classmethod
    def find_course(cls, name):
        course = cls.objects.filter(name__icontains=name)
        return course


class Profile(models.Model):
    """
    user's profile
    """
    user = models.OneToOneField(
        User, related_name="users", on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,
                               related_name="courses", on_delete=models.CASCADE, null=True)
    profile_image = CloudinaryField("profile", blank=True, null=True)

    @classmethod
    def __str__(self):
        return f"user:{self.user}: course:{self.course}: profile_image:{self.profile_image}"

    @classmethod
    def save_profile(cls, profile):
        cls.save(profile)


class Testimonials(models.Model):
    """
    testimonials in projects
    """

    # user = models.ForeignKey(
    #     User, related_name="users_testimonials", on_delete=models.CASCADE)
    username=models.CharField(max_length=100,null=True)
    profile=CloudinaryField("user_profile",null=True,blank=True)
    statement = models.CharField(max_length=500)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Username: {self.username}: statement: {self.statement}: rating:{self.rating}: created:{self.created_at}"

class About(models.Model):
    """
    more info about the institute
    """
    founder_name = models.CharField(max_length=100)
    Institute_name = models.CharField(max_length=100)
    about_founder = models.CharField(max_length=1000)
    tag_line = models.CharField(max_length=100)
    hero_section = models.CharField(max_length=1000)
    institute_description = models.CharField(max_length=1000)
    founder_image = CloudinaryField("founder_image", null=True, blank=True)
    hero_image = CloudinaryField("hero_image", null=True, blank=True)
    contact_email=models.EmailField()
    primary_phoneNumber=models.CharField(max_length=200)
    secondary_phoneNumber=models.CharField(max_length=200)

    def __str__(self):
        return f"Founder Name: {self.founder_name}: Institute Name: {self.Institute_name}: Tagline: {self.tag_line}: Email: {self.contact_email}"
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    phoneNumber=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    language=models.ForeignKey(Courses,on_delete=models.CASCADE)
    message=models.CharField(max_length=1000)

    def __str__(self) :
        return f"Name: {self.name}: phone: {self.phoneNumber}: email: {self.email}: language: {self.language}"
    @classmethod
    def save_feedback(cls, feedback):
        cls.save(feedback)

class Assets(models.Model):
    logo=CloudinaryField("logo",null=True,blank=True)
    hero_desktop=CloudinaryField("hero_desktop",null=True,blank=True)
    hero_mobile=CloudinaryField("hero_mobile",null=True,blank=True)
    hero_svg1=CloudinaryField("Hero_svg_1", null=True,blank=True)
    hero_svg2=CloudinaryField("Hero_svg_2",null=True,blank=True)
    hero_svg3=CloudinaryField("Hero_svg_3", null=True,blank=True)
    hero_svg4=CloudinaryField("Hero_svg_4",null=True,blank=True)
    hero_svg5=CloudinaryField("Hero_svg_5",null=True,blank=True)
    about_mobile=CloudinaryField("about_mobile",null=True,blank=True)
    about_desktop=CloudinaryField("about_desktop",null=True,blank=True)
    contact=CloudinaryField("contact",null=True,blank=True)