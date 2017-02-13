from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
from cmdb import servers_status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    if request.method == 'POST':
        is_sign = request.POST.get("is_sign",None)
        if(is_sign == "1"):
            uname = request.POST.get("email",None)
            pswd = request.POST.get("pwd",None)
            models.UserInfo.objects.create(user=uname,pwd=pswd,email=uname)
            return render(request,'main.html')
        else:

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
    paginator = Paginator(user_list, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    print(page)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,"user_list.html", {"data": contacts})
