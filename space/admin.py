from django.contrib import admin

# Register your models here.
from .models import Super
from . models import QualityInspection
admin.site.register(Super)
admin.site.register(QualityInspection)