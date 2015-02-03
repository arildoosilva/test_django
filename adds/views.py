from django.shortcuts import render

# Create your views here.
#from .forms import FoodForm
from .forms import AddForm
from .models import Food

def home(request):
	context = {
	'foods': Food.objects.all()
	}
	template = 'home.php'
	return render(request, template, context)

def addfood(request):
	#Regular Django Form
	# form = FoodForm(request.POST or None)
	# if form.is_valid():
	# 	sent_title = form.cleaned_data['title']
	# 	sent_description = form.cleaned_data['description']
	# 	new_food, created = Food.objects.get_or_create(title=sent_title, description=sent_description)

	#Model Form
	form = AddForm(request.POST or None)
	if form.is_valid():
		#new_food = form.save(commit=False) #commit false to save later (in case we do something else with the data)
		sent_title = form.cleaned_data['title']
		sent_description = form.cleaned_data['description']
		new_food_old, created = Food.objects.get_or_create(title=sent_title, description=sent_description)
		#new_food.save()
	context = {'form':form}
	template = 'form.php'
	return render(request, template, context)