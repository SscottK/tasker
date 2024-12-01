from django.contrib import admin
from .models import Checklist, Listitem, List_user, Reminder

# Register your models here.
admin.site.register(Checklist)
admin.site.register(Listitem)
admin.site.register(List_user)
admin.site.register(Reminder)