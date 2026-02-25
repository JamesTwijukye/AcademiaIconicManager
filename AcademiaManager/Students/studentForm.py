from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),  # assuming choices field
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
