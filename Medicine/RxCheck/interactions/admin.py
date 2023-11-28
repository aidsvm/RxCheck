from django.contrib import admin
from .models import Drug, Drug_History

# Register your models here.

@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'instructions')

@admin.register(Drug_History)
class Drug_History_Admin(admin.ModelAdmin):
    list_display = ('drug',)

