from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'phone', 'show')
  list_editable = ('show',)
  list_display_links = ('phone',)
  ordering = ('id',)
  search_fields = ('id', 'first_name', 'last_name')
  list_max_show_all = 200
  
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)