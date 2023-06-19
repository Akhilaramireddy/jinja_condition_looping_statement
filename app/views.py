from django.shortcuts import render

# Create your views here
def wish(request):
    d={'name':'akhila','age':21}
    return render(request,'wish.html',context=d)

def conditions(request):
    d={'a':20 ,'b':50,'c':40 }
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'ANIL'}
    return render(request,'loop.html',d)



