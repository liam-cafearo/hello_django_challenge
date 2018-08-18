# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def get_home(request):
    return render(request, "sitepages/home.html",
                  {"variable_a": "Welcome to the Home page!",
                   "variable_b": "The home page has been rendered in the child template"})


def get_about(request):
    return render(request, "sitepages/about.html",
                  {"variable_c": "Welcome to the about page",
                   "variable_d": "The about page has been rendered in the child template"})


def get_contact(request):
    return render(request, "sitepages/contact.html",
                  {"variable_e": "Welcome to the contact page",
                   "variable_f": "The contact page has been rendered in the child template"})
