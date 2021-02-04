from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-

import json
from django.db import models
from django.conf import settings
# Create your models here.


def upload_update_image(instance,filename):
    return "status/{user}/{filename}".format(user=instance.user, filename =filename)


class StatusQuerySet(models.QuerySet):
    #def serialize(self):
     #   qs = self
      #  return serialize('json',qs,fields= ('user','content','image',"id"))
    # def serialize(self):
    #     list_values = list(self.values("id","user","content","image"))
    #     return json.dumps(list_values)
    pass


class StatusManager(models.Manager):
    def  get_queryset(self):
        return StatusQuerySet(self.model,using=self._db)


class Status(models.Model):
    user     =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content  =models.TextField(blank=True, null=True)
    image    = models.ImageField(upload_to="upload_update_image",blank=True, null=True)
    updated  = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return str(self.content)[:50]or ""
    class Meta:
        verbose_name = 'status post'
        verbose_name_plural = 'Status posts'

    def serialize(self):
        try:
            image = self.image.url
        except:  
            image = ""
        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image
        }
        data = json.dumps(data)
        return data
    @property
    def owner(self):
        return self.user
    