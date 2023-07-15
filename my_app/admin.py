from django.contrib import admin
from .models import Contacts, GroupContacts

# Register your models here.
admin.site.register(Contacts)
admin.site.register(GroupContacts)
