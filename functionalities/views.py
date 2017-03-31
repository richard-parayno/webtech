from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import connection

from .models import *
from .forms import UserForm


# Create your views here.
def index(request):
    logout(request)
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password']
            )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('index')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form' : form})



def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'index.html')

def viewInventory(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM equipments e JOIN equipmentcategory c ON e.equipmentCategoryID = c.equipmentCategoryID JOIN equipmentstatus s on e.equipmentStatus = s.equipmentStatus')
        row = cursor.fetchall()
    
    return render(request, 'warehouseinventory.html', {'inventory': row })


#def requestEquipmentForProject(request):


#def requestMaterialsForProject(request):


#def viewProjectMaterials(request):

#def viewProjectEquipment(request):