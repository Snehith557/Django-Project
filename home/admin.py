from django.contrib import admin

# Register your models here.
from . models import home,projects,contact
# registering the model / the database table in this admin 

admin.site.register(home)
admin.site.register(projects)
admin.site.register(contact)