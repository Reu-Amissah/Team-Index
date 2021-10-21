from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdmissionForm():
    passportpicture = models.ImageField(null=False, blank=False)
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=20, null=False)
    dob = models.DateField(null=False, blank=False)
    gender = models.CharField(null=False, blank=False)
    hometown = models.CharField(null=False, blank=False)
    religion = models.Charfield(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    #parent details
    parent_name = models.CharField(max_length=50, null=False, blank=False)
    parent_occupation = models.CharField(max_length=20, null=False, blank=False)
    parent_email = models.EmailField(blank=False, null=False)
    address_line = models.CharField(null=False, blank=False)
    number = models.CharField(max_length=10, null=False, blank=False)


    
