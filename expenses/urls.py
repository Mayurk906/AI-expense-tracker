from django.urls import path

from .views.auth import login_view, logout_view, register_view
from .views.dashboard import dashboard_view
from .views.expense import ExpenseListView
from .views.expense import ExpenseCreateView,ExpenseUpdateView,ExpenseDeleteView

urlpatterns = [
    path("", dashboard_view, name="dashboard"),

    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path( "expenses/", ExpenseListView.as_view(), name="expense-list"),
    path("expenses/add/",ExpenseCreateView.as_view(),name="expense-add"),
    path( "expenses/<int:pk>/edit/", ExpenseUpdateView.as_view(), name="expense-edit"),
    path( "expenses/<int:pk>/delete/", ExpenseDeleteView.as_view(), name="expense-delete"),
]