from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

# Create your views here.
class StudentLogin(View):
    def get(self,request):
        template_name = 'auth_app/login.html'
        context = {}
        return render(request,template_name,context)
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print("User is here :- ",user)
        if(user is not None):
            login(request,user)
            return redirect('show_stu')
        return redirect('signup')

    
class StudentRegister(View):
    def get(self,request):
        form = UserCreationForm()
        template_name = 'auth_app/register.html'
        context = {'form':form}
        return render(request,template_name,context)
    
    def post(self,request):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('login')
        return HttpResponse("<h1>Login credentials not match</h1>")
    
class StudentLogout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

    
