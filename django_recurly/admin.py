from django.contrib import admin

from . import models


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_code',)
    search_fields = ('=user__id', '=account_code')
    raw_id_fields = ('user',)


admin.site.register(models.Account, AccountAdmin)
