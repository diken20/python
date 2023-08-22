from django.shortcuts import render


# Create your views here.
def fesslearn(request):
    return render(request,'fees/three.html')