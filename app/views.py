from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        To.save()
        return HttpResponse('Topic insertion is successfully')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']
        To=Topic.objects.get(topic_name=tn)

        Wo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url,email=email)[0]
        Wo.save()
        return HttpResponse('Webpage insertion is successfull')

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']

        Wo=Webpage.objects.get(name=name)
        
        Ao=AccessRecord.objects.get_or_create(name=Wo,author=author,date=date)[0]
        Ao.save()
        return HttpResponse('AccessRecord insertion is successfull')
    return render(request,'insert_accessrecord.html')

def retrive_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrive_data.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)

def radio_button(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'radio_button.html',d)