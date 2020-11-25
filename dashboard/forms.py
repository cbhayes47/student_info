from django import forms

class StudentForm(forms.Form):
    pk = forms.IntegerField(label='pk')

class EnrollForm(forms.Form):
    course1 = forms.IntegerField(label='course1_pk')
    course2 = forms.IntegerField(label='course2_pk')
    course3 = forms.IntegerField(label='course3_pk')
