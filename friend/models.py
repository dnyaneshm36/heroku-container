# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
# Create your models here.
from django.conf import settings


class Myfrienddetail(models.Model):
    user     =                          models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name =                        models.CharField(max_length=30)
    last_name =                         models.CharField(max_length=30, blank=True, null=True)
    phone_number =                      models.CharField(max_length=10,blank=True, null=True)
    nick_name =                         models.CharField(max_length=10,blank=True, null=True)
    date_of_birth =                     models.DateField( default=datetime.date.today)
    email               =               models.EmailField( unique=True,null=True)
    
    def __str__(self):
        return self.first_name or ""
    
    class Meta:
        verbose_name = 'My friend detail'
        verbose_name_plural = 'My friends  details'