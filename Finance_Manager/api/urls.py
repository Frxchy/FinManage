from django.urls import path
from .views import (
    BankListCreateView, BankDetailView,
    AccountListCreateView, AccountDetailView,
    TransactionListCreateView, TransactionDetailView,
    CreditCardListCreateView, CreditCardDetailView,
    CreditCardTransactionListCreateView, CreditCardTransactionDetailView
)

urlpatterns = [
    path('banks/', BankListCreateView.as_view(), name='bank-list-create'),
    path('banks/<int:pk>/', BankDetailView.as_view(), name='bank-detail'),
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('credit-cards/', CreditCardListCreateView.as_view(), name='credit-card-list-create'),
    path('credit-cards/<int:pk>/', CreditCardDetailView.as_view(), name='credit-card-detail'),
    path('credit-card-transactions/', CreditCardTransactionListCreateView.as_view(), name='credit-card-transaction-list-create'),
    path('credit-card-transactions/<int:pk>/', CreditCardTransactionDetailView.as_view(), name='credit-card-transaction-detail'),
]
