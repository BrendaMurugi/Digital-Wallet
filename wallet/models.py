from django.db import models

GENDER_CHOICES = (('Male','Male'),('Female','Female'))
NATIONALITIES_CHOICES = (('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'), ('American', 'American'), ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), ('Antiguans', 'Antiguans'), ('Argentinean', 'Argentinean'), ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Azerbaijani', 'Azerbaijani'), ('Bahamian', 'Bahamian'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'), ('Barbadian', 'Barbadian'), ('Barbudans', 'Barbudans'), ('Batswana', 'Batswana'), ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'), ('Beninese', 'Beninese'), ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'), ('British', 'British'), ('Bruneian', 'Bruneian'), ('Bulgarian', 'Bulgarian'), ('Burkinabe', 'Burkinabe'), ('Burmese', 'Burmese'), ('Burundian', 'Burundian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Cape Verdean', 'Cape Verdean'), ('Central African', 'Central African'), ('Chadian', 'Chadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Comoran', 'Comoran'), ('Congolese', 'Congolese'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'), ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Djibouti', 'Djibouti'), ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), ('Dutchman', 'Dutchman'), ('Dutchwoman', 'Dutchwoman'), ('East Timorese', 'East Timorese'), ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'), ('Emirian', 'Emirian'), ('Equatorial Guinean', 'Equatorial Guinean'), ('Eritrean', 'Eritrean'), ('Estonian', 'Estonian'), ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), ('Filipino', 'Filipino'), ('Finnish', 'Finnish'), ('French', 'French'), ('Gabonese', 'Gabonese'), ('Gambian', 'Gambian'), ('Georgian', 'Georgian'), ('German', 'German'), ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), ('Grenadian', 'Grenadian'), ('Guatemalan', 'Guatemalan'), ('Guinea-Bissauan', 'Guinea-Bissauan'), ('Guinean', 'Guinean'), ('Guyanese', 'Guyanese'), ('Haitian', 'Haitian'), ('Herzegovinian', 'Herzegovinian'), ('Honduran', 'Honduran'), ('Hungarian', 'Hungarian'), ('I-Kiribati', 'I-Kiribati'), ('Icelander', 'Icelander'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Ivorian', 'Ivorian'), ('Jamaican', 'Jamaican'), ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'), ('Kenyan', 'Kenyan'), ('Kittian and Nevisian', 'Kittian and Nevisian'), ('Kuwaiti', 'Kuwaiti'), ('Kyrgyz', 'Kyrgyz'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'), ('Liberian', 'Liberian'), ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), ('Lithuanian', 'Lithuanian'), ('Luxembourger', 'Luxembourger'), ('Macedonian', 'Macedonian'), ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'), ('Maldivan', 'Maldivan'), ('Malian', 'Malian'), ('Maltese', 'Maltese'), ('Marshallese', 'Marshallese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'), ('Mexican', 'Mexican'), ('Micronesian', 'Micronesian'), ('Moldovan', 'Moldovan'), ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Moroccan', 'Moroccan'), ('Mosotho', 'Mosotho'), ('Motswana', 'Motswana'), ('Mozambican', 'Mozambican'), ('Namibian', 'Namibian'), ('Nauruan', 'Nauruan'), ('Nepalese', 'Nepalese'), ('Netherlander', 'Netherlander'), ('New Zealander', 'New Zealander'), ('Ni-Vanuatu', 'Ni-Vanuatu'), ('Nicaraguan', 'Nicaraguan'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'), ('North Korean', 'North Korean'), ('Northern Irish', 'Northern Irish'), ('Norwegian', 'Norwegian'), ('Omani', 'Omani'), ('Pakistani', 'Pakistani'), ('Palauan', 'Palauan'), ('Panamanian', 'Panamanian'), ('Papua New Guinean', 'Papua New Guinean'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Rwandan', 'Rwandan'), ('Saint Lucian', 'Saint Lucian'), ('Salvadoran', 'Salvadoran'), ('Samoan', 'Samoan'), ('San Marinese', 'San Marinese'), ('Sao Tomean', 'Sao Tomean'), ('Saudi', 'Saudi'), ('Scottish', 'Scottish'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'), ('Seychellois', 'Seychellois'), ('Sierra Leonean', 'Sierra Leonean'), ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('Slovenian', 'Slovenian'), ('Solomon Islander', 'Solomon Islander'), ('Somali', 'Somali'), ('South African', 'South African'), ('South Korean', 'South Korean'), ('Spanish', 'Spanish'), ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Surinamer', 'Surinamer'), ('Swazi', 'Swazi'), ('Swedish', 'Swedish'), ('Swiss', 'Swiss'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('Tajik', 'Tajik'), ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Togolese', 'Togolese'), ('Tongan', 'Tongan'), ('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'), ('Tuvaluan', 'Tuvaluan'), ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Uruguayan', 'Uruguayan'), ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'), ('Welsh', 'Welsh'), ('Yemenite', 'Yemenite'), ('Zambian', 'Zambian'), ('Zimbabwean', 'Zimbabwean'))
EMPLOYMENT_CHOICES = (('Employed','Employed'),('Self-employed','Self-employed'),('Unemployed','Unemployed'))
CURRENCY_NAME_CHOICES = (('Kenya Shillings','Kenya Shillings'),('Uganda Shillings','Uganda Shillings'),('Rwanda Franc','Rwanda Franc'),('Tanzania Shillings','Tanzania Shillings'))
CURRENCY_CHOICES = (('KSh','KSh'),('USh','USh'),('RWF','RWF'),('TSh','TSh'))
COUNTRY_CHOICES = (('Kenya','Kenya'),('Uganda','Uganda'),('Rwanda','Rwanda'),('Tanzania','Tanzania'))
ACCOUNT_TYPE_CHOICES = (('Personal Account','Personal Account'),('Business Account','Business Account'))
RECEIPT_TYPE_CHOICES = (('Credit','Credit'),('Debit','Debit'))
TRANSACTION_TYPE_CHOICES = (('Credit','Credit'),('Debit','Debit'),('Payments','Payments'),('Wire transfer','Wire transfer'),('Loan repayment','Loan repayment'))
CARD_TYPE_CHOICES = (('Credit card','Credit card'),('Debit card','Debit card'),('Prepaid card','Prepaid card'))
LOAN_STATUS_CHOICE = (('Unpaid','Unpaid'),('Paid','Paid'))

class Customer(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email = models.EmailField()
    phone_number = models.CharField(max_length= 15)
    address = models.CharField(max_length=15)
    nationality = models.CharField(max_length=25,choices=NATIONALITIES_CHOICES,default='Kenyan',null=True)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES,null=True)
    age = models.PositiveSmallIntegerField()
    employment_status = models.CharField(max_length=24,choices=EMPLOYMENT_CHOICES,default='Select option',null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/',null=True)
    def __str__(self):
        return self.first_name

class Currency(models.Model):
    country = models.CharField(max_length=15,choices=COUNTRY_CHOICES,default='Kenya')
    currency_name = models.CharField(max_length=18,choices=CURRENCY_NAME_CHOICES,default='Kenya Shillings',null=True)
    symbol = models.CharField(max_length=15,choices=CURRENCY_CHOICES, default='KSh', null=True)
    def __str__(self):
        return self.symbol

class ThirdParty(models.Model):
    name = models.CharField(max_length=24)
    third_party_id = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length= 15)
    transaction_cost = models.PositiveIntegerField()    
    currency = models.ForeignKey('Currency',on_delete= models.CASCADE,related_name= 'Currency_thirdparty')
    account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Account_thirdparty')
    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=35,choices=TRANSACTION_TYPE_CHOICES)
    transaction_amount = models.IntegerField()
    transaction_cost = models.IntegerField()
    time = models.DateTimeField()
    origin_account = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Wallet_transaction')
    # third_party = models.ForeignKey('ThirdParty',on_delete=models.CASCADE,related_name='ThirdParty_transaction')
    destination_account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Account_transaction')    
    # receipt = models.ForeignKey('Receipt',on_delete=models.CASCADE,related_name='Receipt_transaction')

class Receipt(models.Model):
    # transaction = models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Transaction_receipt')
    receipt_type = models.CharField(max_length=24,choices=RECEIPT_TYPE_CHOICES)
    date_issued = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=100,decimal_places=2)
    receipt_file = models.FileField()

class Wallet(models.Model):
    wallet_name = models.CharField(max_length=24,null=True)
    customer = models.ForeignKey('Customer',on_delete = models.CASCADE,related_name = 'Customer_wallet')
    currency = models.ForeignKey('Currency',on_delete= models.CASCADE,related_name= 'Currency_wallet')
    balance = models.DecimalField(max_digits=100,decimal_places=2)
    date = models.DateTimeField()
    pin = models.SmallIntegerField()

class Account(models.Model):
    account_name = models.CharField(max_length=24)
    account_number = models.CharField(max_length=15)
    account_type = models.CharField(max_length=25,choices=ACCOUNT_TYPE_CHOICES)
    account_balance = models.DecimalField(max_digits=100,decimal_places=2)
    wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Wallet_account')
    def __str__(self):
        return self.account_name

class Card(models.Model):
    card_name = models.CharField(max_length=20,null= True)
    card_number = models.PositiveIntegerField(null = True)
    card_type = models.CharField(max_length= 14,choices=CARD_TYPE_CHOICES,null=True)
    expiry_date = models.DateTimeField(null = True,blank= True)
    is_active = models.BooleanField(default=False)
    cvv = models.SmallIntegerField(null= True)
    account = models.ForeignKey('Account',on_delete= models.CASCADE,related_name='Account_card')
    issuer = models.CharField(max_length= 12,null= True)
    def __str__(self):
        return self.card_name

class Notification(models.Model):
    recipient = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Customer_notification')     
    message = models.TextField(max_length=30)
    date_time = models.DateTimeField(null = True,blank= True)

class Loan(models.Model):
    amount = models.PositiveIntegerField()
    wallet = models.ForeignKey('Wallet',on_delete= models.CASCADE,related_name='wallet_loan')
    interest_rate = models.PositiveIntegerField()
    guarantee = models.ForeignKey('Customer',on_delete= models.CASCADE,related_name='Customer_loan')
    borrow_date_and_time=models.DateTimeField(null = True, blank= True)
    payment_due_date = models.DateTimeField(null = True,blank=True)
    loan_balance = models.PositiveIntegerField()
    loan_term = models.TextField()
    loan_status = models.CharField(max_length= 15,choices= LOAN_STATUS_CHOICE,default= "Unpaid",null= True)
    duration = models.PositiveIntegerField()

class Reward(models.Model):
    bonus = models.PositiveSmallIntegerField()
    transaction = models.ForeignKey('Transaction', on_delete= models.CASCADE,related_name='reward_transaction')
    wallet = models.ForeignKey('Wallet',on_delete= models.CASCADE,related_name='reward_wallet')
    date_time = models.DateField(null = True,blank= True)
