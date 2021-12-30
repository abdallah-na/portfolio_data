from django.db import models
from django.utils.translation import gettext as _

class AboutMe(models.Model):
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    about_me = models.TextField(_("about me"))
    age = models.IntegerField(_("age"))
    current_job = models.CharField(_("current job "), max_length=150)
    profile_pic = models.ImageField(_("profile pic"), upload_to="media")
    about_pic = models.ImageField(_("about pic"), upload_to="media")
    local = models.CharField(_("localisation"), max_length=254)
    phone = models.CharField(_("phone number"),max_length=20)
    facebook = models.SlugField(_("facebook"))
    instgram = models.SlugField(_("instgram"))
    twitter = models.SlugField(_("twitter"))
    linkedin = models.SlugField(_("linkedin"))
    gmail = models.CharField(_("gmail"), max_length=150)

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name

class Education(models.Model):
    Graduation_year = models.IntegerField(_("graduation year")) 
    university_school = models.CharField(_("university or school name"), max_length=254)
    speciality = models.CharField(_("speciality"), max_length=254)
    slug = models.SlugField(_("slug"))

    def fget_absolute_url(self):
        return self.slug
    
    def __str__(self) -> str:
        return self.university_school
    

class Work(models.Model):
    company = models.CharField(_("company name"), max_length=254)
    yearOfWorking = models.IntegerField(_("year of working "))
    _start = models.DateField(_("day of start"))
    _end = models.DateField(_("date of end"))
    slug = models.SlugField(_("slug"))

    def get_absolute_url(self):
        return self.slug
    def __str__(self) -> str:
        return self.company

class Project(models.Model):
    name = models.CharField(_("project name"), max_length=100)
    description = models.TextField(_("description"))
    _image = models.ImageField(_("project image"), upload_to="meia",)
    github = models.SlugField(_("github link"))
    slug = models.SlugField(_("project link"))

    def get_absolute_url(self):
        return self.slug
    def __str__(self) -> str:
        return self.name

    
