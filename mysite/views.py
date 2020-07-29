import json
import requests
from django.shortcuts import render
from .models import Job, Contact
# Create your views here.
def index(request):
    return render(request,'mysite/index.html')
def mywork(request):
    jobs=Job.objects
    return render(request,'mysite/mywork.html',{'jobs':jobs})
def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')
    return render(request,'mysite/contact.html')