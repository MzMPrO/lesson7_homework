from django import forms

from profession.models import Profession


class Form(forms.ModelForm):
    class Meta:
        model = Profession
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
