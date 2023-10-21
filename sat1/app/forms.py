from django import forms
# create the FormName class
class FormName(forms.Form):
    name = forms.charField()
    email = forms.EmailField()
    text = forms.Charfield(widget = forms.Textarea)
