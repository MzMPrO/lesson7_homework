from django import forms

from employee.models import Employee


class Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "hire_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            'department_id': forms.Select(attrs={'class': 'form-control'}),
            'profession_id': forms.Select(attrs={'class': 'form-control'}),
        }
