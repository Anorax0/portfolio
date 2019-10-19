from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from .models import ContactForm, Skills, Projects, Quotes
from .todays_info import TodaysInfo
from .weather import DarkSkyApi
from datetime import datetime

from random import choice


def index(request):
    if request.method == 'GET':
        # get all skills
        skills = Skills.objects.all()

        # get quotes
        try:
            all_quotes = Quotes.objects.filter().values_list('id', flat=True)
            random_quote = choice(all_quotes)
            quote = Quotes.objects.get(id=random_quote)
        except IndexError:
            quote = None

        todays_event = TodaysInfo().todays_event()
        todays_deaths = TodaysInfo().todays_deaths()
        todays_births = TodaysInfo().todays_births()

        # get actual weather for Gdynia, Poland
        weather = DarkSkyApi.objects.filter(forecast_date__date=datetime.today()).first()
        if weather is None:
            weather = DarkSkyApi().get()
            qs = DarkSkyApi(forecast_summary=weather.currently.summary,
                            forecast_temperature=weather.currently.temperature,
                            forecast_humidity=weather.currently.humidity,
                            forecast_windspeed=weather.currently.wind_speed,
                            forecast_pressure=weather.currently.pressure)
            qs.save()
            weather = qs

        projects_list = Projects.objects.all().filter(is_published=True)

        return render(request, 'pages/index.html', {'skills': skills,
                                                    'quote': quote,
                                                    'projects': projects_list,
                                                    'todays_event': todays_event,
                                                    'todays_deaths': todays_deaths,
                                                    'todays_births': todays_births,
                                                    'weather': weather
                                                    })

    elif request.method == 'POST':
        login(request)


def about(request):
    # It wasn't necessary to create this view for static page, but nobody knows when page will be used differently
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        from .tasks import send_email_task
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact_form = ContactForm(name=name, email=email, message=message)
        contact_form.save()
        send_email_task.delay(name)

        messages.success(request, 'Your message has been send.')
        return render(request, 'pages/contact.html')
    else:
        return render(request, 'pages/contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('admin')
        else:
            messages.error(request, "Invalid credentials.")
            return HttpResponseRedirect('login')
    else:
        return render(request, 'pages/login.html')
