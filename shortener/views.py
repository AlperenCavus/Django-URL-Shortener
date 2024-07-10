from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import URL, UserAccess
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
        new_url = URL(link=link, short_uuid=uid)
        new_url.save()
        return JsonResponse({
            "short_url": new_url.short_uuid,
        })

def go(request, pk):
    url_details = URL.objects.get(short_uuid=pk)

    # Get IP address
    ip_address = request.META.get('REMOTE_ADDR')

    # Get user agent and parse it
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = user_agents.parse(user_agent_string)

    os = user_agent.os.family
    device = user_agent.device.family

    # Check if an entry with the same os and device already exists
    user_access = UserAccess.objects.filter(url=url_details, os=os, device=device).first()
    if user_access:
        user_access.clicks += 1
        user_access.time = datetime.now()
        user_access.save()
    else:
        UserAccess.objects.create(
            url=url_details,
            ip_address=ip_address,
            os=os,
            device=device,
            time=datetime.now()
        )

    link = url_details.link
    if not link.startswith(('http://', 'https://')):
        link = 'https://' + link
    return redirect(link)
