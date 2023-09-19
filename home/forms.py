from django import forms

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    create = forms.DateTimeField()
    
