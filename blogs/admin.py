from django.contrib import admin

# Register your models here.
#blogs/models.py
#class Blog(models.Model):  #<---

from .models import Blog    #<---

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

    
admin.site.register(Blog)
