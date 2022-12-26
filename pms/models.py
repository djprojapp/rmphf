from django.db import models
from random import choices

# Create your models here.
class Pensioner(models.Model):
    name=models.CharField(max_length=200)
    fname=models.CharField(max_length=200, null=True)
    pay=models.IntegerField(null=True)
    qs=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200, null=True)
    comm_rate=models.DecimalField(decimal_places=4, max_digits=8, null=True)
    dob=models.CharField(max_length=20,null=True)
    dobf=models.CharField(max_length=20,null=True)
    doa=models.CharField(max_length=20,null=True)
    dor=models.CharField(max_length=20,null=True)
    dod=models.CharField(max_length=20,null=True)
    gp=models.FloatField(null=True)
    np=models.FloatField(null=True)
    comm_amount=models.FloatField(null=True)
    inc03=models.FloatField(null=True)
    inc04=models.FloatField(null=True)
    inc05=models.FloatField(null=True)
    inc06=models.FloatField(null=True)
    inc07=models.FloatField(null=True)
    inc08=models.FloatField(null=True)
    inc09=models.FloatField(null=True)
    inc10=models.FloatField(null=True)
    inc11=models.FloatField(null=True)
    inc12=models.FloatField(null=True)
    inc13=models.FloatField(null=True)
    inc14=models.FloatField(null=True)
    inc15=models.FloatField(null=True)
    inc16=models.FloatField(null=True)
    inc17=models.FloatField(null=True)
    inc18=models.FloatField(null=True)
    inc19=models.FloatField(null=True)
    inc21=models.FloatField(null=True)
    inc22=models.FloatField(null=True)
    incr22=models.FloatField(null=True)
    incm=models.FloatField(null=True)
    cp=models.FloatField(null=True)
    cpr=models.FloatField(null=True)
    ma2010=models.FloatField(null=True)
    ma2015=models.FloatField(null=True)
    tp=models.FloatField(null=True)
    ppo=models.CharField(max_length=9, null=True, unique=True)
    bps=models.IntegerField(null=True)
    rbs=models.IntegerField(null=True)
    cnic=models.CharField(max_length=13, null=True, unique=True)
    qpay=models.IntegerField(null=True)
    ppay=models.IntegerField(null=True)
    spay=models.IntegerField(null=True)
    ui=models.IntegerField(null=True)
    opay=models.IntegerField(null=True)
    lpd=models.IntegerField(null=True)
    cat=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    designation=models.CharField(max_length=50, null=True)
    restd=models.DateField(null=True)

class Status(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    ppo=models.CharField(max_length=9, null=True)
    status=models.CharField(max_length=8)

class BankAccount(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.DO_NOTHING)
    ppo=models.CharField(max_length=9, null=True)
    pname=models.CharField(max_length=20, null=True)
    bname=models.CharField(max_length=10, null=True)
    bb=models.CharField(max_length=20, null=True)
    acctno=models.CharField(max_length=20, null=True)
    payment_ratio=models.FloatField(max_length=4, null=True)

class Payment(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    pname=models.CharField(max_length=20, null=True)
    ppo=models.CharField(max_length=9, null=True)
    month=models.IntegerField(null=True)
    year=models.IntegerField(null=True)
    np=models.IntegerField(null=True)
    increases=models.IntegerField(null=True)
    arrears=models.IntegerField(null=True)
    recoveries=models.IntegerField(null=True)
    ma2010=models.FloatField(null=True)
    ma2015=models.FloatField(null=True)
    tp=models.FloatField(null=True)
    bname=models.CharField(max_length=10,null=True)
    bb=models.CharField(max_length=20,null=True)
    acctno=models.CharField(max_length=20,null=True)
    paid_on=models.DateField(auto_now_add=True, null=True)
    
    class Meta:
        unique_together=('acctno','month', 'year',)
    
class Adjustment(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    ppo=models.CharField(max_length=9, null=True)
    description=models.CharField(max_length=50, null=True, blank=True)
    amount=models.IntegerField(null=True)
    p_type=models.CharField(max_length=1)

class AdjustmentHistory(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    ppo=models.CharField(max_length=9, null=True)
    description=models.CharField(max_length=50, null=True, blank=True)
    amount=models.IntegerField(null=True)
    p_type=models.CharField(max_length=1)

class Increases(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    ppo=models.CharField(max_length=9, null=True)
    description=models.CharField(max_length=50, null=True, blank=True)
    start_date=models.CharField(max_length=10)
    rate=models.CharField(max_length=4, null=True)
    inc_amount=models.IntegerField(null=True)
    tp_amount=models.IntegerField(null=True)

    class Meta:
        verbose_name_plural="increases"

class RecoveryInstallment(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    ppo=models.CharField(max_length=9, null=True)
    description=models.CharField(max_length=20, null=True)
    principal=models.IntegerField(null=True)
    installment=models.IntegerField(null=True)
    recovered=models.IntegerField(null=True)
    balance=models.IntegerField(null=True)
    start_date=models.DateField(null=True, auto_now_add=True)




        
    