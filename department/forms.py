from django import forms

from department.models import Department


class Form(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            'branch_id': forms.Select(attrs={'class': 'form-control'}),
        }
