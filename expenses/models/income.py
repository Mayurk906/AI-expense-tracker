from django.core.validators import MinValueValidator
from django.db import models

from .base import BaseModel
from .category import IncomeCategory

INCOME_SOURCES = [
    ("SALARY", "Salary"),
    ("FREELANCING", "Freelancing"),
    ("BUSINESS", "Business"),
    ("INVESTMENT", "Investment"),
    ("BONUS", "Bonus"),
    ("OTHER", "Other"),
]

class Income(BaseModel):
    title = models.CharField(max_length=200)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    category = models.ForeignKey(
        IncomeCategory,
        on_delete=models.CASCADE,
        related_name="incomes"
    )

    source = models.CharField(
        max_length=20,
        choices=INCOME_SOURCES
    )

    income_date = models.DateField()

    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-income_date"]

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"