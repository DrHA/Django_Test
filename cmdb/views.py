from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
from cmdb import servers_status



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
    free_m = servers_status.server_status()
    print(free_m)
    return render(request,"servers.html",{"data":free_m})

def log(request):
    return render(request,"log.html","")

def scripts(request):
    return render(request,"scripts.html","")

def config(request):
    return render(request,"config.html","")

def mails(request):
    return render(request,"mails.html","")

def server_list(request):
    ser_list = models.Server_list.objects.all()
    return render(request,"server_list.html", {"data": ser_list})

def user_list(request):
    user_list = models.UserInfo.objects.all()
    return render(request,"user_list.html", {"data": user_list})
