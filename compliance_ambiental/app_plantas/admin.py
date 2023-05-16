from django.contrib import admin

# Register your models here.
from .models import Plantas, Projetos

admin.site.register(Plantas)
admin.site.register(Projetos)