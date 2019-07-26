from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from guests import *
import os


# guests = ['Jonathan Poso', 'Laura Larson and Nathan Osborne', 'Shannen Osborne and Eric Victorino', 'Brittany Osborne']

def index(request):
    # print(guests)
    return render(request,'wedding_app/home.html')

def details(request):
    return render(request,'wedding_app/details.html')

def accomodations(request):
    return render(request,'wedding_app/accomodations.html')

def thingstodo(request):
    return render(request,'wedding_app/thingstodo.html')

def registry(request):
    return render(request, 'wedding_app/registry.html')

def photos(request):
    image_list =[]
    app_static_dir = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(settings.BASE_DIR,'apps'),'wedding_app'),'static'),'wedding_app'),'img'),'photos')  #appname is your appname and brands is the folder that you mentioned
    for file in os.listdir(app_static_dir):
        if file.endswith(".JPG"):
            image_list.append(file)
    # print(image_list)
    context = {
        "photos": image_list,
    }
    return render(request,'wedding_app/photos.html', context)



def rsvp(request):
    return render(request,'wedding_app/rsvp.html')

def find(request):
    names = []
    for x in guests:
        if request.POST['last_name'] in x:
        # if request.POST['last_name'] == x:
            names.append(x)
            rsvpd.append(x)

            # request.session['last_name'] = x
        else:
            request.session['last_name'] = "Your invitation could not be found. Please contact Laura."
    request.session['last_name'] = names
    return redirect("/rsvp")

def select_name(request):
    term = "and"
    words = request.POST['name'].split()
    if term in words:
        print('found an and')
        request.session['person1_first'] = words[0]
        request.session['person1_last'] = words[1]
        request.session['person2_first'] = words[3]
        request.session['person2_last'] = words[4]
    return redirect('/form')

def form(request):
    context = {
        "attendee1": request.session['person1_first'],
        "attendee2": request.session['person2_first']
    }
    return render(request,'wedding_app/rsvp_form.html', context)


#create function that adds people who rsvp to rsvpd array and cross check that so that they cannot keep rsvping
