from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import UserForm
from .forms import LogInForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponseNotFound('<h1>User is inactive. Please inform the administrator.')
    else:
        form = LogInForm()

    return render(request, 'index.html', {'form' : form})


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1']
            )
            return HttpResponseRedirect(' ')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form' : form})



def home(request):
    return render(request, 'home.html')
