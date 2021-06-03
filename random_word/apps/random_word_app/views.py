from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'random' not in request.session:
        request.session['random']=""
    if request.POST:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        request.session['random'] = get_random_string(length=14)
        return render(request, 'random_word_app/index.html')
    else:
        return render(request, 'random_word_app/index.html')
    
    
