from django.db.models import Sum

from ..models import Expense, Income
from itertools import chain

from ..models import Expense, Income


def get_recent_transactions(user, limit=5):

    expenses = (
        Expense.objects.filter(user=user)
        .select_related("category")
    )

    incomes = (
        Income.objects.filter(user=user)
        .select_related("category")
    )

    transactions = sorted(
        chain(expenses, incomes),
        key=lambda x: x.created_at,
        reverse=True,
    )

    return transactions[:limit]


def get_dashboard_data(user):

    total_income = (
        Income.objects.filter(user=user)
        .aggregate(total=Sum("amount"))["total"]
        or 0
    )

    total_expense = (
        Expense.objects.filter(user=user)
        .aggregate(total=Sum("amount"))["total"]
        or 0
    )

    balance = total_income - total_expense

    recent_expenses = (
        Expense.objects.filter(user=user)
        .select_related("category")
        .order_by("-expense_date")[:5]
    )

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "recent_transactions": get_recent_transactions(user),
}
    