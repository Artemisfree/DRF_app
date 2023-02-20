from django import forms

class HexFileForm(forms.Form):
    hex_file = forms.FileField()
