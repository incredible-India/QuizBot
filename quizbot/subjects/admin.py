from django.contrib import admin

from .models import Misc
# Register your models here.
@admin.register(Misc)
class MiscAdmin(admin.ModelAdmin):
    list_display = ['id','question','slug','op1','op2','op3','op4']
# Register your models here.
