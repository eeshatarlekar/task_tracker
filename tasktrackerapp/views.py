from django.shortcuts import render,HttpResponse,redirect,HttpResponsePermanentRedirect
from .forms import RegistrationForm,ProjectForm,TasksForm
from .models import Project,Tasks,User
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.views.generic import TemplateView,FormView,CreateView,ListView, DeleteView, UpdateView

# Create your views here.
def home(request):

            if request.method=='POST':
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    request.session['uid']=user.id
                    login(request,user)
                    return dashboard(request)
                else:
                    msg='Wrong Credentials'
                    return HttpResponse('Wrong Credentials. Please try again')
            else:
                return render(request,'login_form.html')

            


class Registration(CreateView):
    form_class=RegistrationForm
    template_name='registration_form.html'
    success_url='/'


def logout_view(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    return render(request,'dashboard.html')

class Project(CreateView):
    form_class=ProjectForm
    template_name='forms.html'
    success_url='tasktrackerdashboard'



from tasktrackerapp import models
def addproj(request):
    
            if request.method=='POST':
                uid=request.session.get('uid')
                u=User.objects.get(id=uid)
                proj=request.POST.get('proj_name')
                desc=request.POST.get('description')
                dl=request.POST.get('deadline')
                new_user = models.Project.objects.create(proj_name=proj,description=desc,deadline=dl,user=u)
                new_user.save()
                   
                return dashboard(request)
            else:
                f=ProjectForm
                return render (request,'forms.html',{'form':f})
        

def addtask(request):
    
            if request.method=='POST':
                id=request.session.get('uid')
                uid=User.objects.get(id=id)
                task=request.POST.get('task_name')
                proj=request.POST.get('project')
                
                proj_id=models.Project.objects.get(id=proj)
                s_time=request.POST.get('start_time')
                e_time=request.POST.get('end_time')
                new_task = Tasks.objects.create(task_name=task, project=proj_id, start_time=s_time,end_time=e_time,user=uid)
                new_task.save()
                return dashboard(request)
            else:
                
                uid=request.session.get('uid')
                u=User.objects.get(id=uid)
                proj=models.Project.objects.filter(user=u)
                print(proj)
                
                
                
                f=TasksForm
                d={'proj':proj,'form':f}
                return render(request,'tasks.html',d)
               


    
from tasktrackerapp import models
class TaskList(ListView):
    model=models.Tasks
    template_name='list.html'

    def get_queryset(self):
        test_filter = self.request.session.get('uid')
        if test_filter:
            object_list=models.Tasks.objects.filter(user=test_filter)
            return object_list
        else:
            return Tasks.objects.all()

            

    
