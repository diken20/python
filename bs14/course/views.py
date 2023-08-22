from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn(request):


    
    return render(request,'course/one.html',{'nm':'Django'})