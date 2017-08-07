from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    my_dict = {'help_me':'This is from views.py'}
    return render(request,'help.html', context=my_dict)
