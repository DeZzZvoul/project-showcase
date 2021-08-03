from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddProjectForm
from .models import *
menu = ["Главная", "Проекты","Преподаватели", "Проблемы"]
buttons = ["ДОБАВИТЬ ПРОБЛЕМУ", "ДОБАВИТЬ ПРОЕКТ"]
def index(request):
    projects = Projects.objects.all()
    return render(request,'problems/index.html', {'projects': projects,'menu': menu, 'title': 'Проекты', 'buttons':buttons})

def projectpage(request, pr_id):
    p = get_object_or_404(Projects, pk=pr_id)
    return render(request, 'problems/project_page.html', {'menu': menu,'buttons':buttons,'p': p})

def main(request):
    return  render(request,'problems/base.html', {'menu': menu,'buttons':buttons, 'title': 'Проектная площадка ММФ НГУ'})

def addpage(request):
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('add_page')
        else:
            print('')
    elif request.method == 'GET':
        form = AddProjectForm()
    else:
        print('')
    return render(request, 'problems/addForm.html', {'form': form})
"""
title = ""
problem = ""
analysis = ""
shortdescription = ""
description = ""
user = Users.objects.get(id = 4)
def add_to_base():
    test_project = Projects.objects.create(title = title, problem = problem, analysis = analysis,
                                           shortdescription = shortdescription, description = description)
    test_project.project.add(user)
    return
    """