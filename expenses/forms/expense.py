from django import forms

from ..models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = (
            "title",
            "amount",
            "category",
            "payment_method",
            "expense_date",
            "description",
        )
        widgets = {

            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "amount": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "category": forms.Select(
                attrs={"class": "form-select"}
            ),

            "payment_method": forms.Select(
                attrs={"class": "form-select"}
            ),

            "expense_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }