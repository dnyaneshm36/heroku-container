# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Myfrienddetail
# Register your models here.

class MyfirendAdmin(admin.ModelAdmin):
    list_display= ['id','user','first_name','last_name','nick_name','email']
    # class Meta:
    #     model = Myfrienddetail





admin.site.register(Myfrienddetail, MyfirendAdmin)