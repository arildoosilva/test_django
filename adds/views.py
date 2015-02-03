from django.shortcuts import render

# Create your views here.
from .forms import FoodForm
from .models import Food

def home(request):
	context = {}
	template = 'home.php'
	return render(request, template, context)

def addfood(request):
	form = FoodForm(request.POST or None)
	if form.is_valid():
		sent_title = form.cleaned_data['title']
		sent_description = form.cleaned_data['description']
		new_food, created = Food.objects.get_or_create(title=sent_title, description=sent_description)
	context = {'form':form}
	template = 'form.php'
	return render(request, template, context)