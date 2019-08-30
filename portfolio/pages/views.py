from django.shortcuts import render
from django.http import HttpResponse
from portfolio.skills.models import Skills


def index(request):
    # skills = Skills.object.
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def projects(request):
    pass
