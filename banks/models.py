from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}{self.branch_name}"
