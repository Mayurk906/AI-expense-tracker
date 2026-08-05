from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from ..models import Income,IncomeCategory
from ..forms.income import IncomeForm


class IncomeListView(LoginRequiredMixin, ListView):

    model = Income

    template_name = "expenses/income/list.html"

    context_object_name = "incomes"
    paginate_by = 5

    def get_queryset(self):


        queryset = (
            Income.objects.filter(user=self.request.user)
            .select_related("category")
            .order_by("-income_date")
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

        context["categories"] = IncomeCategory.objects.all()

        return context
    
class IncomeCreateView(LoginRequiredMixin, CreateView):

    model = Income

    form_class = IncomeForm

    template_name = "expenses/income/form.html"

    success_url = reverse_lazy("income-list")

    def form_valid(self, form):

        form.instance.user = self.request.user

        messages.success(
            self.request,
            "Income added successfully!"
        )

        return super().form_valid(form)
    
class IncomeUpdateView(LoginRequiredMixin, UpdateView):

    model = Income

    form_class = IncomeForm

    template_name = "expenses/income/form.html"

    success_url = reverse_lazy("income-list")

    def get_queryset(self):

        return Income.objects.filter(
            user=self.request.user
        )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Income updated successfully!"
        )

        return super().form_valid(form)
    
class IncomeDeleteView(LoginRequiredMixin, DeleteView):

    model = Income

    template_name = "expenses/income/delete.html"

    success_url = reverse_lazy("income-list")

    def get_queryset(self):

        return Income.objects.filter(
            user=self.request.user
        )

    def form_valid(self, form):

        messages.success(
            self.request,
            "Income  deleted successfully!"
        )

        return super().form_valid(form)
