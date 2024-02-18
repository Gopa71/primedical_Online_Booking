from django.shortcuts import render,redirect
from .models import Task
from servicepp.models import Home 
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate
# Create your views here.
def home(req):
    data=Home.objects.all()
    if req.method=='POST':
        task=req.POST.get('task')
        priority=req.POST.get('priority')
        date=req.POST.get('date')
        tk=Task(task=task,priority=priority,date=date)
        tk.save()

        return redirect('med:delete')
    return render(req,'index.html',{'data':data})

def detail(req):
    data=Task.objects.all()
       
    return render(req,'admin.html',{'data':data})

def delete(req,id):
        data=Task.objects.get(id=id)
        data.delete()
        return redirect('med:detail')

def login(req):
   if req.method=='POST':
      username=req.POST['username']
      password=req.POST['password']
      user=auth.authenticate(username=username,
        password=password)
      
      
     
      if user is not None:
            auth.login(req,user)
            req.session['user']=user.id
            return redirect('med:detail')
      else:
            messages.info(req,"invalid User")
            return redirect('med:login')
   return render(req,'login.html')