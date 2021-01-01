
from django.shortcuts import render
import cv2

import os
from datetime import datetime
from dateutil import tz
from .models import visitor
from django.contrib import messages
path=os.getcwd()

from django.shortcuts import redirect
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
        if(visitor.objects.filter(Reference=Reference).order_by('-id').exists()):
            query=visitor.objects.filter(Reference=Reference).order_by('-id')[0]
            if(query.exit=="Still in Campus"):
                messages.error(request, 'Reference ID has already been issued.')
        else:
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
            if(o.exit=="Still in Campus"):
                o.exit=str(current_time)
                o.save()
                return render(request, 'Index.html')
            else:
                messages.error(request, 'Reference ID is not issued.')

        except:
            messages.error(request, 'Reference ID not issued.')

    return render(request, 'Exit_form.html')


