# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from app_auth.models import Account
from Hello_Django import settings

class MyCustomBackend:

    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)

        if login_valid:
            try:
                user = Account.objects.get(username=username)
                if user.check_password(password):
                    user.is_staff = True
            except Account.DoesNotExist:
                try:
                    django_user = User.objects.get(username=user.username)
                except User.DoesNotExist:
                    #当在django中找不到此用户，便创建这个用户
                    django_user = User(username=user.username,password=user.password)
                    django_user.is_staff = True
                    django_user.is_superuser = True
                    django_user.save()
                return django_user
            return user
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
