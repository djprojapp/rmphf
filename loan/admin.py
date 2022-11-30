from django.contrib import admin
from .models import Loan, Shedule

# Register your models here.
admin.site.register(Loan)
admin.site.register(Shedule)