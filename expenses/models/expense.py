from django.core.validators import MinValueValidator
from django.db import models

from .base import BaseModel
from .category import ExpenseCategory

PAYMENT_METHODS = [
    ("CASH", "Cash"),
    ("UPI", "UPI"),
    ("DEBIT_CARD", "Debit Card"),
    ("CREDIT_CARD", "Credit Card"),
    ("NET_BANKING", "Net Banking"),
]

class Expense(BaseModel):
    title = models.CharField(max_length=200)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )   

    expense_date = models.DateField()

    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["-expense_date"]

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"