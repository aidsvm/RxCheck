# forms.py
from django import forms


class DrugSearchForm(forms.Form):
    drug_name = forms.CharField(label='Enter Drug Name', max_length=100)
