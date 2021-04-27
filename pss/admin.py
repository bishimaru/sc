from django.contrib import admin
from .models import Data, TotalPay

class DataAdmin(admin.ModelAdmin):
    list_display = ('store_name','name','date','number','bigbonus','regularbonus','count','payout','memo')
admin.site.register(Data, DataAdmin)

class TotalAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_pay')
admin.site.register(TotalPay, TotalAdmin)



