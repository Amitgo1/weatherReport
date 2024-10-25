from django.shortcuts import render,redirect
import random
import base64
import requests
import json
from home.models import LoginUser, LoginLogs
# Create your views here.

def generate_otp(phone):
    try:
        otp = random.randint(100000, 999999)
        url = f'https://2factor.in/API/V1/b15d39ca-9273-11ef-8b17-0200cd936042/SMS/+91{phone}/{otp}'
        response = requests.get(url)
        data = response.json()
        print('Generate OTP Response', data)
        print(otp)
        return otp
    except Exception as e:
        return None
    
def index(request):
    if "username" in request.session and request.session["username"]:
        return redirect("home")
    else:
        return redirect("login")

def login(request):
    if request.method == "POST":
        phone = request.POST.get("number")
        name = request.POST.get("name")
        if phone is None or name is None:
            return render(request, "home/login.html", {"message": "Invalid Request"})
        otp = generate_otp(phone)
        if otp is None:
            return render(request, "home/login.html", {"message": "Something went wrong"})
        
        users = LoginUser.objects.filter(username__iexact=name)
        if any(users):
            user = users.first()
            name = user.username
        else:
            user = LoginUser.objects.create(username=name, phoneno=phone)
        LoginLogs.objects.create(login_user=user, otp=otp)
        name = base64.b64encode(name.encode()).decode()
        return redirect("/verifyotp?u="+name)
    return render(request, "home/login.html")

    
def verify_otp(request):
    if request.method == "POST":
        username = request.GET.get("u")
        if username is None or not username:
            return render(request, "home/verify_otp.html", {"message": "Invalid Request"})
        username = base64.b64decode(username).decode()
        users = LoginUser.objects.filter(username=username)
        if not any(users):
            return render(request, "home/verify_otp.html", {"message": "Invalid Username"})
        user = users.first()
        logs = LoginLogs.objects.filter(login_user=user, is_used=False)
        if not any(logs):
            return render(request, "home/verify_otp.html", {"message": "Invalid OTP"})
        log = logs.first()
        user_otp = request.POST.get("otp")
        print(user_otp, log.otp, user.username)
        if str(log.otp) != str(user_otp):
            return render(request, "home/verify_otp.html", {"message": "Invalid OTP"})
        log.is_used = True
        log.save()
        user.is_verified = True
        user.save()
        request.session["username"] = user.username
        return redirect("home")
    return render(request, "home/verify_otp.html")

def logout(request):
    del request.session["username"]
    return redirect("login")

def home(request):
    if "username" in request.session and request.session["username"]:
        city = request.GET.get("city", "Noida")
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey=5IaUDUqGVZn3Ns1SXCfe2mW7htx9kthA"
        resp = requests.get(url)
        data = resp.json()
        user_data = data["timelines"]
        data = user_data["daily"]
        return render(request,"home/home.html", {"data":data, "city":city})
    else:
        return redirect("login")


    