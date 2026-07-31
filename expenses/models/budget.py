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

    month = models.PositiveSmallIntegerField()

    year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["-year", "-month"]
        unique_together = ("user", "category", "month", "year")

    def __str__(self):
        if self.category:
            return f"{self.category.name} Budget ({self.month}/{self.year})"

        return f"Overall Budget ({self.month}/{self.year})"