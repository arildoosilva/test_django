from django.contrib import admin

# Register your models here.
from .models import Food

class FoodAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'timestamp', 'updated']
	search_fields = ['title', 'description']
	class Meta:
		model = Food

admin.site.register(Food, FoodAdmin)