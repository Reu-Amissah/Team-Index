from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AdmissionForm():
    passportpicture = models.ImageField(null=False, blank=False)
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=20, null=False)
    dob = models.DateField(null=False, blank=False)
    
