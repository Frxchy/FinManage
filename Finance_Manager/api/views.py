from rest_framework import generics
from .models import Bank, Account, Transaction, CreditCard, CreditCardTransaction
from .serializers import BankSerializer, AccountSerializer, TransactionSerializer, CreditCardSerializer, CreditCardTransactionSerializer

class BankListCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CreditCardListCreateView(generics.ListCreateAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CreditCardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CreditCardTransactionListCreateView(generics.ListCreateAPIView):
    queryset = CreditCardTransaction.objects.all()
    serializer_class = CreditCardTransactionSerializer

class CreditCardTransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditCardTransaction.objects.all()
    serializer_class = CreditCardTransactionSerializer
