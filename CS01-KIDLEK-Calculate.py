from tkinter import *
root = Tk()
root.title("เครื่องคิดเลข")

content = ""
textinput = StringVar(value = "0")

def btn(number):
    global content
    content = content+str(number)
    textinput.set(content)

def equal():
    global content
    calcu = float(eval(content))
    textinput.set(calcu)
    content = ""

def clear ():
    global content
    content = ""
    textinput.set("")
    YAY.insert(0,"0")

YAY = Entry(font = (30),fg="white",bg="black",textvariable=textinput,justify="right")
YAY.grid(columnspan=4)



but7=Button(fg="black",font=(30),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
but8=Button(fg="black",font=(30),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
but9=Button(fg="black",font=(30),text="9",command=lambda:btn(79),padx=30,pady=15).grid(row=1,column=2)
butc=Button(fg="black",bg="yellow",font=(30),text="C",command = clear,padx=30,pady=15).grid(row=1,column=3)

but4=Button(fg="black",font=(30),text="4",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
but5=Button(fg="black",font=(30),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
but6=Button(fg="black",font=(30),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
butplus=Button(fg="black",bg="yellow",font=(30),command=lambda:btn("+"),text="+",padx=30,pady=15).grid(row=2,column=3)

but1=Button(fg="black",font=(30),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=3,column=0)
but2=Button(fg="black",font=(30),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=3,column=1)
but3=Button(fg="black",font=(30),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=3,column=2)
butminus=Button(fg="black",bg="yellow",font=(30),command=lambda:btn("-"),text="-",padx=30,pady=15).grid(row=3,column=3)

but0=Button(fg="black",font=(30),text="0",command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
butdot=Button(fg="black",font=(30),text=".",command=lambda:btn("."),padx=30,pady=15).grid(row=4,column=0)
buthan=Button(fg="black",bg="yellow",font=(30),command=lambda:btn("/"),text="/",padx=30,pady=15).grid(row=4,column=2)
butkoon=Button(fg="black",bg="yellow",font=(30),command=lambda:btn("*"),text="x",padx=30,pady=15).grid(row=4,column=3)

buteq=Button(fg="black",bg="green",font=(30),command=equal,text="=",padx=80,pady=15).grid(row=5,column=0,columnspan=2)
butopen=Button(fg="black",bg="yellow",font=(30),command=lambda:btn("("),text="(",padx=35,pady=15).grid(row=5,column=2)
butclose=Button(fg="black",bg="yellow",font=(30),command=lambda:btn(")"),text=")",padx=35,pady=15).grid(row=5,column=3)

root.mainloop()