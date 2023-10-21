from django.shortcuts import render
from . import forms
# Create your views here.

def form_name_view(request):
    form  = forms.FormName()

# check to see if we are getting post request back

    if request.method == "POST":
        form = forms.FormName(request.POST)
#then check to see if the form is valid
    if form.isvalid()
# if form.is_valid == True then do something 

        print("form validation successful see console for information:")
        print("Name :"+form.cleaned_data['name'] )
        print("email: "+form.cleaned_data['email'])
        print("message:"+form.cleaned_data['text'])
    return render(request,'home.html',{'form':form})