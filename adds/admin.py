from django.contrib import admin

# Register your models here.
from .models import Food

class FoodAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'title', 'description', 'timestamp', 'updated']
	search_fields = ['title', 'description']
	list_editable = ['title', 'description']
	def __str__(self):
		return self.title
	class Meta:
		model = Food

admin.site.register(Food, FoodAdmin)