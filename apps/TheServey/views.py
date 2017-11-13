from django.shortcuts import render, HttpResponse, redirect

def register (request):
    return render(request,'TheServey/index.html')

def submit(request):
    if request.method == "POST":
        print "urname in request post", request.POST
        if 'urname' not in request.session:
            request.session['urname'] = request.POST['urname']
            request.session['loca'] = request.POST['loca']
            request.session['fav'] = request.POST['fav']
            request.session['comments'] = request.POST['comments']
            request.session['counter'] = 0
            request.session['counter'] += 1
    return render(request,'TheServey/form.html')
