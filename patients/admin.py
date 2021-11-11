from django.contrib import admin

# Register your models here.
# relative import- importing product class
from .models import patients

admin.site.register(patients)
