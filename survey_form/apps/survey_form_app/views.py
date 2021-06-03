from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    return render(request, 'survey_form_app/index.html')

def process(request):
    if request.POST:
        # request.session['count']=4
        print(request.POST['name'])
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1

        # request.session = request.POST
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',request.session)
        return redirect('/result')
    else:
        return redirect('/')

def result(request):

    print("9999999999", request.session)

    context = {
        'name'  :   request.session['name'],
        'location'  :   request.session['location'],
        'language'  :   request.session['language'],
        'comment'  :   request.session['comment'],
        'count'  :   request.session['count']
    }

    return render(request, 'survey_form_app/result.html', context)


