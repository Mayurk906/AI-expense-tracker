from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..services.dashboard import get_dashboard_data
from django.db.models import Sum
from ..models import Income, Expense, Budget
from django.db.models.functions import ExtractMonth
@login_required
def dashboard_view(request):

    # Total Income
    total_income = (
        Income.objects.filter(
            user=request.user
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    # Total Expense
    total_expense = (
        Expense.objects.filter(
            user=request.user
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0
    )

    # Current Balance
    balance = total_income - total_expense

    # Latest Budget
    current_budget = (
        Budget.objects.filter(
            user=request.user
        )
        .order_by("-year", "-month")
        .first()
    )

    # Recent Expenses
    recent_expenses = (
        Expense.objects.filter(
            user=request.user
        )
        .select_related("category")
        .order_by("-expense_date")[:5]
    )
    
    category_totals = (
        Expense.objects.filter(
            user=request.user
        )
        .values("category__name")
        .annotate(
            total=Sum("amount")
        )
        .order_by("-total")
    )
    
    monthly_expenses = (
        Expense.objects.filter(
            user=request.user
        )
        .annotate(
            month=ExtractMonth("expense_date")
        )
        .values("month")
        .annotate(
            total=Sum("amount")
        )
        .order_by("month")
    )

    context = {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "current_budget": current_budget,
        "recent_transactions": recent_expenses,
        "category_totals": category_totals,
        "monthly_expenses": monthly_expenses,


    }

    return render(
        request,
        "expenses/dashboard/dashboard.html",
        context,
    )