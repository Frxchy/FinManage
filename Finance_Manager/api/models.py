from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    swift_code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('savings', 'Savings'),
        ('checking', 'Checking'),
        ('credit', 'Credit'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.account.account_number} - {self.amount} - {self.date}"

class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_cards')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='credit_cards')
    card_number = models.CharField(max_length=20, unique=True)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    limit = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.card_number}"

class CreditCardTransaction(models.Model):
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.credit_card.card_number} - {self.amount} - {self.date}"
    
