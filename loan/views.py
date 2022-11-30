from re import I
from django.shortcuts import render, redirect
from loan.models import Loan, Shedule
from datetime import date, datetime
from django.db.models import Sum, Count
from dateutil.relativedelta import relativedelta


# Create your views here.

def recovery(request):
    if request.method=='POST':
        loan_no=request.POST['loan_no']
        loan_amount=request.POST['loan_amount']
        loan_scheme=request.POST['loan_scheme']
        d1,m1,y1= [int(x) for x in request.POST['disbursment_date'].split('-')]
        disbursment_date=date(y1,m1,d1)
        due_date=disbursment_date
        new_loanee=Loan.objects.create(loan_no=loan_no,loan_amount=loan_amount, disbursment_date=disbursment_date, loan_scheme=loan_scheme)
        loanee=Loan.objects.latest('id')
        i=0
        if loanee.loan_scheme==3:
            while i<16:
                i += 1
                loan_no_id=loanee.id
                inst_no= i
                install_amount=round(int(loan_amount)/16,0)
                if inst_no==16:
                    install_amount=int(loan_amount)-install_amount*15
                due_date = due_date + relativedelta(months=6)
                Shedule.objects.create(loan_no_id=loan_no_id, inst_no=inst_no, install_amount=install_amount, due_date=due_date)
        else:
             while i<12:
                i += 1
                loan_no_id=loanee.id
                inst_no= i
                install_amount=round(int(loan_amount)/12,0)
                if inst_no==12:
                    install_amount=int(loan_amount)-install_amount*11
                due_date = due_date + relativedelta(months=3)
                Shedule.objects.create(loan_no_id=loan_no_id, inst_no=inst_no, install_amount=install_amount, due_date=due_date)
    return render(request, 'loan/recovery.html')

def disbursment(request):
    loan=Loan.objects.all().order_by('loan_no')
    tl=Loan.objects.all().aggregate(total=Sum('loan_amount'))
    tr=Shedule.objects.all().aggregate(total=Sum('install_amount'))
    fy22=Shedule.objects.filter(due_date__gt='2022-06-30').filter(due_date__lt='2023-07-01').aggregate(r22=Sum('install_amount'))
    fy23=Shedule.objects.filter(due_date__gt='2023-06-30').filter(due_date__lt='2024-07-01').aggregate(r23=Sum('install_amount'))
    fy24=Shedule.objects.filter(due_date__gt='2024-06-30').filter(due_date__lt='2025-07-01').aggregate(r24=Sum('install_amount'))
    fy25=Shedule.objects.filter(due_date__gt='2025-06-30').filter(due_date__lt='2026-07-01').aggregate(r25=Sum('install_amount'))
    fy26=Shedule.objects.filter(due_date__gt='2026-06-30').filter(due_date__lt='2027-07-01').aggregate(r26=Sum('install_amount'))
    fy27=Shedule.objects.filter(due_date__gt='2027-06-30').filter(due_date__lt='2028-07-01').aggregate(r27=Sum('install_amount'))
    fy28=Shedule.objects.filter(due_date__gt='2028-06-30').filter(due_date__lt='2029-07-01').aggregate(r28=Sum('install_amount'))
    fy29=Shedule.objects.filter(due_date__gt='2029-06-30').filter(due_date__lt='2030-07-01').aggregate(r29=Sum('install_amount'))
    fy30=Shedule.objects.filter(due_date__gt='2030-06-30').filter(due_date__lt='2031-07-01').aggregate(r30=Sum('install_amount'))
    fy31=Shedule.objects.filter(due_date__gt='2031-06-30').aggregate(r31=Sum('install_amount'))
    dy22=Loan.objects.filter(disbursment_date__gt='2022-06-30').filter(disbursment_date__lt='2023-07-01').aggregate(d22=Sum('loan_amount'))
    return render(request, 'loan/disbursment.html', {'fy22':fy22,'fy23':fy23, 'fy24':fy24, 'fy25':fy25, 'fy26':fy26, 'fy27':fy27, 'fy28':fy28, 'fy29':fy29, 'fy30':fy30, 'fy31':fy31, 'loan':loan, 'tl':tl, 'tr':tr, 'dy22':dy22})

def delete(request, loan_no):
    loan=Loan.objects.get(loan_no=loan_no).delete()
    return redirect('/loan/disbursment')

def index(request):
    loan=Loan.objects.all().order_by('loan_no')
    tl=Loan.objects.all().aggregate(total=Sum('loan_amount'))
    tr=Shedule.objects.all().aggregate(total=Sum('install_amount'))
    fy22=Shedule.objects.filter(due_date__gt='2022-06-30').filter(due_date__lt='2023-07-01').aggregate(r22=Sum('install_amount'))
    fy23=Shedule.objects.filter(due_date__gt='2023-06-30').filter(due_date__lt='2024-07-01').aggregate(r23=Sum('install_amount'))
    fy24=Shedule.objects.filter(due_date__gt='2024-06-30').filter(due_date__lt='2025-07-01').aggregate(r24=Sum('install_amount'))
    fy25=Shedule.objects.filter(due_date__gt='2025-06-30').filter(due_date__lt='2026-07-01').aggregate(r25=Sum('install_amount'))
    fy26=Shedule.objects.filter(due_date__gt='2026-06-30').filter(due_date__lt='2027-07-01').aggregate(r26=Sum('install_amount'))
    fy27=Shedule.objects.filter(due_date__gt='2027-06-30').filter(due_date__lt='2028-07-01').aggregate(r27=Sum('install_amount'))
    fy28=Shedule.objects.filter(due_date__gt='2028-06-30').filter(due_date__lt='2029-07-01').aggregate(r28=Sum('install_amount'))
    fy29=Shedule.objects.filter(due_date__gt='2029-06-30').filter(due_date__lt='2030-07-01').aggregate(r29=Sum('install_amount'))
    fy30=Shedule.objects.filter(due_date__gt='2030-06-30').filter(due_date__lt='2031-07-01').aggregate(r30=Sum('install_amount'))
    fy31=Shedule.objects.filter(due_date__gt='2031-06-30').aggregate(r31=Sum('install_amount'))
    dy22=Loan.objects.filter(disbursment_date__gt='2022-06-30').filter(disbursment_date__lt='2023-07-01').aggregate(d22=Sum('loan_amount'))
    l=Loan.objects.all().aggregate(tl=Count('loan_no'))
    sc1=Loan.objects.all().filter(loan_scheme=1).aggregate(tl=Count('loan_no'))
    sc2=Loan.objects.all().filter(loan_scheme=2).aggregate(tl=Count('loan_no'))
    sc3=Loan.objects.all().filter(loan_scheme=3).aggregate(tl=Count('loan_no'))
    return render(request, 'loan/index.html', {'l':l, 'sc1':sc1, 'sc2':sc2, 'sc3':sc3, 'fy22':fy22,'fy23':fy23, 'fy24':fy24, 'fy25':fy25, 'fy26':fy26, 'fy27':fy27, 'fy28':fy28, 'fy29':fy29, 'fy30':fy30, 'fy31':fy31, 'loan':loan, 'tl':tl, 'tr':tr, 'dy22':dy22})

