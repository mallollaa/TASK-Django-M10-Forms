from django import forms
from models import StoreItem

class StoreItemForm(forms.ModelForm):
    class Meta :
        model = StoreItem
        feild = ["name" , "description","kind","price"] 
