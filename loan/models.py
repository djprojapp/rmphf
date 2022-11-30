from django.db import models

# Create your models here.

class Loan(models.Model):
    loan_no=models.IntegerField(unique=True)
    loan_scheme=models.IntegerField(null=True)
    loan_amount=models.IntegerField(null=True)
    disbursment_date=models.DateField(null=True)

    class Meta:
        db_table='loan'

class Shedule(models.Model):
    loan_no=models.ForeignKey(Loan, on_delete=models.CASCADE, null=True)
    inst_no=models.IntegerField(null=True)
    install_amount=models.DecimalField(decimal_places=0, max_digits=11,null=True)
    due_date=models.DateField(null=True)

    class Meta:
        db_table='shedule'
