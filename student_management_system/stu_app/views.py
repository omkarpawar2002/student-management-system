from django.shortcuts import render,redirect
from django.views import View
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CreateStudentView(LoginRequiredMixin,View):
    login_url = 'login'
    template_name = 'stu_app/create_stu.html'

    def get(self,request):
        form = StudentForm()
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('show_stu')
        context = {'form':form}
        return render(request,self.template_name,context)

class ShowStudentView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        objs = Student.objects.all()
        template_name = 'stu_app/show_stu.html'
        context = {'records':objs}
        return render(request,template_name,context)
    
class UpdateStudentView(View):
    def get(self,request,pk):
        obj = Student.objects.get(roll=pk)
        form = StudentForm(instance=obj)
        template_name = 'stu_app/update_stu.html'
        context = {'form':form}
        return render(request,template_name,context)

    def post(self,request,pk):
        obj = Student.objects.get(roll=pk)
        form = StudentForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('show_stu')
        return HttpResponse('data error')
    
class DeleteStudentView(View):

    def get(self,request,pk):
        obj = Student.objects.get(roll=pk)
        template_name = 'stu_app/delete_stu.html'
        context = {'record':obj}
        return render(request,template_name,context)
    
    def post(self,request,pk):
        obj = Student.objects.get(roll=pk)
        if(obj is not None):
            obj.delete()
            return redirect('show_stu')
        return HttpResponse("Error occured")
