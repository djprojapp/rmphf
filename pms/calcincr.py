from datetime import date
dor=date(2007,8,25)
d2002=date(2002,7,1)
d2005=date(2005,7,1)
d2007=date(2007,7,1)
d2008=date(2008,7,1)
d2009=date(2009,7,1)
d2011=date(2011,7,1)
d2015=date(2015,7,1)
d2016=date(2016,7,1)
d2017=date(2017,7,1)
res_date=date(20015,8,25)
np=20748
inc=[]
res=[]
if dor<d2005:
    inc03=round(np*0.15)
    np=np+inc03
    if np<300:
        np=300
        inc03=np-inc03
    if dor>date(2003,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2003,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc03,np])

if dor<d2005:
    inc04=round(np*0.08)
    np=np+inc04
    if np<300:
        np=300
        inc04=np-inc04
    if dor>date(2004,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2004,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc04,np])
    

if dor<d2011:
    inc05=round(np*0.10)
    np=np+inc05
    if np<300:
        np=300
        inc05=np-inc05
    if dor>date(2005,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2005,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc05,np])
if dor<d2011:
    inc06=round(np*0.15)
    np=np+inc06
    if np<300:
        np=300
        inc06=np-inc06
    if dor>date(2006,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2006,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc06,np])
    
if dor<d2007:
    inc07=round(np*0.15)
    np=np+inc07
    if np<300:
        np=300
        inc07=np-inc07
    if dor>date(2007,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2007,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc07,np])

if dor<d2008:
    inc08=round(np*0.20)
    np=np+inc08
    if np<2000:
        np=2000
        inc08=np-inc08
    if dor>date(2008,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2008,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc08,np])
if dor<d2009:
    inc09=round(np*0.15)
    np=np+inc09
    if np<2000:
        np=2000
        inc09=np-inc09
    if dor>date(2009,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2009,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc09,np])
if dor<d2017:
    inc10=round(np*0.15)
    np=np+inc10
    if np<3000:
        np=3000
        inc10=np-inc10
    if dor>date(2010,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2010,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc10,np])
if dor<d2002:
    inc11=round(np*0.20)
    np=np+inc11
    if np<3000:
        np=3000
        inc11=np-inc11
    if dor>date(2011,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2011,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc11,np])
elif dor>=d2002:
    inc11=round(np*0.15)
    np=np+inc11
    if np<3000:
        np=3000
        inc11=np-inc11
    if dor>date(2011,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2011,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc11,np])
if dor<d2015:
    inc12=round(np*0.20)
    np=np+inc12
    if np<3000:
        np=3000
        inc12=np-inc12
    if dor>date(2012,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2012,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc12,np])
if dor<d2016:
    inc13=(np*0.10)
    np=np+inc13
    if dor>date(2013,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2013,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc13,np])
if dor<d2016:
    inc14=round(np*0.10)
    np=np+inc14
    if dor>date(2014,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2014,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc14,np])
if dor:
    inc15=round(np*0.075)
    np=np+inc15
    if dor>date(2015,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2015,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc15,np])

if dor:
    inc16=round(np*0.10)
    np=np+inc16
    if dor>date(2016,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2016,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc16,np])

if dor:
    inc17=round(np*0.10)
    np=np+inc17
    if dor>date(2017,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2017,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc17,np])

if dor:
    inc18=round(np*0.10)
    np=np+inc18
    if dor>date(2018,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2018,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc18,np])

if dor:
    inc19=round(np*0.10)
    np=np+inc19
    if dor>date(2019,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2019,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc19,np])

if dor:
    inc21=round(np*0.10)
    np=np+inc21
    if dor>date(2021,7,1):
        wef=dor.strftime("%d-%m-%Y")
    else:
        wef=date(2021,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc21,np])



