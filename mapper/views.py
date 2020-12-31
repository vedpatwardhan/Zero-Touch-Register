import firebase_admin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
import cv2
from django.template import RequestContext
from django.template.context_processors import csrf

from firebase_admin import credentials, firestore
from .forms import EntryForm
from .forms import ExitForm
import os
from datetime import datetime
from dateutil import tz
from .models import visitor


path=os.getcwd()


def home(request):
    return render(request,'Index.html')
def entry(request):
    india_tz = tz.gettz('Asia/Kolkata')
    now = datetime.now()
    now=now.astimezone(india_tz)
    current_time=now.strftime("%d/%m/%Y, %H:%M:%S")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        purpose=request.POST.get('purpose')
        identity=request.POST.get('identity')
        Reference=request.POST.get('Reference_student')
        aadhar=request.POST.get('aadhar')
        section=request.POST.get("department")
        other=request.POST.get("otherIdentity")
        other1=""
        if(other==None):
            other1+="NA"
        else:
            other1=other
        print("Value of other: ",other1)
        image=path+"/image.jpg"
        log=visitor(name=name,entry=current_time,phone=phone,address=address,other=other1,purpose=purpose,email=email,identity=identity,Reference=Reference,aadhar=aadhar,section=section,photo=image)
        log.save()
        return render(request, 'Index.html')
    return render(request,'Entry_Form.html')

def exit(request):
    india_tz = tz.gettz('Asia/Kolkata')
    now = datetime.now()
    now = now.astimezone(india_tz)
    current_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    if request.method == 'POST':
        try:
            Reference_student = request.POST.get('Reference_student')

            o=visitor.objects.filter(Reference=Reference_student).order_by('-id')[0]
            print(o)
            if(o.exit=="Still in Campus"):
                o.exit=str(current_time)
                o.save()
            else:
                return HttpResponse('<b>Reference no. not found as Entered</b>')
            return render(request, 'Index.html')

        except:
            return HttpResponse('<b>Reference no. not found</b>')

    return render(request, 'Exit_form.html')



def validate(n):

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread('test.jpg')

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
    return len(faces)==n

# def firebase_data_entry(name,email,phone,address,purpose,identity,Reference_student,Reference_parent):
#
#     doc = collection.document('log')  # specifies the 'log' document
#     current_time = datetime.now()
#     res = collection.document(str(current_time)).set({
#         'Entry-Time': current_time,
#         'Exit': 'NA',
#         'name': name,
#         'email':email,
#         'phone':phone,
#         'address':address,
#         'purpose':purpose,
#         'identity':identity,
#         'Reference_student':Reference_student,
#         'Reference_parent':Reference_parent,
#     })
#     timelist[tuple([Reference_student,Reference_parent])]=str(current_time)
# print(timelist)