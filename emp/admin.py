from django.contrib import admin
from .models import EMP
# Register your models here.
class adminEMP(admin.ModelAdmin):
    list_display=('name','working')
    
admin.site.register(EMP,adminEMP)

