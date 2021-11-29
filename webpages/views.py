from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. # These are the physical webpages
def homePage_view(request,*args, **kwargs): # python specific args
    print(request.user)
    #return HttpResponse("<h1>Home Page</h1>") # string of html not acatual html code
    return render(request, "home.html", {}) # returns html template

# Another View (html page) for services
def servicesPage_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Services Page</h1>")
    return render(request, "services.html", {}) # returns html template

# Another View (html page) for services
def appointmentsPage_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Appointments Page</h1>")
    return render(request, "appointments.html", {}) # returns html template

# Another View (html page) for services
def patientsPage_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Patients Page</h1>")
    return render(request, "patients.html", {}) # returns html template
