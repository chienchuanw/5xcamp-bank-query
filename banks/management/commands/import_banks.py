from django.core.management.base import BaseCommand, CommandParser
from banks.models import Bank, Branch
import pandas
import os
from django.conf import settings


class Command(BaseCommand):
    help = "Import bank information from a CSV file"

    # Define CLI parameters
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "csv_file", type=str, nargs="?", default="data/financial_institutions.csv"
        )

    def handle(self, *args, **kwargs):
        # Provide CSV path and load data
        csv_file = os.path.join(settings.BASE_DIR, kwargs["csv_file"])
        data = pandas.read_csv(csv_file)

        # Delete all existing data before import new data
        Bank.objects.all().delete()
        Branch.objects.all().delete()

        # Import data from designated CSV
        for _, row in data.iterrows():
            try:
                if pandas.isna(row["機構代號"]):
                    bank, created = Bank.objects.get_or_create(
                        code=row["總機構代號"],
                        defaults={"name": row["機構名稱"]},
                        address=(row["地址"] if not pandas.isna(row["地址"]) else ""),
                        telephone=(row["電話"] if not pandas.isna(row["電話"]) else ""),
                        website=(
                            row["金融機構網址"]
                            if not pandas.isna(row["金融機構網址"])
                            else ""
                        ),
                        announcement_date=pandas.to_datetime(
                            row["公告日期"], errors="coerce"
                        ),
                    )
                else:
                    try:
                        bank = Bank.objects.get(code=row["總機構代號"])
                    except Bank.DoesNotExist:
                        self.stderr.write(
                            f"Bank code: {row['總機構代號']} does not exist."
                        )
                        continue

                    Branch.objects.create(
                        bank=bank,
                        branch_code=row["機構代號"],
                        branch_name=row["機構名稱"],
                        address=row["地址"],
                        telephone=row["電話"],
                        manager=row["負責人"] if not pandas.isna(row["負責人"]) else "",
                        update_date=pandas.to_datetime(
                            row["異動日期"], errors="coerce"
                        ),
                        announcement_date=pandas.to_datetime(
                            row["公告日期"], errors="coerce"
                        ),
                    )
            except Bank.DoesNotExist:
                self.stderr.write(f"Bank code: {row['總機構代號']} does not exist")
            except Exception:
                self.stderr.write(f"Failed to import row: {row} due to {Exception}")

        self.stdout.write(self.style.SUCCESS("Successfully imported"))
