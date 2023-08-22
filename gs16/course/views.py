from django.shortcuts import render

# Create your views here.
def learn(request):
    return render(request,'course/one.html',{'title':'learn Django','cname':'Django'})