from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from skills.models import Skills
from quotes.models import Quotes
from projects.models import Projects
from .models import ContactForm

from random import randint


def index(request):
    if request.method == 'GET':
        # get all skills
        skills = Skills.objects.all()

        # get quotes
        max_id_quites = Quotes.objects.order_by('-id')[0]  # get highest id
        random_id = randint(1, max_id_quites.id)  # get random id
        quote = Quotes.objects.get(id=random_id)

        projects_list = Projects.objects.all().filter(is_published=True)
        print(projects_list)
        return render(request, 'pages/index.html', {'skills': skills, 'quote': quote, 'projects': projects_list})

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
