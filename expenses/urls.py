from django.urls import path

from .views.auth import login_view, logout_view, register_view
from .views.dashboard import dashboard_view
from .views.expense import ExpenseListView
from .views.expense import ExpenseCreateView,ExpenseUpdateView,ExpenseDeleteView
from .views.income import (
    IncomeListView,
    IncomeCreateView,
    IncomeUpdateView,
    IncomeDeleteView,
)
from .views.budget import BudgetListView, BudgetCreateView, BudgetUpdateView, BudgetDeleteView
urlpatterns = [
    path("", dashboard_view, name="dashboard"),

    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path( "expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("expenses/add/",ExpenseCreateView.as_view(),name="expense-add"),
    path( "expenses/<int:pk>/edit/", ExpenseUpdateView.as_view(), name="expense-edit"),
    path( "expenses/<int:pk>/delete/", ExpenseDeleteView.as_view(), name="expense-delete"),
    path("income/",IncomeListView.as_view(),name="income-list"),
    path("income/add/",IncomeCreateView.as_view(),name="income-add"),
    path("income/<int:pk>/edit/",IncomeUpdateView.as_view(),name="income-edit"),
    path("income/<int:pk>/delete/",IncomeDeleteView.as_view(),name="income-delete"),
    path("budget/", BudgetListView.as_view(), name="budget-list"),
    path("budget/add/", BudgetCreateView.as_view(), name="budget-add"),
    path("budget/<int:pk>/edit/", BudgetUpdateView.as_view(), name="budget-edit"),
    path("budget/<int:pk>/delete/", BudgetDeleteView.as_view(), name="budget-delete"),
]