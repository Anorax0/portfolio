from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from pages.models import About, ContactForm, Skills, Projects, Quotes
from pages.todays_info import TodaysInfo
from pages.tasks import send_email_task
from pages.weather import WeatherAPI


import logging

log = logging.getLogger(__name__)


def index(request):
    if request.method == "GET":

        # get all skills
        skills = Skills().get_all()

        # get quotes
        quote = Quotes().get_random_quote()

        # get today's inf
        todays_info = TodaysInfo().get_events()

        # get today's weather
        weather = WeatherAPI().get()

        # get list of projects
        projects_list = Projects().get_all()

        return render(
            request,
            "pages/index.html",
            {
                "skills": skills,
                "quote": quote,
                "projects": projects_list,
                "todays_event": todays_info["events"],
                "todays_deaths": todays_info["deaths"],
                "todays_births": todays_info["births"],
                "weather": weather,
            },
        )

    elif request.method == "POST":
        login(request)


def about(request):
    context = {"about": About.objects.first()}
    return render(request, "pages/about.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        contact_form = ContactForm(name=name, email=email, message=message)
        contact_form.save()

        # celery task
        send_email_task(name, message)

        messages.success(request, "Your message has been send.")
        return render(request, "pages/contact.html")
    else:
        return render(request, "pages/contact.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("admin")
        else:
            messages.error(request, "Invalid credentials.")
            return HttpResponseRedirect("login")
    else:
        return render(request, "pages/login.html")


def projects(request, project=None):
    if project == "compiler":
        return render(request, "pages/compiler.html")
    else:
        return HttpResponseRedirect("index")
