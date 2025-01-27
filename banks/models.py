from django.db import models


class Bank(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    update_date = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    announcement_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="branches")
    branch_code = models.CharField(max_length=10)
    branch_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    manager = models.CharField(max_length=100, null=True, blank=True)
    update_date = models.DateField(null=True, blank=True)
    announcement_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self) -> str:
        return f"{self.branch_code} - {self.branch_name}"
