from tkinter import *
import random
import time
i3=Tk()
i3.configure(cursor="shuttle")

l=["Mercury","Venus","Earth","Mars","jupiter","Saturn","Uranus","Neptune"]*2
random.shuffle(l)

l1=[]
l2=[]
l3=[]

b1=Button(i3,text="1")
b2=Button(i3,text="1")
b3=Button(i3,text="1")
b4=Button(i3,text="1")
b5=Button(i3,text="1")
b6=Button(i3,text="1")
b7=Button(i3,text="1")
b8=Button(i3,text="1")
b9=Button(i3,text="1")
b10=Button(i3,text="1")
b11=Button(i3,text="1")
b12=Button(i3,text="1")
b13=Button(i3,text="1")
b14=Button(i3,text="1")
b15=Button(i3,text="1")
b16=Button(i3,text="1")

class button_command:
    def __init__(self,button,text):
        self.text=text
        self.button=button
    def f(self):
        global l1
        global l2
        global l3
        if self.button not in l2:
            l1.append(self.text)
            l2.append(self.button)
            self.button.configure(text=self.text)
            if len(l2)!=0:
                if len(l1)==2:
                    self.button.update_idletasks()
                    time.sleep(0.8)
                    if l1[0]!=l1[1]:
                        for i in l2:
                            i.configure(text="1")
                        l1=[]
                        l2=[]
                    else:
                        for i in l2:
                            i.configure(command=lambda:None)
                            l3.append(i)
                        l1=[]
                        l2=[]
        if len(l3)==16:
            i3.destroy()
            i4=Tk()
            p1=Label(i4,text="Congratulation!!\n You won",font="times 25 italic")
            i4.rowconfigure(0,weight=1)
            i4.columnconfigure(0,weight=1)
            p1.grid(row=0,column=0,sticky=NSEW)

a=button_command(b1,l[0])
b=button_command(b2,l[1])
c=button_command(b3,l[2])
d=button_command(b4,l[3])
e=button_command(b5,l[4])
f=button_command(b6,l[5])
g=button_command(b7,l[6])
h=button_command(b8,l[7])
i=button_command(b9,l[8])
j=button_command(b10,l[9])
k=button_command(b11,l[10])
Q=button_command(b12,l[11])
m=button_command(b13,l[12])
n=button_command(b14,l[13])
o=button_command(b15,l[14])
p=button_command(b16,l[15])


b1.configure(command=a.f)
b2.configure(command=b.f)
b3.configure(command=c.f)
b4.configure(command=d.f)
b5.configure(command=e.f)
b6.configure(command=f.f)
b7.configure(command=g.f)
b8.configure(command=h.f)
b9.configure(command=i.f)
b10.configure(command=j.f)
b11.configure(command=k.f)
b12.configure(command=Q.f)
b13.configure(command=m.f)
b14.configure(command=n.f)
b15.configure(command=o.f)
b16.configure(command=p.f)

i3.rowconfigure(0,weight=1)
i3.rowconfigure(1,weight=1)
i3.rowconfigure(2,weight=1)
i3.rowconfigure(3,weight=1)
i3.columnconfigure(0,weight=1)
i3.columnconfigure(1,weight=1)
i3.columnconfigure(2,weight=1)
i3.columnconfigure(3,weight=1)

b1.grid(row=0,column=0,sticky=NSEW)

b2.grid(row=0,column=1,sticky=NSEW)

b3.grid(row=0,column=2,sticky=NSEW)

b4.grid(row=0,column=3,sticky=NSEW)

b5.grid(row=1,column=0,sticky=NSEW)

b6.grid(row=1,column=1,sticky=NSEW)

b7.grid(row=1,column=2,sticky=NSEW)

b8.grid(row=1,column=3,sticky=NSEW)

b9.grid(row=2,column=0,sticky=NSEW)

b10.grid(row=2,column=1,sticky=NSEW)

b11.grid(row=2,column=2,sticky=NSEW)

b12.grid(row=2,column=3,sticky=NSEW)

b13.grid(row=3,column=0,sticky=NSEW)

b14.grid(row=3,column=1,sticky=NSEW)

b15.grid(row=3,column=2,sticky=NSEW)

b16.grid(row=3,column=3,sticky=NSEW)

i3.mainloop()