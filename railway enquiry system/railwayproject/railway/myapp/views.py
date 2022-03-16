
import re
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django import forms
from myapp.forms import *
from myapp.models import *
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
import datetime


'''def index(request):
    
    return render(request,'bookticket.html')'''

def admin_signup(request):
    if request.method=="POST":
        username = request.POST['username']
        print(username)
        forms=admin_form(request.POST)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.is_admin=True
            forms.save()
            return t_registration(request)
        else:
            print("ERROR FROM INVALID")
    return render(request,'signup.html')

def user_signup(request):
    if request.method=="POST":
        forms=admin_form(request.POST)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.is_customer=True
            forms.save()
            return render(request,'login.html')

        else:
            print("ERROR FROM INVALID")
    return render(request,'usersignup.html')


def adminuser_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_admin == True:
            request.session['username'] = username
            print(username)
            return t_registration(request)
            #return book(request)
        
        elif user and user.is_customer == True:
            
            request.session['username'] = username
            return bookticket2(request)
        else:
            return HttpResponse("Invalid login details.....")
    return render(request,'login.html')

def userviewticket(request):
    if 'username' in request.session:
        z=request.session['username']
        f=billing.objects.filter(uname=z)
    return render(request,'userviewticket.html',{'view':f})

def cancel(request,pk):
    c=billing.objects.get(pk=pk)
    c.delete()
    return render(request,'bookticket2.html')
    
   

def adminuser_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(adminuser_login)

def viewticket(request):
    c=billing.objects.all()
    return render(request,'viewticket.html',{'view':c})

def payement(request):
    c=billing.objects.all()
    return render(request,'payement.html',{'view':c})

def admindata(request):
    c=admin.objects.all()
    return render(request,'admindata.html',{'view':c})


def t_registration(request):
    form=train_registration()
    if request.method=='POST':
        form=train_registration(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect(t_display)
        else:
            print("ERROR FORM INVALID")
    return render(request,'traininfo.html',{'form':form})

def t_display(request):
    d=train_reg.objects.all()
    return render(request,'trainview.html',{'view':d})

def bticket(request):
     
    return render(request,'bookticket1.html')

def u_t_display(request):
    d=train_reg.objects.all()
    return render(request,'user_t_details.html',{'view':d})



def book(request,pk):
    d=train_reg.objects.get(pk=pk)
    z=d.train_no
    us=request.session['username']
    
    if request.method=='POST':
        forms=customer_form(request.POST)
        if forms.is_valid():
            
            x=request.POST['train_no']
            y=request.POST['c_from']
            z=request.POST['c_to']
            l=request.POST['firstName']
            m=request.POST['lastName']
            n=request.POST['contact_no']
            q=request.POST['email']
            o=datetime.datetime.now()
            pa=int(request.POST["passenger"])
            p=100
            print(x,y,z,l,m,n,o,pa)
            
            if (z == 'aluva' and y=='pulinchodu'):
                p=100
            elif (y == 'aluva' and z=='pulinchodu'): 
                p=100
            elif (z == 'aluva' and y=='companypady'):
                p=120
            elif (y == 'aluva' and z=='companypady'):
                p=120  
            elif (z == 'aluva' and y=='ambattukavu'):
                p=140  
            elif (y == 'aluva' and z=='ambattukavu'):
                p=140 
            elif (z == 'aluva' and y=='muttom'):
                p=180   
            elif (y == 'aluva' and z=='muttom'):
                p=180
            elif (z == 'aluva' and y=='kalamassery'):
                p=200 
            elif (y == 'aluva' and z=='kalamassery'):
                p=200
            elif (z == 'aluva' and y=='Cochin University'):
                p=200 
            elif (y == 'aluva' and z=='Cochin University'):
                p=200
            elif (z == 'aluva' and y=='Pathadipalam'):
                p=200 
            elif (y == 'aluva' and z=='Pathadipalam'):
                p=200
            elif (z == 'aluva' and y=='Edapally'):
                p=200 
            elif (y == 'aluva' and z=='Edapally'):
                p=200
            elif (z == 'aluva' and y=='Changampuzha park'):
                p=200 
            elif (y == 'aluva' and z=='Changampuzha park'):
                p=200
            elif (z == 'aluva' and y=='Palarivattom'):
                p=200 
            elif (y == 'aluva' and z=='Palarivattom'):
                p=200
            elif (z == 'aluva' and y=='JLN Stadium'):
                p=200 
            elif (y == 'aluva' and z=='JLN Stadium'):
                p=200
            elif (z == 'aluva' and y=='Kaloor'):
                p=200 
            elif (y == 'aluva' and z=='Kaloor'):
                p=200
            elif (z == 'aluva' and y=='Town hall'):
                p=200 
            elif (y == 'aluva' and z=='Town hall'):
                p=200
            elif (z == 'aluva' and y=='MG Road'):
                p=200 
            elif (y == 'aluva' and z=='MG Road'):
                p=200
            elif (z == 'aluva' and y=='Maharajas College'):
                p=200 
            elif (y == 'aluva' and z=='Maharajas College'):
                p=200
            elif (z == 'aluva' and y=='Ernakulam South'):
                p=200 
            elif (y == 'aluva' and z=='Ernakulam South'):
                p=200
            elif (z == 'aluva' and y=='Kadavanthara'):
                p=200 
            elif (y == 'aluva' and z=='Kadavanthara'):
                p=200
            elif (z == 'aluva' and y=='Elamkulam'):
                p=200 
            elif (y == 'aluva' and z=='Elamkulam'):
                p=200
            elif (z == 'aluva' and y=='Vytilla'):
                p=200 
            elif (y == 'aluva' and z=='Vytilla'):
                p=200
            elif (z == 'aluva' and y=='Thykoodam'):
                p=200 
            elif (y == 'aluva' and z=='Thykoodam'):
                p=200
            elif (z == 'aluva' and y=='Petta'):
                p=200 
            elif (y == 'aluva' and z=='Petta'):
                p=200
            elif (z == 'Pulinchodu' and y=='Companypady'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Companypady'):
                p=200
            elif (z == 'Pulinchodu' and y=='Ambattukavu'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Ambattukavu'):
                p=200
            elif (z == 'Pulinchodu' and y=='Muttom'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Muttom'):
                p=200
            elif (z == 'Pulinchodu' and y=='Kalamassery'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Kalamassery'):
                p=200
            elif (z == 'Pulinchodu' and y=='Cochin University'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Cochin University'):
                p=200
            elif (z == 'Pulinchodu' and y=='Pathadipalam'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Pathadipalam'):
                p=200
            elif (z == 'Pulinchodu' and y=='Edapally'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Edapally'):
                p=200
            elif (z == 'Pulinchodu' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Changampuzha park'):
                p=200
            elif (z == 'Pulinchodu' and y=='Palarivattom'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Palarivattom'):
                p=200
            elif (z == 'Pulinchodu' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Pulinchodu' and z=='JLN Stadium'):
                p=200
            elif (z == 'Pulinchodu' and y=='Kaloor'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Kaloor'):
                p=200
            elif (z == 'Pulinchodu' and y=='Town hall'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Town hall'):
                p=200 
            elif (z == 'Pulinchodu' and y=='MG Road'):
                p=200 
            elif (y == 'Pulinchodu' and z=='MG Road'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Maharajas College'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Maharajas College'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Ernakulam South'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Kadavanthara'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Elamkulam'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Elamkulam'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Vytilla'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Vytilla'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Thykoodam'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Thykoodam'):
                p=200 
            elif (z == 'Pulinchodu' and y=='Petta'):
                p=200 
            elif (y == 'Pulinchodu' and z=='Petta'):
                p=200 
            elif (z == 'Companypady' and y=='Ambattukavu'):
                p=200 
            elif (y == 'Companypady' and z=='Ambattukavu'):
                p=200 
            elif (z == 'Companypady' and y=='Muttom'):
                p=200 
            elif (y == 'Companypady' and z=='Muttom'):
                p=200
            elif (z == 'Companypady' and y=='Kalamassery'):
                p=200 
            elif (y == 'Companypady' and z=='Kalamassery'):
                p=200
            elif (z == 'Companypady' and y=='Cochin University'):
                p=200 
            elif (y == 'Companypady' and z=='Cochin University'):
                p=200
            elif (z == 'Companypady' and y=='Pathadipalam'):
                p=200 
            elif (y == 'Companypady' and z=='Pathadipalam'):
                p=200
            elif (z == 'Companypady' and y=='Edapally'):
                p=200 
            elif (y == 'Companypady' and z=='Edapally'):
                p=200
            elif (z == 'Companypady' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Companypady' and z=='Changampuzha park'):
                p=200
            elif (z == 'Companypady' and y=='Palarivattom'):
                p=200 
            elif (y == 'Companypady' and z=='Palarivattom'):
                p=200
            elif (z == 'Companypady' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Companypady' and z=='JLN Stadium'):
                p=200
            elif (z == 'Companypady' and y=='Kaloor'):
                p=200 
            elif (y == 'Companypady' and z=='Kaloor'):
                p=200
            elif (z == 'Companypady' and y=='Town hall'):
                p=200 
            elif (y == 'Companypady' and z=='Town hall'):
                p=200
            elif (z == 'Companypady' and y=='MG Road'):
                p=200 
            elif (y == 'Companypady' and z=='MG Road'):
                p=200
            elif (z == 'Companypady' and y=='Maharajas College'):
                p=200 
            elif (y == 'Companypady' and z=='Maharajas College'):
                p=200
            elif (z == 'Companypady' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Companypady' and z=='Ernakulam South'):
                p=200
            elif (z == 'Companypady' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Companypady' and z=='Kadavanthara'):
                p=200
            elif (z == 'Companypady' and y=='Elamkulam'):
                p=200 
            elif (y == 'Companypady' and z=='Elamkulam'):
                p=200
            elif (z == 'Companypady' and y=='Vytilla'):
                p=200 
            elif (y == 'Companypady' and z=='Vytilla'):
                p=200
            elif (z == 'Companypady' and y=='Thykoodam'):
                p=200 
            elif (y == 'Companypady' and z=='Thykoodam'):
                p=200
            elif (z == 'Companypady' and y=='Petta'):
                p=200 
            elif (y == 'Companypady' and z=='Petta'):
                p=200
            elif (z == 'Ambattukavu' and y=='Muttom'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Muttom'):
                p=200
            elif (z == 'Ambattukavu' and y=='Kalamassery'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Kalamassery'):
                p=200
            elif (z == 'Ambattukavu' and y=='Cochin University'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Cochin University'):
                p=200
            elif (z == 'Ambattukavu' and y=='Pathadipalam'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Pathadipalam'):
                p=200
            elif (z == 'Ambattukavu' and y=='Edapally'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Edapally'):
                p=200
            elif (z == 'Ambattukavu' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Changampuzha park'):
                p=200
            elif (z == 'Ambattukavu' and y=='Palarivattom'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Palarivattom'):
                p=200
            elif (z == 'Ambattukavu' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Ambattukavu' and z=='JLN Stadium'):
                p=200
            elif (z == 'Ambattukavu' and y=='Town hall'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Town hall'):
                p=200
            elif (z == 'Ambattukavu' and y=='MG Road'):
                p=200 
            elif (y == 'Ambattukavu' and z=='MG Road'):
                p=200
            elif (z == 'Ambattukavu' and y=='Maharajas College'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Maharajas College'):
                p=200
            elif (z == 'Ambattukavu' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Ernakulam South'):
                p=200
            elif (z == 'Ambattukavu' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Kadavanthara'):
                p=200
            elif (z == 'Ambattukavu' and y=='Elamkulam'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Elamkulam'):
                p=200
            elif (z == 'Ambattukavu' and y=='Vytilla'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Vytilla'):
                p=200
            elif (z == 'Ambattukavu' and y=='Thykoodam'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Thykoodam'):
                p=200
            elif (z == 'Ambattukavu' and y=='Petta'):
                p=200 
            elif (y == 'Ambattukavu' and z=='Petta'):
                p=200
            elif (z == 'Muttom' and y=='Kalamassery'):
                p=200 
            elif (y == 'Muttom' and z=='Kalamassery'):
                p=200
            elif (z == 'Muttom' and y=='Cochin University'):
                p=200 
            elif (y == 'Muttom' and z=='Cochin University'):
                p=200
            elif (z == 'Muttom' and y=='Pathadipalam'):
                p=200 
            elif (y == 'Muttom' and z=='Pathadipalam'):
                p=200
            elif (z == 'Muttom' and y=='Edapally'):
                p=200 
            elif (y == 'Muttom' and z=='Edapally'):
                p=200
            elif (z == 'Muttom' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Muttom' and z=='Changampuzha park'):
                p=200
            elif (z == 'Muttom' and y=='Palarivattom'):
                p=200 
            elif (y == 'Muttom' and z=='Palarivattom'):
                p=200
            elif (z == 'Muttom' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Muttom' and z=='JLN Stadium'):
                p=200
            elif (z == 'Muttom' and y=='Kaloor'):
                p=200 
            elif (y == 'Muttom' and z=='Kaloor'):
                p=200
            elif (z == 'Muttom' and y=='Town hall'):
                p=200 
            elif (y == 'Muttom' and z=='Town hall'):
                p=200
            elif (z == 'Muttom' and y=='MG Road'):
                p=200 
            elif (y == 'Muttom' and z=='MG Road'):
                p=200
            elif (z == 'Muttom' and y=='Maharajas College'):
                p=200 
            elif (y == 'Muttom' and z=='Maharajas College'):
                p=200
            elif (z == 'Muttom' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Muttom' and z=='Ernakulam South'):
                p=200
            elif (z == 'Muttom' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Muttom' and z=='Kadavanthara'):
                p=200
            elif (z == 'Muttom' and y=='Elamkulam'):
                p=200 
            elif (y == 'Muttom' and z=='Elamkulam'):
                p=200
            elif (z == 'Muttom' and y=='Vytilla'):
                p=200 
            elif (y == 'Muttom' and z=='Vytilla'):
                p=200
            elif (z == 'Muttom' and y=='Thykoodam'):
                p=200 
            elif (y == 'Muttom' and z=='Thykoodam'):
                p=200
            elif (z == 'Muttom' and y=='Petta'):
                p=200 
            elif (y == 'Muttom' and z=='Petta'):
                p=200
            elif (z == 'Kalamassery' and y=='Cochin University'):
                p=200 
            elif (y == 'Kalamassery' and z=='Cochin University'):
                p=200
            elif (z == 'Kalamassery' and y=='Pathadipalam '):
                p=200 
            elif (y == 'Kalamassery' and z=='Pathadipalam'):
                p=200
            elif (z == 'Kalamassery' and y=='Edapally'):
                p=200 
            elif (y == 'Kalamassery' and z=='Edapally'):
                p=200
            elif (z == 'Kalamassery' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Kalamassery' and z=='Changampuzha park'):
                p=200
            elif (z == 'Kalamassery' and y=='Palarivattom'):
                p=200 
            elif (y == 'Kalamassery' and z=='Palarivattom'):
                p=200
            elif (z == 'Kalamassery' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Kalamassery' and z=='JLN Stadium'):
                p=200
            elif (z == 'Kalamassery' and y=='Kaloor'):
                p=200 
            elif (y == 'Kalamassery' and z=='Kaloor'):
                p=200
            elif (z == 'Kalamassery' and y=='Town hall'):
                p=200 
            elif (y == 'Kalamassery' and z=='Town hall'):
                p=200
            elif (z == 'Kalamassery' and y=='MG Road'):
                p=200 
            elif (y == 'Kalamassery' and z=='MG Road'):
                p=200
            elif (z == 'Kalamassery' and y=='Maharajas College'):
                p=200 
            elif (y == 'Kalamassery' and z=='Maharajas College'):
                p=200
            elif (z == 'Kalamassery' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Kalamassery' and z=='Ernakulam South'):
                p=200
            elif (z == 'Kalamassery' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Kalamassery' and z=='Kadavanthara'):
                p=200
            elif (z == 'Kalamassery' and y=='Elamkulam'):
                p=200 
            elif (y == 'Kalamassery' and z=='Elamkulam'):
                p=200
            elif (z == 'Kalamassery' and y=='Vytilla'):
                p=200 
            elif (y == 'Kalamassery' and z=='Vytilla'):
                p=200
            elif (z == 'Kalamassery' and y=='Thykoodam'):
                p=200 
            elif (y == 'Kalamassery' and z=='Thykoodam'):
                p=200
            elif (z == 'Kalamassery' and y=='Petta'):
                p=200 
            elif (y == 'Kalamassery' and z=='Petta'):
                p=200
            elif (z == 'Cochin University' and y=='Pathadipalam'):
                p=200 
            elif (y == 'Cochin University' and z=='Pathadipalam'):
                p=200
            elif (z == 'Cochin University' and y=='Edapally'):
                p=200 
            elif (y == 'Cochin University' and z=='Edapally'):
                p=200
            elif (z == 'Cochin University' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Cochin University' and z=='Changampuzha park'):
                p=200
            elif (z == 'Cochin University' and y=='Palarivattom'):
                p=200 
            elif (y == 'Cochin University' and z=='Palarivattom'):
                p=200
            elif (z == 'Cochin University' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Cochin University' and z=='JLN Stadium'):
                p=200
            elif (z == 'Cochin University' and y=='Kaloor'):
                p=200 
            elif (y == 'Cochin University' and z=='Kaloor'):
                p=200
            elif (z == 'Cochin University' and y=='Town hall'):
                p=200 
            elif (y == 'Cochin University' and z=='Town hall'):
                p=200
            elif (z == 'Cochin University' and y=='MG Road'):
                p=200 
            elif (y == 'Cochin University' and z=='MG Road'):
                p=200
            elif (z == 'Cochin University' and y=='Maharajas College'):
                p=200 
            elif (y == 'Cochin University' and z=='Maharajas College'):
                p=200
            elif (z == 'Cochin University' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Cochin University' and z=='Ernakulam South'):
                p=200
            elif (z == 'Cochin University' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Cochin University' and z=='Kadavanthara'):
                p=200
            elif (z == 'Cochin University' and y=='Elamkulam'):
                p=200 
            elif (y == 'Cochin University' and z=='Elamkulam'):
                p=200
            elif (z == 'Cochin University' and y=='Vytilla'):
                p=200 
            elif (y == 'Cochin University' and z=='Vytilla'):
                p=200
            elif (z == 'Cochin University' and y=='Thykoodam'):
                p=200 
            elif (y == 'Cochin University' and z=='Thykoodam'):
                p=200
            elif (z == 'Cochin University' and y=='Petta'):
                p=200 
            elif (y == 'Cochin University' and z=='Petta'):
                p=200
            elif (z == 'Pathadipalam' and y=='Edapally'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Edapally'):
                p=200
            elif (z == 'Pathadipalam' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Changampuzha park'):
                p=200
            elif (z == 'Pathadipalam' and y=='Palarivattom'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Palarivattom'):
                p=200
            elif (z == 'Pathadipalam' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Pathadipalam' and z=='JLN Stadium'):
                p=200
            elif (z == 'Pathadipalam' and y=='Kaloor'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Kaloor'):
                p=200
            elif (z == 'Pathadipalam' and y=='Town hall'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Town hall'):
                p=200
            elif (z == 'Pathadipalam' and y=='MG Road'):
                p=200 
            elif (y == 'Pathadipalam' and z=='MG Road'):
                p=200
            elif (z == 'Pathadipalam' and y=='Maharajas College'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Maharajas College'):
                p=200
            elif (z == 'Pathadipalam' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Ernakulam South'):
                p=200
            elif (z == 'Pathadipalam' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Kadavanthara'):
                p=200
            elif (z == 'Pathadipalam' and y=='Elamkulam'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Elamkulam'):
                p=200
            elif (z == 'Pathadipalam' and y=='Vytilla'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Vytilla'):
                p=200
            elif (z == 'Pathadipalam' and y=='Thykoodam'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Thykoodam'):
                p=200
            elif (z == 'Pathadipalam' and y=='Petta'):
                p=200 
            elif (y == 'Pathadipalam' and z=='Petta'):
                p=200
            elif (z == 'Edapally' and y=='Changampuzha park'):
                p=200 
            elif (y == 'Edapally' and z=='Changampuzha park'):
                p=200
            elif (z == 'Edapally' and y=='Palarivattom'):
                p=200 
            elif (y == 'Edapally' and z=='Palarivattom'):
                p=200
            elif (z == 'Edapally' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Edapally' and z=='JLN Stadium'):
                p=200
            elif (z == 'Edapally' and y=='Kaloor'):
                p=200 
            elif (y == 'Edapally' and z=='Kaloor'):
                p=200
            elif (z == 'Edapally' and y=='Town hall'):
                p=200 
            elif (y == 'Edapally' and z=='Town hall'):
                p=200
            elif (z == 'Edapally' and y=='MG Road'):
                p=200 
            elif (y == 'Edapally' and z=='MG Road'):
                p=200
            elif (z == 'Edapally' and y=='Maharajas College'):
                p=200 
            elif (y == 'Edapally' and z=='Maharajas College'):
                p=200
            elif (z == 'Edapally' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Edapally' and z=='Ernakulam South'):
                p=200
            elif (z == 'Edapally' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Edapally' and z=='Kadavanthara'):
                p=200
            elif (z == 'Edapally' and y=='Elamkulam'):
                p=200 
            elif (y == 'Edapally' and z=='Elamkulam'):
                p=200
            elif (z == 'Edapally' and y=='Vytilla'):
                p=200 
            elif (y == 'Edapally' and z=='Vytilla'):
                p=200
            elif (z == 'Edapally' and y=='Thykoodam'):
                p=200 
            elif (y == 'Edapally' and z=='Thykoodam'):
                p=200
            elif (z == 'Edapally' and y=='Petta'):
                p=200 
            elif (y == 'Edapally' and z=='Petta'):
                p=200
            elif (z == 'Changampuzha park' and y=='Palarivattom'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Palarivattom'):
                p=200
            elif (z == 'Changampuzha park' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Changampuzha park' and z=='JLN Stadium'):
                p=200
            elif (z == 'Changampuzha park' and y=='Kaloor'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Kaloor'):
                p=200
            elif (z == 'Changampuzha park' and y=='Town hall'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Town hall'):
                p=200
            elif (z == 'Changampuzha park' and y=='MG Road'):
                p=200 
            elif (y == 'Changampuzha park' and z=='MG Road'):
                p=200
            elif (z == 'Changampuzha park' and y=='Maharajas College'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Maharajas College'):
                p=200
            elif (z == 'Changampuzha park' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Ernakulam South'):
                p=200
            elif (z == 'Changampuzha park' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Kadavanthara'):
                p=200
            elif (z == 'Changampuzha park' and y=='Elamkulam'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Elamkulam'):
                p=200
            elif (z == 'Changampuzha park' and y=='Vytilla'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Vytilla'):
                p=200
            elif (z == 'Changampuzha park' and y=='Thykoodam'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Thykoodam'):
                p=200
            elif (z == 'Changampuzha park' and y=='Petta'):
                p=200 
            elif (y == 'Changampuzha park' and z=='Petta'):
                p=200
            elif (z == 'Palarivattom' and y=='JLN Stadium'):
                p=200 
            elif (y == 'Palarivattom' and z=='JLN Stadium'):
                p=200
            elif (z == 'Palarivattom' and y=='Kaloor'):
                p=200 
            elif (y == 'Palarivattom' and z=='Kaloor'):
                p=200
            elif (z == 'Palarivattom' and y=='Town hall'):
                p=200 
            elif (y == 'Palarivattom' and z=='Town hall'):
                p=200
            elif (z == 'Palarivattom' and y=='MG Road'):
                p=200 
            elif (y == 'Palarivattom' and z=='MG Road'):
                p=200
            elif (z == 'Palarivattom' and y=='Maharajas College'):
                p=200 
            elif (y == 'Palarivattom' and z=='Maharajas College'):
                p=200
            elif (z == 'Palarivattom' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Palarivattom' and z=='Ernakulam South'):
                p=200
            elif (z == 'Palarivattom' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Palarivattom' and z=='Kadavanthara'):
                p=200
            elif (z == 'Palarivattom' and y=='Elamkulam'):
                p=200 
            elif (y == 'Palarivattom' and z=='Elamkulam'):
                p=200
            elif (z == 'Palarivattom' and y=='Vytilla'):
                p=200 
            elif (y == 'Palarivattom' and z=='Vytilla'):
                p=200
            elif (z == 'Palarivattom' and y=='Thykoodam'):
                p=200 
            elif (y == 'Palarivattom' and z=='Thykoodam'):
                p=200
            elif (z == 'Palarivattom' and y=='Petta'):
                p=200 
            elif (y == 'Palarivattom' and z=='Petta'):
                p=200
            elif (z == 'JLN Stadium' and y=='Kaloor'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Kaloor'):
                p=200
            elif (z == 'JLN Stadium' and y=='Town hall'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Town hall'):
                p=200
            elif (z == 'JLN Stadium' and y=='MG Road'):
                p=200 
            elif (y == 'JLN Stadium' and z=='MG Road'):
                p=200
            elif (z == 'JLN Stadium' and y=='Maharajas College'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Maharajas College'):
                p=200
            elif (z == 'JLN Stadium' and y=='Ernakulam South'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Ernakulam South'):
                p=200
            elif (z == 'JLN Stadium' and y=='Kadavanthara'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Kadavanthara'):
                p=200
            elif (z == 'JLN Stadium' and y=='Elamkulam'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Elamkulam'):
                p=200
            elif (z == 'JLN Stadium' and y=='Vytilla'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Vytilla'):
                p=200
            elif (z == 'JLN Stadium' and y=='Thykoodam'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Thykoodam'):
                p=200
            elif (z == 'JLN Stadium' and y=='Petta'):
                p=200 
            elif (y == 'JLN Stadium' and z=='Petta'):
                p=200
            elif (z == 'Kaloor' and y=='Town hall'):
                p=200 
            elif (y == 'Kaloor' and z=='Town hall'):
                p=200
            elif (z == 'Kaloor' and y=='MG Road'):
                p=200 
            elif (y == 'Kaloor' and z=='MG Road'):
                p=200
            elif (z == 'Kaloor' and y=='Maharajas College'):
                p=200 
            elif (y == 'Kaloor' and z=='Maharajas College'):
                p=200
            elif (z == 'Kaloor' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Kaloor' and z=='Ernakulam South'):
                p=200
            elif (z == 'Kaloor' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Kaloor' and z=='Kadavanthara'):
                p=200
            elif (z == 'Kaloor' and y=='Elamkulam'):
                p=200 
            elif (y == 'Kaloor' and z=='Elamkulam'):
                p=200
            elif (z == 'Kaloor' and y=='Vytilla'):
                p=200 
            elif (y == 'Kaloor' and z=='Vytilla'):
                p=200
            elif (z == 'Kaloor' and y=='Thykoodam'):
                p=200 
            elif (y == 'Kaloor' and z=='Thykoodam'):
                p=200
            elif (z == 'Kaloor' and y=='Petta'):
                p=200 
            elif (y == 'Kaloor' and z=='Petta'):
                p=200
            elif (z == 'Town hall' and y=='MG Road'):
                p=200 
            elif (y == 'Town hall' and z=='MG Road'):
                p=200
            elif (z == 'Town hall' and y=='Maharajas College'):
                p=200 
            elif (y == 'Town hall' and z=='Maharajas College'):
                p=200
            elif (z == 'Town hall' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Town hall' and z=='Ernakulam South'):
                p=200
            elif (z == 'Town hall' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Town hall' and z=='Kadavanthara'):
                p=200
            elif (z == 'Town hall' and y=='Elamkulam'):
                p=200 
            elif (y == 'Town hall' and z=='Elamkulam'):
                p=200
            elif (z == 'Town hall' and y=='Vytilla'):
                p=200 
            elif (y == 'Town hall' and z=='Vytilla'):
                p=200
            elif (z == 'Town hall' and y=='Thykoodam'):
                p=200 
            elif (y == 'Town hall' and z=='Thykoodam'):
                p=200
            elif (z == 'Town hall' and y=='Petta'):
                p=200 
            elif (y == 'Town hall' and z=='Petta'):
                p=200
            elif (z == 'MG Road' and y=='Maharajas College'):
                p=200 
            elif (y == 'MG Road' and z=='Maharajas College'):
                p=200
            elif (z == 'MG Road' and y=='Ernakulam South'):
                p=200 
            elif (y == 'MG Road' and z=='Ernakulam South'):
                p=200
            elif (z == 'MG Road' and y=='Kadavanthara'):
                p=200 
            elif (y == 'MG Road' and z=='Kadavanthara'):
                p=200
            elif (z == 'MG Road' and y=='Elamkulam'):
                p=200 
            elif (y == 'MG Road' and z=='Elamkulam'):
                p=200
            elif (z == 'MG Road' and y=='Vytilla'):
                p=200 
            elif (y == 'MG Road' and z=='Vytilla'):
                p=200
            elif (z == 'MG Road' and y=='Thykoodam'):
                p=200 
            elif (y == 'MG Road' and z=='Thykoodam'):
                p=200
            elif (z == 'MG Road' and y=='Petta'):
                p=200 
            elif (y == 'MG Road' and z=='Petta'):
                p=200
            elif (z == 'Maharajas College' and y=='Ernakulam South'):
                p=200 
            elif (y == 'Maharajas College' and z=='Ernakulam South'):
                p=200
            elif (z == 'Maharajas College' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Maharajas College' and z=='Kadavanthara'):
                p=200
            elif (z == 'Maharajas College' and y=='Elamkulam'):
                p=200 
            elif (y == 'Maharajas College' and z=='Elamkulam'):
                p=200
            elif (z == 'Maharajas College' and y=='Vytilla'):
                p=200 
            elif (y == 'Maharajas College' and z=='Vytilla'):
                p=200
            elif (z == 'Maharajas College' and y=='Thykoodam'):
                p=200 
            elif (y == 'Maharajas College' and z=='Thykoodam'):
                p=200
            elif (z == 'Maharajas College' and y=='Petta'):
                p=200 
            elif (y == 'Maharajas College' and z=='Petta'):
                p=200
            elif (z == 'Ernakulam South' and y=='Kadavanthara'):
                p=200 
            elif (y == 'Ernakulam South' and z=='Kadavanthara'):
                p=200
            elif (z == 'Ernakulam South' and y=='Elamkulam'):
                p=200 
            elif (y == 'Ernakulam South' and z=='Elamkulam'):
                p=200
            elif (z == 'Ernakulam South' and y=='Vytilla'):
                p=200 
            elif (y == 'Ernakulam South' and z=='Vytilla'):
                p=200
            elif (z == 'Ernakulam South' and y=='Thykoodam'):
                p=200 
            elif (y == 'Ernakulam South' and z=='Thykoodam'):
                p=200
            elif (z == 'Ernakulam South' and y=='Petta'):
                p=200 
            elif (y == 'Ernakulam South' and z=='Petta'):
                p=200
            elif (z == 'Kadavanthara' and y=='Elamkulam'):
                p=200 
            elif (y == 'Kadavanthara' and z=='Elamkulam'):
                p=200
            elif (z == 'Kadavanthara' and y=='Vytilla'):
                p=200 
            elif (y == 'Kadavanthara' and z=='Vytilla'):
                p=200
            elif (z == 'Kadavanthara' and y=='Thykoodam'):
                p=200 
            elif (y == 'Kadavanthara' and z=='Thykoodam'):
                p=200
            elif (z == 'Kadavanthara' and y=='Petta'):
                p=200 
            elif (y == 'Kadavanthara' and z=='Petta'):
                p=200
            elif (z == 'Elamkulam' and y=='Vytilla'):
                p=200 
            elif (y == 'Elamkulam' and z=='Vytilla'):
                p=200
            elif (z == 'Elamkulam' and y=='Thykoodam'):
                p=200 
            elif (y == 'Elamkulam' and z=='Thykoodam'):
                p=200
            elif (z == 'Elamkulam' and y=='Petta'):
                p=200 
            elif (y == 'Elamkulam' and z=='Petta'):
                p=200
            elif (z == 'Vytilla' and y=='Thykoodam'):
                p=200 
            elif (y == 'Vytilla' and z=='Thykoodam'):
                p=200
            elif (z == 'Vytilla' and y=='Petta'):
                p=200 
            elif (y == 'Vytilla' and z=='Petta'):
                p=200
            elif (z == 'Thykoodam' and y=='Petta'):
                p=200 
            elif (y == 'Thykoodam' and z=='Petta'):
                p=200
            
            t=p*pa
            print(p * pa)
            d={'p':t,'x':x ,'a':us, 'l':l,'m':m,'n':n,'o':o,'x':x,'y':y,'z':z,'pa':pa,'q':q}
            return render(request,'billing.html',{'d':d})
        else:
            print("ERROR FORM INVALID")
    c={"i":z,"a":us}
    return render(request,'bookticket1.html',{'i':c})



def search(request):
    
        if request.method=='POST':
            d_src=request.POST['d_place']
            a_src=request.POST['a_place']
            print(d_src )
            if d_src and a_src:
                
                match=train_reg.objects.filter(Q(d_place__icontains=d_src) and Q(a_place__icontains=a_src))
                print(d_src)
                print(a_src)
                if match:
                
                    return render(request,'bookticket2.html',{'srh':match})
                else:
                    messages.error(request,"no result found")
                
            else:
                messages.error(request,"no result found")
        return render(request,'bookticket2.html')
    


def billings(request):
    if request.method=='POST':
        form=bill(request.POST)
        if form.is_valid():
            form.save()
            return submit(request)
        else:
            print("ERROR")
    return render(request,'billing.html')

def delete(request,pk):
    d=train_reg.objects.get(pk=pk)
    d.delete()
    return t_display(request)

def submit(request):
    return render(request,'submit.html') 
def bookticket2(request):
    if 'username' in request.session:
        us=request.session['username']
        return render(request,'bookticket2.html',{'us':us})
    return adminuser_login(request,)

def bookticket(request):
    return render(request,'bookticket.html')
def search1(request):
    
        if request.method=='POST':
            d_src=request.POST['d_place']
            a_src=request.POST['a_place']
            print(d_src )
            if d_src and a_src:
                
                match=train_reg.objects.filter(Q(d_place__icontains=d_src) and Q(a_place__icontains=a_src))
                print(d_src)
                print(a_src)
                if match:
                
                    return render(request,'bookticket.html',{'srh':match})
                else:
                    messages.error(request,"no result found")
                
            else:
                messages.error(request,"no result found")
        return render(request,'bookticket.html')
    




         