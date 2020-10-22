
from django import forms
from .models import Employee2


class EmployeeForm(forms.ModelForm):
   


    class Meta:
        model = Employee2
        fields = ('firstname','lastname','age','address')
        labels = {
            
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'age': 'Age',
            'address': 'Address'

        }
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        #self.fields['position'].empty_label = "Select"
        #self.fields['emp_code'].required = False
