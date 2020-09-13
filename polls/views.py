from django.shortcuts import render
from . import views
from django.http import HttpResponse

from django.views.generic import ListView,TemplateView
from .models import Department

# Create your views here.
 

class DepartmentList(ListView):
    model = Department


def index(request):
    return HttpResponse("Index page")

def detail(request, department_id):
    return HttpResponse("You're looking at Departemnt %s." % department_id) 


class AboutView(TemplateView):
    template_name="student.html"