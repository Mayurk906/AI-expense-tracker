from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from ..models import Budget
from ..forms.budget import BudgetForm
from django.db.models import Sum
from ..models import Budget, Expense


class BudgetListView(LoginRequiredMixin, ListView):

    model = Budget

    template_name = "expenses/budget/list.html"

    context_object_name = "budgets"

    def get_queryset(self):

        return (
            Budget.objects.filter(user=self.request.user)
            .select_related("category")
        )
        
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for budget in context["budgets"]:

            spent = (
                Expense.objects.filter(
                    user=self.request.user,
                    category=budget.category,
                    expense_date__month=budget.month,
                    expense_date__year=budget.year,
                )
                .aggregate(
                    total=Sum("amount")
                )["total"]
                or 0
            )

            budget.spent = spent

            budget.remaining = budget.amount - spent

            budget.usage = (spent / budget.amount) * 100

        return context
class BudgetCreateView(LoginRequiredMixin, CreateView):

    model = Budget

    form_class = BudgetForm

    template_name = "expenses/Budget/form.html"

    success_url = reverse_lazy("budget-list")

    def form_valid(self, form):

        form.instance.user = self.request.user

        messages.success(
            self.request,
            "Budget added successfully!"
        )

        return super().form_valid(form)
    
class BudgetUpdateView(LoginRequiredMixin, UpdateView):

    model = Budget

    form_class = BudgetForm

    template_name = "expenses/budget/form.html"

    success_url = reverse_lazy("budget-list")

    def get_queryset(self):

        return Budget.objects.filter(
            user=self.request.user
        )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Budget updated successfully!"
        )

        return super().form_valid(form)
    
class BudgetDeleteView(LoginRequiredMixin, DeleteView):

    model = Budget

    template_name = "expenses/budget/delete.html"

    success_url = reverse_lazy("budget-list")

    def get_queryset(self):

        return Budget.objects.filter(
            user=self.request.user
        )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Budget deleted successfully!"
        )

        return super().form_valid(form)