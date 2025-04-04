from django.http import Http404
from django.shortcuts import render

from .models import *


# Create your views here.

def news(request):
    return render(request, 'Dashboard/news.html')
def component(request):
    return render(request, 'Dashboard/component.html')
def vehicle(request):
    workpackages = WorkPackage.objects.all()
    workpackages_a = WorkPackage.objects.filter(rg_area='RG_C')
    workpackages_b= WorkPackage.objects.filter(rg_area='RG_C')
    workpackages_c = WorkPackage.objects.filter(rg_area='RG_C')
    workpackages_d = WorkPackage.objects.filter(rg_area='RG_D')
    workpackages_e = WorkPackage.objects.filter(rg_area='RG_E')
    workpackages_f = WorkPackage.objects.filter(rg_area='RG_F')

    users = User.objects.all()
    ctx = {'Users': users, 'Workpackages': workpackages, 'Workpackage_A': workpackages_a, 'Workpackage_B': workpackages_b, 'Workpackage_C': workpackages_c, 'Workpackage_D': workpackages_d, 'Workpackage_E': workpackages_e, 'Workpackage_F': workpackages_f}
    return render(request, 'Dashboard/vehicle.html', ctx)
def overview(request):
    return render(request, 'Dashboard/Overview.html')
def home(request):
    user = request.user  # the user
    email = user.email  # their email
    username = user.username  # their username

def details(request, primary_key):
    try:
        workpackage = WorkPackage.objects.get(pk=primary_key)
    except WorkPackage.DoesNotExist:
        raise Http404('Workpackage does not exist')
    workpackages = WorkPackage.objects.all()
    users = User.objects.all()
    ctx = {'Users': users, 'Workpackage': workpackage}
    return render(request, 'Dashboard/WorkPackage_detail.html', ctx)
