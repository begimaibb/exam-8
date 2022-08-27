from django import forms
from webapp.models import Product, Review


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Find')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review_text", "rating"]
