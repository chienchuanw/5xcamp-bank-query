from django.urls import path
from .views import BankHomeView

app_name = "banks"

urlpatterns = [
    path("", BankHomeView.as_view(), name="home"),
    path(
        "<str:bank_code>/<str:branch_code>/<str:bank_name>-<str:branch_name>.html",
        BankHomeView.as_view(),
        name="detail",
    ),
]
