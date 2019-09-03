from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from skills.models import Skills
from quotes.models import Quotes
from projects.models import Projects
from .models import ContactForm


def index(request):
    if request.method == 'GET':
        skills = Skills.objects.all()
        quotes = Quotes.objects.all()
        projects_list = Projects.objects.all()
        return render(request, 'pages/index.html', {'skills': skills, 'quotes': quotes, 'projects': projects_list})

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('admin')
        else:
            messages.error(request, "Invalid credentials.")
            return HttpResponseRedirect('admin')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact_form = ContactForm(name=name, email=email, message=message)
        contact_form.save()

        messages.success(request, 'Your message has been saved.')
        return render(request, 'pages/contact.html')
    else:
        return render(request, 'pages/contact.html')


def projects(request):
    pass
