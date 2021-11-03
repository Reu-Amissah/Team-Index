from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdmissionForm(models.Model):
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=20, blank=False)
    dob = models.DateField(blank=False)
    gender = models.CharField( blank=False, max_length=20)
    hometown = models.CharField( blank=False, max_length=50)
    religion = models.CharField(blank=False, max_length=50)
    email = models.EmailField( blank=False)
    picture = models.ImageField(null=False, blank=False)
    disability = models.BooleanField(blank=False)
    disability_info = models.CharField(blank=False, max_length=300)
    transportation = models.BooleanField(blank=False)

    #parent details
    parent_name = models.CharField(max_length=50, null=False, blank=False)
    parent_address_line = models.CharField(max_length=200, blank=False)
    parent_occupation = models.CharField(max_length=20, blank=False)
    number = models.CharField(max_length=10, blank=False)
    parent_email = models.EmailField(blank=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url= ''
        return url
        
    def __str__(self):
        return self.firstname



class Contact(models.Model):
    firstname = models.CharField(blank=False, max_length= 50)
    lastname = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False)
    phone = models.CharField(blank=False, max_length=10)
    message = models.CharField(blank=False, max_length=300)

    def __str__(self):
        return self.firstname + " " + self.lastname


    

    
