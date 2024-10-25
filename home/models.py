from django.db import models

class LoginUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    phoneno = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)
    
    
class LoginLogs(models.Model):
    login_user = models.ForeignKey('LoginUser', on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_used = models.BooleanField(default=False)



