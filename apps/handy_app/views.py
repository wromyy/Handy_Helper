from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'handy_app/index.html')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
    'assign_job': Job.objects.filter(job_todo=request.session['user_id']),
    'user': User.objects.get(id=request.session['user_id']),
    'all_jobs': Job.objects.all()
    }
    return render(request, 'handy_app/dashboard.html', context)

def register(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                print(key, value)
                messages.error(request, value)
            return redirect('/')
        register_user = User.objects.create(email=request.POST['email'], password=request.POST['passwordsignup'],first_name=request.POST['fname'], last_name=request.POST['lname'])
        register_user.save()
        request.session['user_id'] = register_user.id
        request.session['fname'] = register_user.first_name
    return redirect('/dashboard')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        login_user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = login_user.id
        request.session['fname'] = login_user.first_name
        print(request.session['fname'])
    return redirect('/dashboard')

def delete_job(request, num):
    login_user = User.objects.get(id=request.session['user_id'])
    delete_job = Job.objects.get(id=num)
    if delete_job.User == login_user:
        d = delete_job
        d.delete()
        return redirect("/dashboard")
    else:
        return redirect("/dashboard")


def logout(request):
    del request.session['fname']
    del request.session['user_id']
    return redirect('/')

def view_job(request, num):
    context = {
        "view_job": Job.objects.get(id=num)
    }
    
    return render(request, 'handy_app/view_job.html', context)

def edit_job(request,num):
    job = Job.objects.get(id=num)
    if request.session['user_id'] != job.User.id:
        return redirect('/dashboard')
    else:
        context = {
            "edit_job": Job.objects.get(id=num),
        }
        return render(request, "handy_app/edit.html",context)

def create(request):
    return render(request, 'handy_app/create_job.html')

def newjobs(request):
    if request.method == "POST":
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/create')       
        create = Job.objects.create(title=request.POST['title'], location=request.POST['location'], description=request.POST['description'], User=User.objects.get(id=request.session['user_id']))
        return redirect('/dashboard')

def update(request, num):
    print("here")
    login_user = User.objects.get(id=request.session['user_id'])
    edit_job = Job.objects.get(id=num)
    if edit_job.User == login_user:
        update_job = Job.objects.get(id=num)
        update_job.title = request.POST['title']
        update_job.location = request.POST['location']
        update_job.description = request.POST['description']
        update_job.save()
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')

def assign_job(request, num):
    job = Job.objects.get(id=num)
    user = User.objects.get(id=request.session['user_id'])
    job.job_todo.add(user)
    return redirect('/dashboard')
