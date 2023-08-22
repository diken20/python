from django.shortcuts import render

# Create your views here.
def fee(request):
    return render(request,'fees/three.html',{'title':'DjangoFees','cname':'Django','charge':300})