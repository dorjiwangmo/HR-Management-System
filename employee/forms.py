from django import forms
from .models import Employee
from django.contrib.auth.password_validation import validate_password


class EmployeeForm(forms.ModelForm):
    dob = forms.DateField(
        label='DOB',
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%Y'],
        error_messages={'invalid': ('Enter a valid date in the format dd/mm/yyyy.')},
    )
    appointment_date = forms.DateField(
        label='Appointment Date',
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%Y'],
        error_messages={'invalid': ('Enter a valid date in the format dd/mm/yyyy.')},
    )
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'gender', 'dob', 'designation', 'department', 'appointment_date']
        labels = {
            'name': 'Name',
            'employee_id': 'Employee ID',
            'gender': 'Gender',
            'dob':'DOB',
            'designation':'Designation',
            'department':'Department',
            'appointment_date':'Appointment Date'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter name'}),
            'employee_id': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Enter employee ID'}),
            'gender': forms.Select(attrs={'class': 'form-control','placeholder': 'Select gender'}),
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'dd/mm/yyyy'}),
            'designation': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter designation'}),
            'department': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter department'}),
            'appointment_date': forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'dd/mm/yyyy'}),
        }


class LoginFormm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id':"username", 'type':"text", "class":'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id':"password", 'type':"password", "class":'form-control'
    }))

    class Meta:
        fields = ['username','password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = self.user_cache
            if user is None or not user.is_superuser:
                raise forms.ValidationError("Only superuser can login.")

        return username




