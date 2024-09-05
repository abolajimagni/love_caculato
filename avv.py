from tkinter import *
import tkinter

root=Tk()
root.geometry('700x250')
root.title('Love Caculator')
root.configure(background='#101010')

def cal():
    your_name=y_entry.get()
    partner_name=p_entry.get()
    name=your_name+partner_name
    lower=name.lower()
    t=lower.count('t')
    r=lower.count('r')
    u=lower.count('u')
    e=lower.count('e')
    l=lower.count('l')
    o=lower.count('o')
    v=lower.count('v')
    e=lower.count('e')
    caculate= t+r+u+e
    caculate2=l+o+v+e
    truelove=str(caculate)+ str(caculate2)
    result1=(truelove+'%')
    result.insert(0,result1)

    check2=int(truelove)

    if check2 >=90:
       remark.insert(1,"You are highly compatible")
    elif check2 <=89 and check2 > 70:
       remark.insert(1,"You are compatible")
    elif check2 <= 69 and check2 > 50:
       remark.insert(1,"You will get along")
    else:
       remark.insert(0,"You are not too close... but she may be right partner")



frame=tkinter.Frame()
frame.configure(background='#101010',)
frame.pack(pady=50)


title= Label(root,text='Love caculator',bg='#101010',fg='magenta')
p_name=Label(frame, text='Yours Name: ', bg="#101010",fg='#ffffff', font=('arial',12,"bold"))
p_entry=Entry(frame, background='white', foreground='orange',
             borderwidth=5, relief='raised',width=40, )
y_name=Label(frame, text="Patner's Name: ",bg="#101010",fg='#ffffff', font=('arial',12,"bold") )

y_entry= Entry(frame, background='white', foreground='orange',
             borderwidth=5, relief='raised',width=40, )
caculate=Button(frame,text='Caculate', command=cal)
result=Entry(frame,bg='#101010',fg="antiquewhite1", border=0)
r_label=Label(frame,text='Remark',bg='#101010', fg= 'red',font=('arial' , 14 , 'italic'))
remark=Entry(frame,bg='#101010',fg='white',width=47,font=('arial 10',14,'bold italic'))

title.pack()
p_name.grid(row=0,column=0)
p_entry.grid(row=0,column=1)
y_name.grid(row=1,column=0, pady=10)
y_entry.grid(row=1, column=1,)
caculate.grid(row=2, column=1, columnspan=6)
result.grid(row=2,column=2)
r_label.grid(row=3,column=0)
remark.grid(row=3, column=1)
frame.pack()




root.mainloop()