from django.contrib import admin
from .models import LoginUser, LoginLogs

admin.site.register(LoginUser)
admin.site.register(LoginLogs)
