from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Sections(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='sections')
    about = models.BooleanField(default=True,blank=True)
    experience = models.BooleanField(default=True,blank=True)
    projects = models.BooleanField(default=True,blank=True)
    education = models.BooleanField(default=True,blank=True)
    skills = models.BooleanField(default=True,blank=True)
    certifications = models.BooleanField(default=True,blank=True)
    

class Profile(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    email = models.CharField(max_length=100)
    image = models.ImageField(default = None, upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f"{self.email} : {self.username}"

class Social(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='social')
    github = models.URLField(max_length=200, null=True, blank=True, default="")
    linkedin = models.URLField(max_length=200, null=True, blank=True, default="")
    twitter = models.URLField(max_length=200, null=True, blank=True, default="")

class Experience(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    startdate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    enddate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} : {self.title}"


class Project(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=200, null=True, blank=True)
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    enddate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.TextField(blank=True)

    github = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)


class Education(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='education')
    
    title = models.CharField(max_length=200, null=True, blank=True)
    field = models.CharField(max_length=200, null=True, blank=True)
    school = models.CharField(max_length=200, null=True, blank=True)

    startyear = models.IntegerField(null=True, blank=True)
    endyear = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)


class Certification(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='certificte')
    
    title = models.CharField(max_length=200, null=True, blank=True)
    organisation = models.CharField(max_length=200, null=True, blank=True)
    credential = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    certificate = models.URLField(max_length=200, blank=True, null=True)


class SkillCategory(models.Model):
    
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.title}"

class Skill(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='skills', default=None)
    category = models.ForeignKey("SkillCategory", on_delete=models.CASCADE, related_name='skill')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.name} [{self.category}]"