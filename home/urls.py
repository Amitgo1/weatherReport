from home.views import index, login, verify_otp, home, logout
from django.urls import path

urlpatterns = [
    path('',index, name="index"),
    path('login',login, name="login"),
    path('verifyotp',verify_otp, name="verify_otp"),
    path('home', home, name='home'),
    path('logout', logout, name="logout")
    
]
