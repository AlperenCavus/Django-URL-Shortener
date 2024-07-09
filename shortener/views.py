from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL
import uuid
import user_agents
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        if link.startswith('http://'):
            link = link[7:]
        elif link.startswith('https://'):
            link = link[8:]
        uid = str(uuid.uuid4())[:5]
        new_url = URL(link=link, short_uuid=uid)  # Use short_uuid instead of uuid
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = URL.objects.get(short_uuid=pk)  # Use short_uuid for lookup

    # Get IP address
    ip_address = request.META.get('REMOTE_ADDR')

    # Get user agent and parse it
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = user_agents.parse(user_agent_string)

    os = user_agent.os.family
    device = user_agent.device.family
    time = datetime.now()  # Use current time from datetime module

    # Store the information
    url_details.ip_address = ip_address
    url_details.os = os
    url_details.device = device
    url_details.time = time
    url_details.save()

    link = url_details.link
    if not link.startswith(('http://', 'https://')):
        link = 'https://' + link
    return redirect(link)
