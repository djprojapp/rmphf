from datetime import date
import ageqs
d1=15
m1=2
y1=1975
d2=19
m2=10
y2=2000
d3=2
m3=2
y3=2022
ageqs.datediff(d1,m1,y1,d3,m3,y3)
#print(f"{age.years} years {age.months} months {age.days} days")
age_nb=ageqs.years+1
#print(f"Age on Next birthday = {age_nb}")
length_of_service=ageqs.datediff(d2,m2,y2,d3,m3,y3)
print(f"{ageqs.years} years {ageqs.months} months {ageqs.days} days")
if ageqs.months>=6:
    NQS=ageqs.years+1
    #print(f"NQS= {NQS}")
else:
    NQS=ageqs.years
    #print(f"NQS= {NQS}")

com_table2001 ={20:40.5043, 21:39.7341, 22:38.9653,23:38.1974,24:37.4307,25:36.6651,26:35.9006,27:35.1372,28:34.3750,29:33.6143,30:32.8071,31:32.0974,32:31.3412,33:30.5869,34:29.8343,35:29.0841,36:28.3362,37:27.5908,38:26.8482,39:26.1009,40:25.3728,41:24.6406,42:23.9126,43 : 23.184 , 44 :  22.4713 , 45:21.7592,46:21.0538,47:20.3555,48:19.6653,49:18.9841,50:18.3129,51:17.6525,52:17.005,53:16.371,54:15.7517,55:15.1478,56:14.5602,57:13.9888,58:13.434,59:12.8953,60:12.3719}
rate_on_next_birthday=com_table2001[age_nb]
print(rate_on_next_birthday)
dob=date(y1,m1,d1)
print(dob)
doa=date(y2,m2,d2)
print(doa)
dor=date(y3,m3,d3)
print(dor)
n_years_res=round(rate_on_next_birthday)
print(n_years_res)
dores=date(y3+n_years_res,m3,d3)
print (dores)
d=date(y1,m1,d1)
