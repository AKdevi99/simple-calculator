from tkinter import *

win=Tk()
#window setting
win.config(bg="black")
win.title("simple calculator")
total=0
p=0
#function
def button_click(number):

    current=display.get()
    display.delete(0,END)#delete the things on screen to avoid repeation
    display.insert(0,str(current)+str(number))

def add_func():
    x=display.get()
    display.delete(0,END)
    global total,op
    total+=int(x)
    op="+"

def sub_func():
    x=display.get()
    display.delete(0,END)
    global total,op,p
    if(p==0):
        total+=int(x)
        p+=1
    else:
        total-=int(x)
    op = "-"

def mul_func():
    x=display.get()
    display.delete(0,END)
    global total,op
    total=1
    total *= int(x)
    op = "*"

def div_func():
    x=display.get()
    display.delete(0,END)
    global total,op
    total = int(x)
    op = "/"



def equal_button():
    global total,op
    y=int(display.get())
    if(op=="+"):
        total+=y
    elif (op=='-'):
        total-=y
    elif(op=='*'):
        total*=y
    elif(op=='/'):
        total=float(total)/y
    display.delete(0,END)
    display.insert(0,str(total))



def clear_display():
    display.delete(0,END)
    global total,p
    total=0
    p=0



#creating stuff

display=Entry(win,width=45,borderwidth=10)
num_1=Button(win,text="1",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(1))
num_2=Button(win,text="2",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(2))
num_3=Button(win,text="3",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(3))
num_4=Button(win,text="4",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(4))
num_5=Button(win,text="5",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(5))
num_6=Button(win,text="6",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(6))
num_7=Button(win,text="7",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(7))
num_8=Button(win,text="8",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(8))
num_9=Button(win,text="9",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(9))
num_0=Button(win,text="0",fg="white",bg="black",padx=30,pady=25,command=lambda :button_click(0))
add_button=Button(win,text="+",fg="white",bg="black",padx=30,pady=25,command=add_func)
sub_button=Button(win,text="-",fg="white",bg="black",padx=30,pady=25,command=sub_func)
mul_button=Button(win,text="*",fg="white",bg="black",padx=30,pady=25,command=mul_func)
div_button=Button(win,text="/",fg="white",bg="black",padx=30,pady=25,command=div_func)
eql_button=Button(win,text="=",fg="white",bg="black",padx=30,pady=25,width=12,command=equal_button)
clr_button=Button(win,text="CE",fg="white",bg="black",padx=26,pady=25,command=clear_display)

#sorting stuff
display.grid(row=1,column=0,columnspan=4,pady=30)
num_7.grid(row=2,column=0)
num_8.grid(row=2,column=1)
num_9.grid(row=2,column=2)
div_button.grid(row=2,column=3)
num_4.grid(row=3,column=0)
num_5.grid(row=3,column=1)
num_6.grid(row=3,column=2)
mul_button.grid(row=3,column=3)
num_3.grid(row=4,column=0)
num_2.grid(row=4,column=1)
num_1.grid(row=4,column=2)
sub_button.grid(row=4,column=3)
eql_button.grid(row=5,column=0,columnspan=2)
add_button.grid(row=5,column=3)
clr_button.grid(row=5,column=2)



win=mainloop()