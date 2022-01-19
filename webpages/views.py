from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. # These are the physical webpages
def homePage_view(request,*args, **kwargs): # python specific args
    # can use this for user authentication
    print(request.user)
    print(args, kwargs)
    print(request)
    #return HttpResponse("<h1>Home Page</h1>") # string of html not acatual html code
    return render(request, "home.html", {}) # returns html template
    # Can pass in context into the brackets, Takes template and content renders it all and returns
    # raw html

# Another View (html page) for services
def servicesPage_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Services Page</h1>")
    return render(request, "services.html", {}) # returns html template

# Another View (html page) for appointments
def appointmentsPage_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Appointments Page</h1>")
    my_content = {  # this is a dictonary key/value pair
        "type": "Cleaning",
        "day": 12,
        "weekday": "Monday",
        "month": "Januray",
        "time": 1230,
        "patients_List": ["Dallas", 130, "Austin", 230, "Houston", 330],
        "testHtml": "<h2>This is a testing Html</h2>"
    } #send this to the appointments page
    return render(request, "appointments.html", my_content) # returns html template


# Another View (html page) for patients
def patientsPage_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Patients Page</h1>")
    return render(request, "patients.html", {}) # returns html template
