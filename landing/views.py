from django.shortcuts import render
from datetime import datetime
from landing.forms import SubscriberForm


def landing_page(request):
    name = "username"
    current_day = datetime.now()
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
