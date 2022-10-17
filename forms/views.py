import imp
import re
from django.shortcuts import render
from django.forms import modelformset_factory
from .models import *



def home(request):
    inputt = input(int())
    ExampleFormSet = modelformset_factory(Example, fields=('name', 'ls'), extra=inputt)
    if request.method == 'POST':
        return inputt

        if request.method == 'POST':
            form = ExampleFormSet(request.POST)
        # instances = form.save(commit=False)
        # for instance in instances:
        #     instance.save()
            instances = form.save()

    form = ExampleFormSet(queryset=Example.objects.none())

    

    return render(request, 'home.html', {'form' : form})



