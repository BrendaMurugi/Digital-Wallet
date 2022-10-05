from django.contrib import admin
from .models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class WalletAdmin(admin.ModelAdmin):
    list_display = ('wallet_name', 'balance')
    search_fields = ('wallet_name', 'balance')

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country', 'currency_name', 'symbol')
    search_fields = ('currency_name', 'symbol')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'account_balance')
    search_fields = ('account_name',)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'third_party_id')
    search_fields = ('name',) 

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('date_issued', 'total_amount')
    search_fields = ('date_issued', 'total_amount')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount','origin_account','destination_account')
    search_fields = ('amount','origin_account','destination_account')

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'card_number')
    search_fields = ('card_name', 'card_number')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message')
    search_fields = ('recipient',)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('amount', 'wallet', 'guarantee')
    search_fields = ('amount', 'wallet', 'guarantee')

class RewardAdmin(admin.ModelAdmin):
    list_display = ('bonus',)
    search_fields = ('bonus',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Reward,RewardAdmin)