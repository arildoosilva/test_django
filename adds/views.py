from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	template = 'home.php'
	return render(request, template, context)