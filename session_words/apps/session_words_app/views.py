from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities']=""
    return render(request, 'session_words_app/index.html')

def process(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Before', request.POST)
    if len(request.POST['new_word']) >0:     
        if 'big_font' in request.POST:
            show_big="30px"
        else:
            show_big="12px" 
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', request.POST)
        temp_list=""
        time_now = strftime("%I:%S %p, %B %d %Y", gmtime())
        temp_list = "<p style='color:" + str(request.POST['color_word']) + "; font-size:" + str(show_big) + ";'>"+ str(request.POST['new_word']) + "</p>"
        temp_list += "<span> - added on " + str(time_now) + "</span><br>"
        request.session['activities'] += temp_list
        return redirect('/session_words')
    return redirect('/')

def session_words(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@After', request.session)
    context = {
    "activities": request.session['activities']
    }   
    return render(request, 'session_words_app/index.html', context)

def clear_session(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Clear')
    request.session.clear()  
    return redirect('/')