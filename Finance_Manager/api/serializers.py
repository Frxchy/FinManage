from rest_framework import serializers
from .models import Bank, Account, Transaction, CreditCard, CreditCardTransaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'address', 'swift_code']

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = Account
        fields = ['id', 'user', 'bank', 'account_number', 'account_type', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'date', 'amount', 'description', 'category']

class CreditCardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = CreditCard
        fields = ['id', 'user', 'bank', 'card_number', 'expiration_date', 'cvv', 'limit', 'balance']

class CreditCardTransactionSerializer(serializers.ModelSerializer):
    credit_card = serializers.PrimaryKeyRelatedField(queryset=CreditCard.objects.all())

    class Meta:
        model = CreditCardTransaction
        fields = ['id', 'credit_card', 'date', 'amount', 'description', 'category']

