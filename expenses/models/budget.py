from django.core.validators import MinValueValidator
from django.db import models

from .base import BaseModel
from .category import ExpenseCategory

class Budget(BaseModel):

    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="budgets"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    MONTH_CHOICES = [
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
    ]

    month = models.PositiveSmallIntegerField(
        choices=MONTH_CHOICES
    )

    year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["-year", "-month"]
        unique_together = ("user", "category", "month", "year")

    def __str__(self):
        if self.category:
            return f"{self.category.name} Budget ({self.month}/{self.year})"

        return f"Overall Budget ({self.month}/{self.year})"