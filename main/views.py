from django.shortcuts import render
from . models import (contactus, team, clientsay)

# Create your views here.


def index(request):
    team_info = team.objects.all()
    clientsay_info = clientsay.objects.all()
    msg = f'hi, '
    contex = {
        'msg': msg,
        'team_info': team_info,
        'clientsay_info': clientsay_info,

    }
    return render(request, 'index.html', contex)


def clientComments(request):
    client_email = request.POST.get('clmail')
    client_name = request.POST.get('clname')
    client_msg = request.POST.get('contact-message')
    contactus.objects.create(client_email=client_email,
                             client_name=client_name, client_message=client_msg)
    return render(request, 'index.html')
