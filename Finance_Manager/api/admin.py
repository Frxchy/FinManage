from django.contrib import admin
from .models import Bank, Account, Transaction, CreditCard, CreditCardTransaction

# Register your models here.
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(CreditCard)
admin.site.register(CreditCardTransaction)