from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%b %d, %Y <br> %I:%S %p", gmtime())
        # "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, 'time_display_app/index.html', context)