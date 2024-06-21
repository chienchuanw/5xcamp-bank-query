from django.shortcuts import render
from django.views.generic import TemplateView


class BankHomeView(TemplateView):
    template_name = "banks/home.html"
