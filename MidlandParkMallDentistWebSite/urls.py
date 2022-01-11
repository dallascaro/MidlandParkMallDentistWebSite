"""MidlandParkMallDentistWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# For web pages and accessing urls

# import View created from view.py in webpages

from django.contrib import admin
from django.urls import path

from webpages.views import homePage_view, servicesPage_view, appointmentsPage_view, patientsPage_view

urlpatterns = [
    path('', homePage_view, name='home'),
    path('home', homePage_view),
    path('services/', servicesPage_view),
    path('appointments/', appointmentsPage_view),
    path('patients/', patientsPage_view),
    # From services view
    path('services/home/', homePage_view),
    path('services/appointments/', appointmentsPage_view),
    path('services/patients/', patientsPage_view),
    # From appointments view
    path('appointments/home/', homePage_view),
    path('appointments/services/', servicesPage_view),
    path('appointments/patients/', patientsPage_view),
    # From patients view
    path('patients/home/', homePage_view),
    path('patients/services/', servicesPage_view),
    path('patients/appointments/', appointmentsPage_view),
    path('admin/', admin.site.urls),
]
