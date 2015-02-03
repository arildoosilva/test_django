from django import forms
from .models import Food

class FoodForm(forms.Form):
	title = forms.CharField(max_length=200)
	description = forms.CharField(max_length=200)

class AddForm(forms.ModelForm):
	class Meta:
		model = Food