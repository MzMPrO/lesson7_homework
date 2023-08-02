from django import forms

from branch.models import Branch


class Form(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.EmailInput(attrs={"class": "form-control"}),
        }
