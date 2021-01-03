from django.shortcuts import render
from django.http import Http404

from .models import CPD
from .models import SDL_Webinars
from .models import SDL_OnlineCourse

# Create your views here.

def home(request, *args, **kwargs):
        return render(request, 'index.html')

def list_of_cpds(request, *args, **kwargs):
    cpd_list = CPD.objects.all()
    context = { 'cpd_list' : cpd_list}
    return render(request, 'list_of_cpds.html', context)

def self_directed_learning(request, *args, **kwargs):
    webinar_list = SDL_Webinars.objects.all()
    onlinecourse_list = SDL_OnlineCourse.objects.all()
    context = { 'webinar_list' : webinar_list,
                'onlinecourse_list': onlinecourse_list}
    return render(request, 'self_directed_learning.html', context)

def my_learning_roadmap(request, *args, **kwargs):
    return render(request, 'my-learning-roadmap.html')