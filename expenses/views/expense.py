from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from ..models import Expense,ExpenseCategory
from ..forms.expense import ExpenseForm


class ExpenseListView(LoginRequiredMixin, ListView):

    model = Expense

    template_name = "expenses/expense/list.html"

    context_object_name = "expenses"
    paginate_by = 5

    def get_queryset(self):


        queryset = (
            Expense.objects.filter(user=self.request.user)
            .select_related("category")
            .order_by("-expense_date")
        )

        search = self.request.GET.get("search")

        if search:

            queryset = queryset.filter(
                title__icontains=search
            )

        category = self.request.GET.get("category")

        if category:

            queryset = queryset.filter(
                category_id=category
            )

        return queryset
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["categories"] = ExpenseCategory.objects.all()   

        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):

    model = Expense

    form_class = ExpenseForm

    template_name = "expenses/expense/form.html"

    success_url = reverse_lazy("expense-list")

    def form_valid(self, form):

        form.instance.user = self.request.user

        messages.success(
            self.request,
            "Expense added successfully!"
        )

        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):

    model = Expense

    form_class = ExpenseForm

    template_name = "expenses/expense/form.html"

    success_url = reverse_lazy("expense-list")

    def get_queryset(self):

        return Expense.objects.filter(
            user=self.request.user
        )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Expense updated successfully!"
        )

        return super().form_valid(form)


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):

    model = Expense

    template_name = "expenses/expense/delete.html"

    success_url = reverse_lazy("expense-list")

    def get_queryset(self):

        return Expense.objects.filter(
            user=self.request.user
        )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Expense deleted successfully!"
        )

        return super().form_valid(form)