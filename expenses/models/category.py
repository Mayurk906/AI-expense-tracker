from django.db import models

from .base import BaseModel

class BaseCategory(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=20, default="#007bff")

    class Meta:
        abstract = True
        
class ExpenseCategory(BaseCategory):

    class Meta:
        ordering = ["name"]
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"

    def __str__(self):
        return self.name
    
class IncomeCategory(BaseCategory):

    class Meta:
        ordering = ["name"]
        verbose_name = "Income Category"
        verbose_name_plural = "Income Categories"

    def __str__(self):
        return self.name