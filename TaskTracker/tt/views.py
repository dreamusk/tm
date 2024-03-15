from django.http import HttpResponse 
from django.shortcuts import render
from tt.models import Team
from tt.models import Manage



def team_view(request):
    teams = Team.objects.all()
    return render(request, 'team_template.html', {'teams': teams})

def left(request):
    joined_data = Manage.objects.select_related('pid', 'empid')
    context = {'joined_data': joined_data}
    return render(request, 'left.html', context)

def home(request):
    return render(request,"home.html")

def dataTeam(request):
    return render(request,"dataTeam.html")











