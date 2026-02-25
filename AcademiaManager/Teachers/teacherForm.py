
from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),  # assuming choices field
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
