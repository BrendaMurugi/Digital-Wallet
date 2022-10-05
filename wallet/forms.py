from django import forms
from .import models

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ("first_name","last_name","age","email","phone_number","address","nationality","gender","employment_status","profile_picture")
        widgets = {
            "first_name":forms.TextInput(attrs={'placeholder': 'Enter your first name','class': "form-control"}),
            "last_name":forms.TextInput(attrs={'placeholder': 'Enter your last name','class': "form-control"}),
            "age":forms.TextInput(attrs={'placeholder': 'Enter your age','class': "form-control"}),
            "email":forms.TextInput(attrs={'placeholder': 'Enter your email','class': "form-control"}),
            "phone_number":forms.TextInput(attrs={'placeholder': 'Enter your phone number','class': "form-control"}),
            "address":forms.TextInput(attrs={'placeholder': 'Enter your address','class': "form-control"}),
            "nationality":forms.Select(attrs={'class': "form-control"}),
            "gender":forms.Select(attrs={'class': "form-control"}),
            "employment_status":forms.Select(attrs={'class': "form-control"}),
         }

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Wallet
        fields = ("wallet_name","customer","currency","balance","date","pin")
        widgets = {
            "wallet_name":forms.TextInput(attrs={'placeholder': 'Enter your wallet name','class': "form-control"}),
            "customer":forms.Select(attrs={'class': "form-control"}),
            "currency":forms.Select(attrs={'class': "form-control"}),
            "balance":forms.TextInput(attrs={'class': "form-control"}),
            "date":forms.TextInput(attrs={'class': "form-control"}),
            "pin":forms.TextInput(attrs={'placeholder': 'Enter your pin','class': "form-control"}),
        }

class CurrencyRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = ("country","currency_name","symbol")
        widgets = {
            "country":forms.Select(attrs={'class': "form-control"}),
            "currency_name":forms.Select(attrs={'class': "form-control"}),
            "symbol":forms.Select(attrs={'class': "form-control"})
        }

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ("account_name","account_number","account_type","account_balance","wallet")
        widgets = {
            "account_name":forms.TextInput(attrs={'placeholder': 'Enter account name','class': "form-control"}),
            "account_number":forms.TextInput(attrs={'class': "form-control"}),
            "account_type":forms.Select(attrs={'class': "form-control"}),
            "account_balance":forms.TextInput(attrs={'class': "form-control"}),
            "wallet":forms.Select(attrs={'class': "form-control"}),
        }

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.ThirdParty
        fields = ("name","third_party_id","is_active","email","phone_number","transaction_cost","currency","account")
        widgets = {
            "name":forms.TextInput(attrs={'placeholder': 'Enter third-party name','class': "form-control"}),
            "third_party_id":forms.TextInput(attrs={'placeholder': 'Enter third-party id','class': "form-control"}),
            "is_active":forms.CheckboxInput(attrs={'class': "form-control"}),
            "email":forms.TextInput(attrs={'placeholder': 'Enter your email','class': "form-control"}),
            "phone_number":forms.TextInput(attrs={'placeholder': 'Enter your phone number','class': "form-control"}),
            "transaction_cost":forms.TextInput(attrs={'placeholder': 'Enter transaction cost','class': "form-control"}),
            "currency":forms.Select(attrs={'class': "form-control"}),
            "account":forms.Select(attrs={'class': "form-control"}),
        }

class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Receipt
        fields = ("receipt_type","date_issued","total_amount","receipt_file")
        widgets = {
            "receipt_type":forms.Select(attrs={'class': "form-control"}),
            "date_issued":forms.TextInput(attrs={'class': "form-control"}),
            "total_amount":forms.TextInput(attrs={'class': "form-control"}),
            "receipt_file":forms.Select(attrs={'class': "form-control"}),
        }

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ("amount","transaction_type","transaction_cost","time","origin_account","destination_account","receipt")
        widgets = {
            "amount":forms.TextInput(attrs={'placeholder': 'Enter amount to transact','class': "form-control"}),
            "transaction_type":forms.Select(attrs={'class': "form-control"}),
            "transaction_cost":forms.TextInput(attrs={'placeholder': 'Enter transaction cost','class': "form-control"}),
            "time":forms.TextInput(attrs={'class': "form-control"}),
            "origin_account":forms.Select(attrs={'class': "form-control"}),
            "destination_account":forms.Select(attrs={'class': "form-control"}),
            "receipt":forms.Select(attrs={'class': "form-control"}),
        }

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Card
        fields = ("card_name","card_number","card_type","expiry_date","is_active","cvv","account","issuer")
        widgets = {
            "card_name":forms.TextInput(attrs={'placeholder': 'Enter card name','class': "form-control"}),
            "card_number":forms.TextInput(attrs={'placeholder': 'Enter card number','class': "form-control"}),
            "card_type":forms.Select(attrs={'class': "form-control"}),
            "expiry_date":forms.TextInput(attrs={'class': "form-control"}),
            "is_active":forms.CheckboxInput(attrs={'class': "form-control"}),
            "cvv":forms.TextInput(attrs={'placeholder': 'Enter cvv','class': "form-control"}),
            "account":forms.Select(attrs={'class': "form-control"}),
            "issuer":forms.TextInput(attrs={'placeholder': 'Enter issuer','class': "form-control"}),
        }

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Notification
        fields = ("recipient","message","date_time")
        widgets = {
            "recipient":forms.Select(attrs={'class': "form-control"}),
            "message":forms.TextInput(attrs={'placeholder': 'Enter notification message','class': "form-control"}),
            "date_time":forms.TextInput(attrs={'class': "form-control"})
        }

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Loan
        fields = ("amount","wallet","interest_rate","guarantee","borrow_date_and_time","payment_due_date","loan_balance","loan_term","loan_status","duration")
        widgets = {
            "amount":forms.TextInput(attrs={'placeholder': 'Enter amount to borrow','class': "form-control"}),
            "wallet":forms.Select(attrs={'class': "form-control"}),
            "interest_rate":forms.TextInput(attrs={'class': "form-control"}),
            "guarantee":forms.Select(attrs={'class': "form-control"}),
            "borrow_date_and_time":forms.TextInput(attrs={'class': "form-control"}),
            "payment_due_date":forms.TextInput(attrs={'class': "form-control"}),
            "loan_balance":forms.TextInput(attrs={'class': "form-control"}),
            "loan_term":forms.TextInput(attrs={'placeholder': 'Enter loan terms','class': "form-control"}),
            "loan_status":forms.Select(attrs={'class': "form-control"}),
            "duration":forms.TextInput(attrs={'class': "form-control"})
        }

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Reward
        fields = ("bonus","transaction","wallet","date_time")
        widgets = {
            "bonus":forms.TextInput(attrs={'class': "form-control"}),
            "transaction":forms.Select(attrs={'class': "form-control"}),
            "wallet":forms.Select(attrs={'class': "form-control"}),
            "date_time":forms.TextInput(attrs={'class': "form-control"}),
        }