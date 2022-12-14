from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers
from .views import AccountViewset, CardViewset, CustomerViewset, LoanViewset, NotificationViewset, ReceiptViewset, TransactionViewset, WalletViewset, AccountDepositView, AccountTransferView, AccountWithdrawalView, AccountLoanRequestView, AccountLoanRepaymentView, AccountBuyAirtimeView

router = routers.DefaultRouter()
router.register(r"customers",CustomerViewset)
router.register(r"wallets",WalletViewset)
router.register(r"accounts",AccountViewset)
router.register(r"cards",CardViewset)
router.register(r"transactions",TransactionViewset)
router.register(r"loans",LoanViewset)
router.register(r"receipts",ReceiptViewset)
router.register(r"notifications",NotificationViewset)

urlpatterns = [
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
    path("withdrawal/",AccountWithdrawalView.as_view(),name="withrawal-view"),
    path("loan_request/",AccountLoanRequestView.as_view(),name="loan-view"),
    path("loan_repayment/",AccountLoanRepaymentView.as_view(),name="repay-loan-view"),
    path("buy_airtime/",AccountBuyAirtimeView.as_view(),name="repay-loan-view"),
]