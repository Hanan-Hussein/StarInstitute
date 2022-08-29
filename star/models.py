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
        return self.name

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
    def __str__(self) ->str:
        return self.user

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

