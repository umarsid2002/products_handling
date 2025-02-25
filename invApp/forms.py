from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            'product_id': 'Product Id',
            'name': 'Name',
            'sku': 'Sku',
            'price': 'Price',
            'qty': 'Qty',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'e.g 1', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'T-shirt', 'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder': '001', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': '19.99', 'class': 'form-control'}),
            'qty': forms.NumberInput(attrs={'placeholder': '10', 'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder': 'Abc Company', 'class': 'form-control'}),
        }