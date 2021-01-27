from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from datetime import date
import os
import csv
from datetime import datetime
from dateutil import tz
from .models import visitor
from django.contrib import messages
path=os.getcwd()

from django.shortcuts import redirect
def home(request):
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('home/')
        return HttpResponseRedirect('/')

    return render(request,'login_page.html')

@login_required(login_url='/')
def landing_page(request):
    return render(request,'Index.html')

def logout(request):
    print("logout called")
    auth_logout(request)
    return HttpResponsePermanentRedirect('/')

@login_required(login_url='/')
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
        imagename=request.POST.get("imagename")
        other1=""
        print(imagename)
        if(other==None):
            other1+="NA"
        else:
            other1=other
        print("Value of other: ",other1)
        imagename1=""
        if (imagename == None):

            imagename1 += "NA"
        else:
            imagename1=imagename
        if(visitor.objects.filter(Reference=Reference).order_by('-id').exists()):
            query=visitor.objects.filter(Reference=Reference).order_by('-id')[0]
            if(query.exit=="Still in Campus"):
                messages.error(request, 'Reference ID has already been issued.')
            else:
                log = visitor(name=name, imagename=imagename1, entry=current_time, phone=phone,
                              dateofentry=str(date.today()), address=address, other=other1, purpose=purpose,
                              email=email, identity=identity, Reference=Reference, aadhar=aadhar, section=section)
                log.save()
                # return render(request, 'Index.html')
                return HttpResponseRedirect('home/')
        else:
            log=visitor(name=name,imagename=imagename1,entry=current_time,phone=phone,dateofentry=str(date.today()),address=address,other=other1,purpose=purpose,email=email,identity=identity,Reference=Reference,aadhar=aadhar,section=section)
            log.save()
            # return render(request, 'Index.html')
            return HttpResponseRedirect('home/')
    return render(request,'Entry_Form.html')

@login_required(login_url='/')
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
                return HttpResponseRedirect('home/')
            else:
                messages.error(request, 'Reference ID is not issued.')

        except:
            messages.error(request, 'Reference ID not issued.')

    return render(request, 'Exit_form.html')




@login_required(login_url='/')
def export_users_csv_today(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Today\'s Report.csv"'
    writer = csv.writer(response)
    writer.writerow(['Entry No.','Name','Entry Time','Entry Date', 'Exit Time', 'Phone', 'Email', 'Address', 'Purpose', 'Identity', 'If Other then Specify', 'Reference ID','Aadhar','Section to be Visited ','Image Name As Taken on Device'])

    users = visitor.objects.filter(dateofentry=str(date.today())).values_list()
    for user in users:
        writer.writerow(user)

    return response

@login_required(login_url='/')
def export_users_csv_overall(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Overall Report.csv"'
    # today=str(datetime.date.today())
    writer = csv.writer(response)
    writer.writerow(['Entry No.','Name','Entry Time','Entry Date', 'Exit Time', 'Phone', 'Email', 'Address', 'Purpose', 'Identity', 'If Other then Specify', 'Reference ID','Aadhar','Section to be Visited ','Image Name As Taken on Device'])

    users = visitor.objects.all().values_list()
    for user in users:
        writer.writerow(user)

    return response

@login_required(login_url='/')
def export_users_csv_inside(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Still In Campus Report.csv"'
    # today=str(datetime.date.today())
    writer = csv.writer(response)
    writer.writerow(['Entry No.','Name','Entry Time','Entry Date', 'Exit Time', 'Phone', 'Email', 'Address', 'Purpose', 'Identity', 'If Other then Specify', 'Reference ID','Aadhar','Section to be Visited ','Image Name As Taken on Device'])

    users = visitor.objects.filter(exit="Still in Campus").values_list()
    for user in users:
        writer.writerow(user)

    return response

datel=[]
@login_required(login_url='/')
def export_users_csv_date(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=" Custom Report.csv"'

    date = request.POST.get('date')
    tobepassed=""
    global datel
    if(date!=None):
        date = date.split('/')
        tobepassed+= date[2] + "-" + date[0] + "-" + date[1]
        datel.append(tobepassed)

    print(datel)
    writer = csv.writer(response)
    writer.writerow(['Entry No.','Name','Entry Time','Entry Date', 'Exit Time', 'Phone', 'Email', 'Address', 'Purpose', 'Identity', 'If Other then Specify', 'Reference ID','Aadhar','Section to be Visited ','Image Name As Taken on Device'])
    print("here")
    passv=""
    if len(datel)!=0:
        passv+=datel[len(datel)-1]
    users = visitor.objects.filter(dateofentry=passv).values_list()

    for user in users:
        writer.writerow(user)
    if request.method=="GET":
        while(len(datel)!=0):
            datel.pop(0)
    return response
