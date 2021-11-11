from django.db import models

# Create your models here.
# Store the patients information
class patients(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    dateOfBirth = models.TextField()
    address = models.TextField()
    phoneNumber = models.TextField()
    email = models.TextField()
    socialSecurity = models.TextField()
