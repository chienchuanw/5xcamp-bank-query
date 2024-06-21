from django.urls import path
from .views import BankHomeView

app_name = "banks"

urlpatterns = [
    path("", BankHomeView.as_view(), name="home"),
]
