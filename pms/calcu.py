from datetime import datetime, date
import tkinter as tk

np=2500
dr=date(2007,8,25)
d2002=date(2002,7,1)
d2005=date(2005,7,1)
d2007=date(2007,7,1)
d2008=date(2008,7,1)
d2009=date(2009,7,1)
d2011=date(2011,7,1)
d2015=date(2015,7,1)
d2016=date(2016,7,1)
d2017=date(2017,7,1)
ma2010=round(np*0.25)
ma2015=round(ma2010*0.25)

inc=[]
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
if dr<d2005:
    inc03=round(np*0.15)
    np=np+inc03
    if np<300:
        np=300
        inc03=np-inc03
    if dr>date(2003,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2003,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc03,np])

if dr<d2005:
    inc04=round(np*0.08)
    np=np+inc04
    if np<300:
        np=300
        inc04=np-inc04
    if dr>date(2004,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2004,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc04,np])
    

if dr<d2011:
    inc05=round(np*0.10)
    np=np+inc05
    if np<300:
        np=300
        inc05=np-inc05
    if dr>date(2005,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2005,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc05,np])
if dr<d2011:
    inc06=round(np*0.15)
    np=np+inc06
    if np<300:
        np=300
        inc06=np-inc06
    if dr>date(2006,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2006,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc06,np])
    
if dr<d2007:
    inc07=round(np*0.15)
    np=np+inc07
    if np<300:
        np=300
        inc07=np-inc07
    if dr>date(2007,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2007,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc07,np])

if dr<d2008:
    inc08=round(np*0.20)
    np=np+inc08
    if np<2000:
        np=2000
        inc08=np-inc08
    if dr>date(2008,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2008,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc08,np])
if dr<d2009:
    inc09=round(np*0.15)
    np=np+inc09
    if np<2000:
        np=2000
        inc09=np-inc09
    if dr>date(2009,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2009,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc09,np])
if dr<d2017:
    inc10=round(np*0.15)
    np=np+inc10
    ma2010=round(np*0.25)
    ma2015=round(ma2010*0.25)
    if np<3000:
        np=3000
        inc10=np-inc10
    if dr>date(2010,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2010,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc10,np])
if dr<d2002:
    inc11=round(np*0.20)
    np=np+inc11
    if np<3000:
        np=3000
        inc11=np-inc11
    if dr>date(2011,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2011,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc11,np])
elif dr>=d2002:
    inc11=round(np*0.15)
    np=np+inc11
    if np<3000:
        np=3000
        inc11=np-inc11
    if dr>date(2011,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2011,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc11,np])
if dr<d2015:
    inc12=round(np*0.20)
    np=np+inc12
    if np<3000:
        np=3000
        inc12=np-inc12
    if dr>date(2012,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2012,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc12,np])
if dr<d2016:
    inc13=round(np*0.10)
    np=np+inc13
    if dr>date(2013,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2013,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc13,np])
if dr<d2016:
    inc14=round(np*0.10)
    np=np+inc14
    if dr>date(2014,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2014,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc14,np])
if dr:
    inc15=round(np*0.075)
    np=np+inc15
    if dr>date(2015,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2015,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc15,np])

if dr:
    inc16=round(np*0.10)
    np=np+inc16
    if dr>date(2016,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2016,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc16,np])

if dr:
    inc17=round(np*0.10)
    np=np+inc17
    if dr>date(2017,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2017,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc17,np])

if dr:
    inc18=round(np*0.10)
    np=np+inc18
    if dr>date(2018,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2018,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc18,np])

if dr:
    inc19=round(np*0.10)
    np=np+inc19
    if dr>date(2019,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2019,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc19,np])

if dr:
    inc21=round(np*0.10)
    np=np+inc21
    if dr>date(2021,7,1):
        wef=dr.strftime("%d-%m-%Y")
    else:
        wef=date(2021,7,1).strftime("%d-%m-%Y")
    inc.append([wef,inc21,np])
    tp=np+ma2010+ma2015

cl=tk.Tk()
cl.geometry('500x620+200+100')
def show(msg,gross):
    gross=2500
    msg.config(text="pension= %d" %gross)
    return
msg=tk.Label(cl, text="Pension").grid(row=5, column=5)
buton=tk.Button(cl, text="Pension",command=show ).grid(row=1,column=1)
cl.mainloop()
