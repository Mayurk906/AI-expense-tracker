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