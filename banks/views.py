from typing import Any
from django.views.generic import ListView, DetailView
from .models import Bank, Branch
import json
from django.conf import settings


class BankHomeView(ListView):
    template_name = "banks/home.html"
    model = Bank
    context_object_name = "banks"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["branches"] = Branch.objects.all()

        banks = Bank.objects.values("id", "code", "name")

        # Process each bank to remove substrings from the name
        renamed_bank = [
            {
                "id": bank["id"],
                "code": bank["code"],
                "name": bank["name"]
                .replace("股份有限公司", "")
                .replace("有限公司", "")
                .strip(),
            }
            for bank in banks
        ]

        # Serialize the banks and branches querysets to JSON
        banks_json = json.dumps(renamed_bank)
        branches_json = json.dumps(
            list(
                Branch.objects.values(
                    "id",
                    "branch_name",
                    "bank_id",
                    "branch_code",
                    "address",
                    "telephone",
                )
            )
        )

        # Add the JSON serialized data to the context
        context["banks_json"] = banks_json
        context["branches_json"] = branches_json
        context["base_url"] = settings.BASE_URL

        return context


class BranchDetailView(DetailView):
    pass
