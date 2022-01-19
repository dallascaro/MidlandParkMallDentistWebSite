from django.shortcuts import render

from.models import patients
# Create your views here.
def patient_detail_view(request):
    obj = patients.objects.get(id=1)
    context = {
        'firstName': obj.firstName,
        'lastName':obj.lastName,
        'dateOfBirth': obj.dateOfBirth,
        'address': obj.address,
        'phoneNumber': obj.phoneNumber,
        'email': obj.email,
        'socialSecurity': obj.socialSecurity
    } # dictionary
    return render(request, "patient/detials.html", context)
