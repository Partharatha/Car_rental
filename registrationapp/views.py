from django.shortcuts import render,redirect
from registrationapp.forms import UserForm, UserProfileForm,userUpdateForm,UserProfileUpdateForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registrationapp.forms import PasswordResetForm
from django.contrib import messages


#! Create your views here.

def registration(request):
    registered = False
    if request.method =='POST':
      form = UserForm(request.POST)
      form1 = UserProfileForm(request.POST,request.FILES)

      if form.is_valid() and form1.is_valid():
         user = form.save()
         user.set_password(user.password)
         user.save()

         profile = form1.save(commit=False)
         profile.user = user
         profile.save()
         registered = True
      

        #! to display the data in backend
        #  print(form.cleaned_data['username'])
        #  print(form1.cleaned_data['city'])
     
    else:
        form = UserForm()
        form1 = UserProfileForm()
    context = {
        'form': form,
        'form1': form1,
        'registered': registered
    }
    return render(request, "registration.html", context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        #print(password)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            return HttpResponse("Plz check your creds....!!!!")  


    return render(request, "login.html", {})

@login_required(login_url='login')
def home(request):
    return render(request, "home.html", {})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html", {})

@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = userUpdateForm(request.POST, instance=request.user)
        form1= UserProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid() and form1.is_valid():
            user= form.save()
            user.save()

            profile=form1.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile')
    else:
        form = userUpdateForm(instance=request.user)
        form1=UserProfileUpdateForm(instance=request.user)

    return render(request, "update.html", {'form': form,'form1':form1})




def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            new_password = form.cleaned_data['New_Password']
            confirm_new_password = form.cleaned_data['Confirm_New_Password']
            print(new_password)
            print(confirm_new_password)

            if new_password != confirm_new_password:
                messages.error(request, "Passwords do not match.")
            else:
                try:
                    user = User.objects.get(username=username)
                    user.set_password(new_password)   
                    user.save()
                    messages.success(request, "Password reset successful! Please login.")
                    return redirect("login") 
                except User.DoesNotExist:
                    messages.error(request, "User not found.")
    else:
        form = PasswordResetForm()

    return render(request, "password_reset.html", {"form": form})