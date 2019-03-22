from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    if request.session._session:
        context = {
            "f_name" : request.session['first_name'],
            "l_name" : request.session['last_name'],
            "email" : request.session['email'],
        }
    else:
        context = {}

    return render(request, "index.html", context)



def process_registration(request):
    errors = User.objects.reg_validator (request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        request.session['first_name'] = request.POST['fname']
        request.session['last_name'] = request.POST['lname']
        request.session['email'] = request.POST['email']
        return redirect ('/')

    else:
        User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = request.POST['password'])
        messages.success(request, "Successfully registered")
        request.session['first_name'] = request.POST['fname']

        return redirect("/reg_success")

def reg_success(request):
        context = {
            "user" : request.session['first_name']
        }
        return render(request, "success.html", context)

def process_login(request):
    errors = User.objects.login_validator (request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        request.session['login_email'] = request.POST['login_email']
        return redirect('/')
    else:
        request.session['login_email'] = request.POST['login_email']
        return redirect('/log_success')


def log_success(request):
    if 'login_email' in request.session:
        dbemail = User.objects.get(email = request.session['login_email'])

        context = {
            "user" : dbemail.first_name
        }
        return render(request, "success.html", context)

def destroy_session(request):
    request.session['first_name'] = ""
    request.session['last_name'] = ""
    request.session['email'] = ""
    request.session['login_email'] = ""
    return redirect('/')