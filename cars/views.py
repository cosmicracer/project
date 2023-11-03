from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from .models import work
from .models import restore
from .models import buy

# Create your views here.

def firstpage(request):
    template = loader.get_template('firstpage.html')
    return HttpResponse(template.render())

def carrestore(request):
    template = loader.get_template('carrestore.html')
    return HttpResponse(template.render())

def carpaint(request):
    template = loader.get_template('carpaint.html')
    return HttpResponse(template.render())

def carsale1(request):
    template = loader.get_template('carsale1.html')
    return HttpResponse(template.render())

def carsale2(request):
    template = loader.get_template('carsale2.html')
    return HttpResponse(template.render())

def carsale3(request):
    template = loader.get_template('carsale3.html')
    return HttpResponse(template.render())

def carsale4(request):
    template = loader.get_template('carsale4.html')
    return HttpResponse(template.render())

def carsale5(request):
    template = loader.get_template('carsale5.html')
    return HttpResponse(template.render())

def carsale6(request):
    template = loader.get_template('carsale6.html')
    return HttpResponse(template.render())

def carpaint(request):
    mydata=work.objects.all()
    if(mydata!=""):
        return render(request,"carpaint.html",{"work":mydata}) 
    else:
        return render(request,"carpaint.html")
    
    
def addData(request):
        if request.method=="POST":
            name=request.POST["name"]
            mail=request.POST["mail"]
            inbox=request.POST["inbox"]

            obj=work()
            obj.name=name
            obj.mail=mail
            obj.inbox=inbox
            obj.save()
            mydata=work.objects.all()
            return redirect("carpaint")
        return render(request,"carpaint.html")


def carrestore(request):
    mydata=restore.objects.all()
    if(mydata!=""):
        return render(request,"carrestore.html",{"restore":mydata}) 
    else:
        return render(request,"carrestore.html")
    
    
def add(request):
        if request.method=="POST":
            name=request.POST["name"]
            mail=request.POST["mail"]
            inbox=request.POST["inbox"]

            obj=restore()
            obj.name=name
            obj.mail=mail
            obj.inbox=inbox
            obj.save()
            mydata=restore.objects.all()
            return redirect("carrestore")
        return render(request,"carrestore.html")

def carsale1(request):
    mydata=buy.objects.all()
    if(mydata!=""):
        return render(request,"carsale1.html",{"buy":mydata}) 
    else:
        return render(request,"carsale1.html")
    
def carsale2(request):
    mydata=buy.objects.all()
    if(mydata!=""):
        return render(request,"carsale2.html",{"buy":mydata}) 
    else:
        return render(request,"carsale2.html")
    
def carsale3(request):
    mydata=buy.objects.all()
    if(mydata!=""):
        return render(request,"carsale3.html",{"buy":mydata}) 
    else:
        return render(request,"carsale3.html")
    
def carsale4(request):
    mydata=buy.objects.all()
    if(mydata!=""):
        return render(request,"carsale4.html",{"buy":mydata}) 
    else:
        return render(request,"carsale4.html")
        
def carsale5(request):
    mydata=buy.objects.all()
    if(mydata!=""):
        return render(request,"carsale5.html",{"buy":mydata}) 
    else:
        return render(request,"carsale5.html")
            
def carsale6(request):
    mydata=buy.objects.all()
    if(mydata!=""):
        return render(request,"carsale6.html",{"buy":mydata}) 
    else:
        return render(request,"carsale6.html")
           
    
def sale(request):
        if request.method=="POST":
            name=request.POST["name"]
            mail=request.POST["mail"]
            inbox=request.POST["inbox"]

            obj=buy()
            obj.name=name
            obj.mail=mail
            obj.inbox=inbox
            obj.save()
            mydata=buy.objects.all()
            return redirect("firstpage")
        return render(request,"firstpage.html")

    







