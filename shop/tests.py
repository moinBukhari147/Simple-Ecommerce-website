from django.shortcuts import render

from django.contrib.auth.models import User
all_users = User.objects.values()
print(all_users)
print(all_users[0]['username'])
