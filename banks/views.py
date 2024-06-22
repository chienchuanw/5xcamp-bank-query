from typing import Any
from django.views.generic import ListView
from .models import Bank, Branch
import json


class BankHomeView(ListView):
    template_name = "banks/home.html"
    model = Bank
    context_object_name = "banks"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["branches"] = Branch.objects.all()

        # Serialize the banks and branches querysets to JSON
        banks_json = json.dumps(list(Bank.objects.values("id", "code", "name")))
        branches_json = json.dumps(
            list(Branch.objects.values("id", "branch_name", "bank_id"))
        )

        # Add the JSON serialized data to the context
        context["banks_json"] = banks_json
        context["branches_json"] = branches_json

        return context
