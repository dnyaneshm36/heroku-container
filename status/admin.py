from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display= ['id','user', '__str__', 'image']
    # class Meta:
    #     model = Status

    #forms = StatusForm



admin.site.register(Status, StatusAdmin)