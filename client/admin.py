from django.contrib import admin

# Register your models here.

from .models import Site
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    filter_horizontal = ['users']

admin.site.register(Site)
admin.site.register(Account, AccountAdmin)