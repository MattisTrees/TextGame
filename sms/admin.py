from django.contrib import admin
from .models import *

# Register your models here.

# Register the Game session model for viewing the table in the Django admin page
admin.site.register(Game)
