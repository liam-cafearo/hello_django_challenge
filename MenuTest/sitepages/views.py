# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime


def get_home(request):
    now = datetime.datetime.now()
    return render(request, "sitepages/home.html", {"current_date": now})


def get_about(request):
    return render(request, "sitepages/about.html",
                  {"variable_a": "Reiciendis molestiae rem. Architecto error aspernatur deserunt qui. Dolores dolor delectus occaecati dolores. Repellat perspiciatis ratione dicta consequatur. Earum nisi commodi animi. Modi inventore possimus quae eligendi.",
                   "variable_b": "Dolores esse sint. Dolor quam magni ut non hic eum beatae. Asperiores ut recusandae molestias eligendi dolorem nobis non quo. Voluptates molestiae minima quaerat qui officiis temporibus autem voluptatem totam. Id maxime cupiditate ut reprehenderit rerum."})


def get_contact(request):
    return render(request, "sitepages/contact.html",
                  {"variable_c": "Firstname: Filiberto",
                   "variable_d": "Lastname: Bruen",
                   "variable_e": "Telephone Number: 1-501-780-2999 x27440"})
