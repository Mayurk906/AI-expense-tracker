from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

PAYMENT_METHODS = [
    ("CASH", "Cash"),
    ("UPI", "UPI"),
    ("DEBIT_CARD", "Debit Card"),
    ("CREDIT_CARD", "Credit Card"),
    ("NET_BANKING", "Net Banking"),
]

INCOME_SOURCES = [
    ("SALARY", "Salary"),
    ("FREELANCING", "Freelancing"),
    ("BUSINESS", "Business"),
    ("INVESTMENT", "Investment"),
    ("BONUS", "Bonus"),
    ("OTHER", "Other"),
]
class BaseModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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