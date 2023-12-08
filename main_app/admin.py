from django.contrib import admin

from .models import Finch, Feeding

admin.site.register(Finch)
# Register your models here.
admin.site.register(Feeding)
