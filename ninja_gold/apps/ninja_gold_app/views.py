from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def random_earn(a,b):
    import random
    return random.randrange(a,b)

def activ_datetime():
    import datetime
    return datetime.datetime.now()


def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = ""
    if 'your_gold' not in request.session:
        request.session['your_gold']=0
    context={
        'activities' : request.session['activities'],
        'your_gold' : request.session['your_gold']
    }
    return render(request, 'ninja_gold_app/index.html', context)

def process_money(request):
    if request.POST['place'] == 'farm':   #place is the name of the <input> tag in html file
        gold_earned=random_earn(10, 20) 
        request.session['your_gold'] += gold_earned
        temp = request.session['activities']
        temp  += "<div class='not_casino'> Earned " + str(gold_earned) + " golds from the farm! (" + str(activ_datetime()) + ")</div><b>"
    
    if request.POST['place'] == 'cave':   #place is the name of the <input> tag in html file
        gold_earned=random_earn(5, 10) 
        request.session['your_gold'] += gold_earned
        temp = request.session['activities']
        temp += "<div class='not_casino'> Earned " + str(gold_earned) + " golds from the farm! (" + str(activ_datetime()) + ")</div><b>"
        
    if request.POST['place'] == 'house':   #place is the name of the <input> tag in html file
        gold_earned=random_earn(2, 5) 
        request.session['your_gold'] += gold_earned
        temp = request.session['activities']
        temp += "<div class='not_casino'> Earned " + str(gold_earned) + " golds from the farm! (" + str(activ_datetime()) + ")</div><b>"
    
    if request.POST['place'] == 'casino':   #place is the name of the <input> tag in html file
        gold_earned=random_earn(-50, 50) 
        request.session['your_gold'] += gold_earned
        temp = request.session['activities']
        if gold_earned >= 0:
            temp += "<div class='casino_win'> Entered a casino and earned " + str(gold_earned)  + " golds ... It's amazing (" + str(activ_datetime()) + ")</div><b>"
        else:
            gold_earned = -1 * gold_earned
            temp += "<div class='casino_loss'> Entered a casino and lost " + str(gold_earned)  + " golds ... Ouch.. (" + str(activ_datetime()) + ")</div><b>"
    
    request.session['activities'] = temp
    return redirect('/display')

def display(request):
    context={
        'activities' : request.session['activities'],
        'your_gold' : request.session['your_gold']
    }
    return render(request, 'ninja_gold_app/index.html', context)

if __name__=="__main__":   #we run own app and with debugging active
    app.run(debug=True)
