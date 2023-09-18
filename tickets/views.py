from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Washroom, Ticket, CustomUser, Role
from django.template import loader
from django.contrib.auth.decorators import login_required
from allauth.account.views import LoginView, LogoutView, SignupView
from allauth.socialaccount.views import ConnectionsView
# Create your views here.
from allauth.account.views import LoginView

def login(request):
    # Your custom logic here, if needed
    return LoginView.as_view(template_name='polls/login.html')(request)

@login_required(login_url='/tickets/login/')
def ticket(request, wr_name):
    print("outside")
    if request.method == 'POST':
        print("inside")
        wr = Washroom.objects.get(unique_id=wr_name)
        title = request.POST.get('title')
        print(title)
        print(request.POST.get('title_text'))
        title_text = request.POST.get('title_text')
        user = CustomUser.objects.get_or_create(email=request.user.email, username=request.user.email)[0]
        ticket = Ticket(title=title, ticket_text=title_text, washroom=wr, user=user)
        ticket.save()
        return redirect('home')
    wr = Washroom.objects.get(unique_id=wr_name)
    context = {"wr_name" : wr.unique_id, "wr_location" : wr.location, "wr_condition" : wr.condition}
    template = loader.get_template('polls/ticket.html') 
    return HttpResponse(template.render(context, request))

@login_required(login_url='/tickets/login/')
def home(request):
    # print(request.user.email_address)
    # print(request.user.email)
    try:
        user = CustomUser.objects.get_or_create(email=request.user.email, username=request.user.email)[0]
        user_tickets = Ticket.objects.filter(user=user)
    except:
        user_tickets = []
    context = {"user_tickets" : user_tickets}
    print("Im here")
    template = loader.get_template('polls/home.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/tickets/login/')
def logout(request):
    return LogoutView.as_view()(request)

