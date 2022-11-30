from django.contrib import admin
from .models import Pensioner, BankAccount, Payment
from .models import Pensioner, BankAccount, Payment,Status, Increases, Adjustment

# Register your models here.
admin.site.register(Pensioner)
admin.site.register(BankAccount)
admin.site.register(Payment)
admin.site.register(Status)
admin.site.register(Increases)
admin.site.register(Adjustment)