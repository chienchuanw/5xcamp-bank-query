from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from django.views.generic import FormView, ListView
from .models import Bank
from .forms import BankSearchForm


class BankHomeView(ListView):
    template_name = "banks/home.html"
    model = Bank
    context_object_name = "banks"
