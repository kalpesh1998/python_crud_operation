from django import forms
from .models import Student_form

class Student_info(forms.ModelForm):
    class Meta:
        model = Student_form
        # fields=["__all__"]
        fields = ["name","age","title","description"]