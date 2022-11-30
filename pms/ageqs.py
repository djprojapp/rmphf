from datetime import datetime, date
def datediff(d1,m1,y1,d2,m2,y2):
	global years, months, days
	if y2>=y1:
		if d2>=d1 and m2>=m1:
			days=d2-d1
			months=m2-m1
			years=y2-y1
			#print(f"{years} years {months} months {days} days")
		if d2>=d1 and m2<m1:
			days=d2-d1
			if m2<m1:
				m2=m2+12
				y2=y2-1
			months=m2-m1
			years=y2-y1
			#print(f"{years} years {months} months {days} days")
		elif d2<d1 and m2 in [1,3,5,7,8,10,12]:
			d2=d2+31
			m2=m2-1
			if m2<m1:
				m2=m2+12
				y2=y2-1
			years=y2-y1
			months=m2-m1
			days=d2-d1
			#print(f"{years} years {months} months {days} days")
		elif d2<d1 and m2 in [4,6,9,11]:
			d2=d2+30
			m2=m2-1
			if m2<m1:
				m2=m2+12
				y2=y2-1
			years=y2-y1
			months=m2-m1
			days=d2-d1
			#print(f"{years} years {months} months {days} days")
		elif d2<d1 and m2 in [2] and y2%4==0:
			d2=d2+29
			if d2<d1:
				d2=d2+31
				m2=m2-1
			m2=m2-1
			if m2<m1:
				m2=m2+12
				y2=y2-1
			years=y2-y1
			months=m2-m1
			days=d2-d1
			#print(f"{years} years {months} months {days} days")
		elif d2<d1 and m2 in [2] and y2%4!=0:
			d2=d2+28
			if d2<d1:
				d2=d2+31
				m2=m2-1
			m2=m2-1
			if m2<m1:
				m2=m2+12
				y2=y2-1
			years=y2-y1
			months=m2-m1
			days=d2-d1
	return years, months, days
age=datediff(15,1,1975,4,2,2022)
print(f"{years} years {months} months {days} days")

'''d1,m1,y1= [int(x) for x in input("Enter Date of Birth: (dd/mm/yyyy)").split('/')]
d2,m2,y2= [int(x) for x in input("Enter Date of Appointment: (dd/mm/yyyy)").split('/')]
d3,m3,y3= [int(x) for x in input("Enter Date of Retirement: (dd/mm/yyyy)").split('/')]
Age=datediff(d1,m1,y1,d3,m3,y3)
print(f"{years} years {months} months {days} days")
QS=datediff(d2,m2,y2,d3,m3,y3)
print(f"{years} years {months} months {days} days")
NQS=years
if months>=6:
	years=years+1
print (NQS) 
'''