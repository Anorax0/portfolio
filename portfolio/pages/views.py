from django.shortcuts import render
from skills.models import Skills
from quotes.models import Quotes


def index(request):
    skills = Skills.objects.all()
    quotes = Quotes.objects.all()
    return render(request, 'pages/index.html', {'skills': skills, 'quotes': quotes})


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def projects(request):
    pass
