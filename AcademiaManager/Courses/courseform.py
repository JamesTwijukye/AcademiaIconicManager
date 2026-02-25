from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-control'}),
                    'code': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.NumberInput(attrs={'class': 'form-control'}),
                   
                }


