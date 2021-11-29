from django.contrib import admin
from .models import HallDetail,UserProfile,Feedback

class user(admin.ModelAdmin):
    list_display = ('profile','list')

class hall(admin.ModelAdmin):
    list_display = ('name','location')

class feed(admin.ModelAdmin):
    list_display = ('username','feedback')


admin.site.register(HallDetail,hall)
admin.site.register(UserProfile,user)
admin.site.register(Feedback,feed)
