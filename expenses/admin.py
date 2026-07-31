from django.contrib import admin
from .models import ExpenseCategory,IncomeCategory,Expense,Income,Budget

class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("name",)
    
@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(BaseCategoryAdmin):
    pass


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(BaseCategoryAdmin):
    pass
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "amount",
        "category",
        "payment_method",
        "expense_date",
        "user",
    )

    search_fields = ("title",)

    list_filter = (
        "category",
        "payment_method",
        "expense_date",
    )

    ordering = ("-expense_date",)
@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "amount",
        "category",
        "source",
        "income_date",
        "user",
    )

    search_fields = ("title",)

    list_filter = (
        "category",
        "source",
        "income_date",
    )

    ordering = ("-income_date",)
    
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
        "amount",
        "month",
        "year",
        "user",
    )

    list_filter = (
        "month",
        "year",
        "category",
    )

    search_fields = (
        "category__name",
    )