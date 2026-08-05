from django import forms

from ..models import Income


class IncomeForm(forms.ModelForm):

    class Meta:

        model = Income

        fields = (
            "title",
            "amount",
            "category",
            "income_date",
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

            "income_date": forms.DateInput(
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