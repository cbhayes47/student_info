from django import forms

class StudentForm(forms.Form):
    pk = forms.IntegerField(label='pk')
