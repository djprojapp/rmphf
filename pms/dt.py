from datetime import datetime, date

a="15-06-1998"
b="19-10-2016"
c="15-05-2022"
d=""
e=""
pay=500
bps=15
rbs=2001
#Service Chronological data
d1,m1,y1= [int(x) for x in a.split('-')]
d2,m2,y2= [int(x) for x in b.split('-')]
db=date(y1,m1,d1)
dob=db.strftime("%d-%m-%Y")
da=date(y2,m2,d2)
doa=da.strftime("%d-%m-%Y")
if c!="":
    d3,m3,y3= [int(x) for x in c.split('-')]
    dr=date(y3,m3,d3)
    dor=dr.strftime("%d-%m-%Y")
else:
    dr=""

if d!="":
    d4,m4,y4= [int(x) for x in d.split('-')]
    dd=date(y4,m4,d4)
    dod=dd.strftime("%d-%m-%Y")
else:
    dd=""
if e!="":
    d5,m5,y5= [int(x) for x in e.split('-')]
    dbf=date(y5,m5,d5)
    dobf=dbf.strftime("%d-%m-%Y")
#Pension Categories
def pen_cat():
    if dr!="" and dd =="":
        pentype="Self"
    elif dr!="" and dd !="":
        pentype="Family-DAR"
    else:
        pentype="Family-DIS"
    return pentype
cat=pen_cat()
#Age, Qualifying Service Calculation
def datediff(d1,m1,y1,d2,m2,y2):
    global years, months, days
    if y2>=y1:
        if d2>=d1 and m2>=m1:
            days=d2-d1
            months=m2-m1
            years=y2-y1
        if d2>=d1 and m2<m1:
            days=d2-d1
            if m2<m1:
                m2=m2+12
                y2=y2-1
            months=m2-m1
            years=y2-y1
        elif d2<d1 and m2 in [1,3,5,7,8,10,12]:
            d2=d2+31
            m2=m2-1
            if m2<m1:
                m2=m2+12
                y2=y2-1
            years=y2-y1
            months=m2-m1
            days=d2-d1
        elif d2<d1 and m2 in [4,6,9,11]:
            d2=d2+30
            m2=m2-1
            if m2<m1:
                m2=m2+12
                y2=y2-1
            years=y2-y1
            months=m2-m1
            days=d2-d1
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
if cat=="Self" or cat=="Family-DAR":
    datediff(d1,m1,y1,d3,m3,y3)
    age=f"{years} Y-{months} M-{days} D"
    age_nb=years+1
else:
    datediff(d1,m1,y1,d4,m4,y4)
    age=f"{years} Y-{months} M-{days} D"
    age_nb=years+1
if age_nb>60:
    age_nb=60

#Commutation Table 2001 
com_table2001 ={20:40.5043, 21:39.7341, 22:38.9653,23:38.1974,24:37.4307,25:36.6651,26:35.9006,27:35.1372,28:34.3750,29:33.6143,30:32.8071,31:32.0974,32:31.3412,33:30.5869,34:29.8343,35:29.0841,36:28.3362,37:27.5908,38:26.8482,39:26.1009,40:25.3728,41:24.6406,42:23.9126,43 : 23.184 , 44 :  22.4713 , 45:21.7592,46:21.0538,47:20.3555,48:19.6653,49:18.9841,50:18.3129,51:17.6525,52:17.005,53:16.371,54:15.7517,55:15.1478,56:14.5602,57:13.9888,58:13.434,59:12.8953,60:12.3719}
comm_rate=com_table2001[age_nb]
num_years_pur=round(comm_rate)
#Restoration due date
if cat=="Self" or cat=="Family-DAR":
    restd=dr.replace(year=dr.year+num_years_pur)
else:
    restd=dd.replace(year=dd.year+num_years_pur)
#Qualifying Service
if cat=="Self" or cat=="Family-DAR":
    datediff(d2,m2,y2,d3,m3,y3)
    qs=years
    if months>=6:
        qs=years+1
else:
    datediff(d2,m2,y2,d4,m4,y4)
    qs=years
    if months>=6:
        qs=years+1
if qs>30:
    qs=30
print(qs)
print(age)
#Gross Pension
gp=round(int(pay)*qs/30*0.7,2)
#Net Pension
if cat=="Self" and rbs>=2005:
    npo=round(gp*0.65,2)
    cp=round(gp*0.35,2)
elif cat=="Self" and rbs<2005:
    npo=round(gp*0.60,2)
    cp=round(gp*0.40,2)
elif cat=="Family-DIS":
    npo=round(gp*0.75,2)
    cp=round(gp*0.25,2)
elif cat=="Family-DAR" and rbs>=2005:
    npo=round(gp*0.65*0.75,2)
    cp=round(gp*0.35*0.75,2)
elif cat=="Family-DAR" and rbs<2005:
    npo=round(gp*0.60*0.75,2)
    cp=round(gp*0.40*0.75,2)
np=npo
#Commutation Amount Calculation
comm_amount=round(cp*12*comm_rate,2)
#Date for increase conditions
d2002=date(2002,7,1)
d2005=date(2005,7,1)
d2007=date(2007,7,1)
d2008=date(2008,7,1)
d2009=date(2009,7,1)
d2011=date(2011,7,1)
d2015=date(2015,7,1)
d2016=date(2016,7,1)
d2017=date(2017,7,1)
#Pension Increases Calculations
inc=[]
restored=[]
inc03=0
inc04=0 
inc05=0
inc06=0
inc07=0
inc08=0
inc09=0
inc10=0
inc11=0
inc12=0
inc13=0
inc14=0
inc15=0
inc16=0
inc17=0
inc18=0
inc19=0
inc21=0
inc22=0
if cat=="Family-DIS":
    dr=dd
#Minimum Pension
if cat=="Self":
    mp=300.00
    mp08=2000.00
    mp10=3000.00
    mp13=5000.00
    mp14=6000.00
    mp18=10000.00
    mp75=15000.00
else:
    mp=150.00
    mp08=1000.00
    mp10=2250.00
    mp13=3750.00
    mp14=4500.00
    mp18=7500.00
    mp75=11250.00
#Increase wef 1.07.2003
if dr<d2005:
    inc03=round(np*0.15,2)
    np=round(np+inc03,2)
    cp=round(cp*1.15,2)
    remarks="Increase"
    if np<mp:
        inc03=round(mp-np+inc03,2)
        np=round(mp,2)
        remarks="Mini Pension"
        
    if dr>date(2003,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2003,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc03,np])

#restoration
d3=date(2003,7,1)
d4=date(2004,7,1)
if d3<restd<d4:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2004
if dr<d2005:
    inc04=round(np*0.08,2)
    cp=round(cp*1.08,2)
    np=round(np+inc04,2)
    remarks="Increase"
    if np<mp:
        inc04=round(mp-np+inc04,2)
        np=round(mp,2)
        remarks="Mini Pension"
    if dr>date(2004,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2004,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc04,np])
#restoration
d4=date(2004,7,1)
d5=date(2005,7,1)
if d4<restd<d5:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2005
if dr<d2011:
    inc05=round(np*0.10,2)
    cp=round(cp*1.10,2)
    np=round(np+inc05,2)
    remarks="Increase"
    if np<mp:
        inc05=round(mp-np+inc05,2)
        np=round(mp,2)
        remarks="Mini Pension"
    if dr>date(2005,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2005,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc05,np])

#restoration
d5=date(2005,7,1)
d6=date(2006,7,1)
if d5<restd<d6:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2006
if dr<d2011:
    inc06=round(np*0.15,2)
    cp=round(cp*1.15,2)
    np=round(np+inc06,2)
    remarks="Increase"
    if np<mp:
        inc06=round(mp-np+inc06,2)
        np=round(mp,2)
        remarks="Mini Pension"
    if dr>date(2006,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2006,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc06,np])
#restoration
d6=date(2006,7,1)
d7=date(2007,7,1)
if d6<restd<d7:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2007    
if dr<d2007:
    inc07=round(np*0.15,2)
    cp=round(cp*1.15,2)
    np=round(np+inc07,2)
    remarks="Increase"
    if np<mp:
        inc07=round(mp-np+inc07,2)
        np=round(mp,2)
        remarks="Mini Pension"
    if dr>date(2007,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2007,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc07,np])
#restoration
d7=date(2007,7,1)
d8=date(2008,7,1)
if d7<restd<d8:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2008
if dr<d2008:
    inc08=round(np*0.20,2)
    cp=round(cp*1.20,2)
    np=round(np+inc08,2)
    remarks="Increase"
    if np<mp08:
        inc08=round(mp08-np+inc08,2)
        np=round(mp08,2)
        remarks="Mini Pension"
    if dr>date(2008,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2008,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc08,np])
#restoration
d8=date(2008,7,1)
d9=date(2009,7,1)
if d8<restd<d9:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2009
if dr<d2009:
    inc09=round(np*0.15,2)
    cp=round(cp*1.15,2)
    np=round(np+inc09,2)
    remarks="Increase"
    if np<mp08:
        inc09=round(mp08-np+inc09,2)
        np=round(mp08,2)
        remarks="Mini Pension"
    if dr>date(2009,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2009,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc09,np])
#restoration
d9=date(2009,7,1)
d10=date(2010,7,1)
if d9<restd<d10:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2010
if dr<d2017:
    inc10=round(np*0.15)
    cp=round(cp*1.15)
    np=round(np+inc10,2)
    remarks="Increase"
    
    if np<mp10:
        inc10=round(mp10-np+inc10,2)
        np=round(mp10,2)
        remarks="Mini Pension"
    
    if dr>date(2010,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2010,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc10,np])
#Medical Allowance
if bps<16:
    ma2010=round(np*0.25,2)
else:
    ma2010=round(np*.20,2)
ma2015=round(ma2010*0.25,2)
#restoration
d10=date(2010,7,1)
d11=date(2011,7,1)
if d10<restd<d11:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2011
if dr<d2002:
    inc11=round(np*0.20,2)
    cp=round(cp*1.20,2)
    np=round(np+inc11,2)
    remarks="Increase"
    if np<mp10:
        inc11=round(mp10-np+inc11,2)
        np=round(mp10,2)
       
        remarks="Mini Pension"
    if dr>date(2011,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2011,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc11,np])

elif dr>=d2002:
    inc11=round(np*0.15,2)
    np=round(np+inc11,2)
    cp=round(cp*1.15,2)
    remarks="Increase"
    if np<mp10:
        inc11=round(mp10-np+inc11,2)
        np=round(mp10,2)
        remarks="Mini Pension"
    if dr>date(2011,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2011,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc11,np])
#restoration
d11=date(2011,7,1)
d12=date(2012,7,1)
if d11<restd<d12:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2012
if dr<d2015:
    inc12=round(np*0.20,2)
    cp=round(cp*1.20,2)
    np=round(np+inc12,2)
    remarks="Increase"
    if np<mp10:
        inc12=round(mp10-inc12,2)
        np=round(mp10,2)
        remarks="Mini Pension"
    if dr>date(2012,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2012,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc12,np])
#restoration
d12=date(2012,7,1)
d13=date(2013,7,1)
if d12<restd<d13:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2013
if dr<d2016:
    inc13=round(np*0.10,2)
    cp=round(cp*1.10,2)
    np=round(np+inc13,2)
    remarks="Increase"
    if np<mp13:
        inc13=round(mp13-np+inc13,2)
        np=round(mp13,2)
        remarks="Mini Pension"
    if dr>date(2013,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2013,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc13,np])
#restoration
d13=date(2013,7,1)
d14=date(2014,7,1)
if d13<restd<d14:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2014
if dr<d2016:
    inc14=round(np*0.10,)
    cp=round(cp*1.10,2)
    np=round(np+inc14,2)
    remarks="Increase"
    if np<mp14:
        inc14=round(mp14-np+inc14,2)
        np=round(mp14,2)
        remarks="Mini Pension"
    if dr>date(2014,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2014,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc14,np])
#restoration
d14=date(2014,7,1)
d15=date(2015,7,1)
if d14<restd<d15:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2015
if dr:
    inc15=round(np*0.075,2)
    cp=round(cp*1.075,2)
    np=round(np+inc15,2)
    remarks="Increase"
    if np<mp14:
        inc15=round(mp14-np+inc15, 2)
        np=round(mp14,2)
        remarks="Mini Pension"
    if dr>date(2015,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2015,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc15,np])
#restoration
d15=date(2015,7,1)
d16=date(2016,7,1)
if d15<restd<d16:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2016
if dr:
    if cat=="Self":
        age85=db.replace(db.year+85)
    else:
        age85=dbf.replace(dbf.year+85)
    
    if age85<=date.today():
        inc16=round(np*0.25,2)
        cp=round(cp*1.25,2)
        np=round(np+inc16,2)
        if age85<=d16:
            remarks="25% increase"
        else:
            remarks="25% increase "+age85.strftime("%d-%m-%Y")+" no arrear prior to this date"
    else:
        inc16=round(np*0.10,2)
        cp=round(cp*1.10,2)
        np=round(np+inc16,2)
        remarks="Increase"
    if np<mp14:
        inc16=round(mp14-np+inc16,2)
        np=round(mp14,2)
        remarks="Mini Pension"
    if dr>date(2016,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2016,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc16,np])
    print(age85)
#restoration
d16=date(2016,7,1)
d17=date(2017,7,1)
if d16<restd<d17:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
    wef=restd.strftime("%d-%m-%Y")
    restored.append([remarks,wef,cp,np])
#Increase wef 1.07.2017
if dr:
    inc17=round(np*0.10,2)
    cp=round(cp*1.10,2)
    np=round(np+inc17,2)
    remarks="Increase"
    if np<mp14:
        inc17=round(mp14-np+inc17,2)
        np=round(mp14,2)
        remarks="Mini Pension"
    if dr>date(2017,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2017,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc17,np])
#restoration
d17=date(2017,7,1)
d18=date(2018,7,1)
if d17<restd<d18:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2018
if dr:
    if cat=="Self":
        age75=db.replace(db.year+75)
    else:
        age75=dbf.replace(dbf.year+75)
    
    inc18=round(np*0.10,2)
    cp=round(cp*1.10,2)
    np=round(np+inc18,2)
    remarks="Increase"
    if age75 > date(2018,7,1) and np<mp18:
        inc18=round(mp18-np+inc18,2)
        np=round(mp18,2)
        remarks="Mini Pension"
    elif age75 < date(2018,7,1) and np<mp75:
        inc18=round(mp75-np+inc18,2)
        np=round(mp75,2)
        remarks="Mini Pension"
    if dr>date(2018,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2018,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc18,np])
#75years mini penison
if age75<date(2019,7,1) and np<mp75:
    incm=round(mp75-np,2)
    np=round(mp75,2)
    remarks="Note: Pensioner has attained 75 years age on "+age75.strftime("%d-%m-%Y")+"\nMini Pension"
    wef=age75.strftime("%d-%m-%Y")
    inc.append([remarks,wef,incm,np])
#restoration
d18=date(2018,7,1)
d19=date(2019,7,1)
if d18<restd<d19:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2019
if dr:
    inc19=round(np*0.10,2)
    cp=round(cp*1.10,2)
    np=round(np+inc19,2)
    remarks="Increase"
    if age75 > date(2019,7,1) and np<mp18:
        inc18=round(mp18-np+inc18,2)
        np=round(mp18,2)
        remarks="Mini Pension"
    elif age75 < date(2019,7,1) and np<mp75:
        inc18=round(mp75-np+inc18,2)
        np=round(mp75,2)
        remarks="Mini Pension"
    if dr>date(2019,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2019,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc19,np])
#75years mini penison
if age75<date(2021,7,1) and np<mp75:
    incm=round(mp75-np,2)
    np=round(mp75,2)
    remarks="Note: Pensioner has attained 75 years age on "+age75.strftime("%d-%m-%Y")+"\nMini Pension"
    wef=age75.strftime("%d-%m-%Y")
    inc.append([remarks,wef,incm,np])
#restoration
d19=date(2019,7,1)
d21=date(2021,7,1)
if d19<restd<d21:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2021
if dr:
    inc21=round(np*0.10,2)
    cp=round(cp*1.10,2)
    np=round(np+inc21,2)
    remarks="Increase"
    if age75 > date(2021,7,1) and np<mp18:
        inc18=round(mp18-np+inc18,2)
        np=round(mp18,2)
        remarks="Mini Pension"
    elif age75 < date(2021,7,1) and np<mp75:
        inc18=round(mp75-np+inc18,2)
        np=round(mp75,2)
        remarks="Mini Pension"
    if dr>date(2021,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2021,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc21,np])
#75years minimum pension
if age75<date(2022,4,1) and np<mp75:
    incm=round(mp75-np,2)
    np=round(mp75,2)
    remarks="Note: Pensioner has attained 75 years age on "+age75.strftime("%d-%m-%Y")+"\nMini Pension"
    wef=age75.strftime("%d-%m-%Y")
    inc.append([remarks,wef,incm,np])
#restoration
d21=date(2021,7,1)
d22=date(2022,4,1)
if d21>restd>d22:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
#Increase wef 1.07.2022
if dr:
    inc22=round(np*0.10,2)
    cp=round(cp*1.102)
    np=round(np+inc22,2)
    remarks="Increase"
    if age75 > date(2022,4,1) and np<mp18:
        inc18=round(mp18-np+inc18,2)
        np=round(mp18,2)
        remarks="Mini Pension"
    elif age75 < date(2022,4,1) and np<mp75:
        inc18=round(mp75-np+inc18,2)
        np=round(mp75,2)
        remarks="Mini Pension"
    if dr>date(2022,4,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2022,7,1).strftime("%d-%m-%Y")
    inc.append([remarks,wef,inc22,np])
#75years minimum pension
if age75<date(2022,7,1) and np<mp75:
    incm=round(mp75-np,2)
    np=round(mp752)
    remarks="Note: Pensioner has attained 75 years age on "+age75.strftime("%d-%m-%Y")+"\nMini Pension"
    wef=age75.strftime("%d-%m-%Y")
    inc.append([remarks,wef,incm,np])
    tp=np+ma2010+ma2015 
#restoration
d22=date(2022,4,1)
d222=date(2022,7,1)
if d22>restd>d222:
    cp=round(cp,2)
    np=round(cp+np,2)
    restore=restd.strftime("%d-%m-%Y")
    remarks="Restored"
    inc.append([remarks,restore,cp,np])
print("Description \tstarts from \tinc  \tNet pension \tAmount ")
for l,k,m, n in inc:
    print(f"{l} \t{k} \tRs.{m}\t Net Pension\t Rs.{n}")

tp=np+ma2010+ma2015
print(tp)
    