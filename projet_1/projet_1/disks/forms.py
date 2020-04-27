from django import forms


class search(forms.Form):
    query = forms.CharField(max_length=100)