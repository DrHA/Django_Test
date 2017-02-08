from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models



def index(request):
    if request.method == 'POST':
        uname = request.POST.get("uname",None)
        pswd = request.POST.get("pswd",None)
        is_sign = request.POST.get("is_sign",None)
        print(is_sign)
        if is_sign == "1":
            return render(request,'sign.html')
        print(uname,pswd)
        models.UserInfo.objects.create(user=uname,pwd=pswd)
        return render(request,'main.html')
    # request.GET
    # return HttpResponse("My First Django")
    userlist = models.UserInfo.objects.all()
    return render(request,"index.html", {"data": userlist})
# Create your views here.

def main(request):
    return render(request,"main.html","")

def sign(request):
    return render(request,"sign.html","")

def servers(request):
    return render(request,"servers.html","")