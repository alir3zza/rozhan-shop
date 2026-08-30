from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

from django.shortcuts import render

def signup_view(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():
            user =form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            login(request, user)
            return redirect("home")

    else:
        form = SignupForm()

    return render(request, "account/signup.html", {"form":form})


def login_view(request):
    if request.method == "POST":

         username= request.POST['username']
         password = request.POST['password']

         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect("home")

    return render(request, "account/login.html")




def logout_view(request):
    logout(request)
    return redirect("home")



@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request,"profile.html",{"profile":profile})


def panel_view(request):
    return render(request,'account/panel.html')
