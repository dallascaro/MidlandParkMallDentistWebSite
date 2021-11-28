from django.db import models

# Create your models here.
# Store the patients information
class patients(models.Model):
    # set max character name size
    firstName = models.CharField(max_length = 40, blank= False) # have to use max length with char field
    lastName = models.CharField(max_length = 40, blank= False)
    dateOfBirth = models.DateField(blank= False)
    address = models.TextField(max_length = 40, blank= False)
    phoneNumber = models.TextField(max_length = 15, blank= False)
    email = models.EmailField(max_length = 40, blank= False)
    socialSecurity = models.TextField(max_length = 9, blank= False)
