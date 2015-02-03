from django import forms

class FoodForm(forms.Form):
	title = forms.CharField(max_length=200)
	description = forms.CharField(max_length=200)