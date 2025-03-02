import tkinter as tk
from tkinter import *
root=Tk()
root.title("simple calculator")
root.maxsize(500,500)
root.minsize(420,600)
root.resizable(False,False)
root.configure(bg="#17161b")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
       try:
           equation = equation.replace("^", "**")
           result=eval(equation)
           label_result.config(text=result)
           equation = str(result)
       except:
           label_result.config(text="Error")
           equation =""


label_result=Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=130,y=100)
Button(root,text="%",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=250,y=100)
Button(root,text="*",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=370,y=100)


Button(root,text="7",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2b36",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=130,y=200)
Button(root,text="9",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=250,y=200)
Button(root,text="^",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("^")).place(x=370,y=200)


Button(root,text="4",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2b36",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=130,y=300)
Button(root,text="6",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=250,y=300)
Button(root,text="-",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=370,y=300)


Button(root,text="1",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2b36",command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=130,y=400)
Button(root,text="3",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=250,y=400)
Button(root,text="+",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=370,y=400)


Button(root,text="00",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2b36",command=lambda:show("00")).place(x=10,y=500)
Button(root,text="0",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=130,y=500)
Button(root,text=".",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=250,y=500)
Button(root,text="=",width=4,height=1,font=("arial",30,"bold"),bd=2,fg="#fff",bg="#fe9037",command=calculate).place(x=370,y=500)

root.mainloop()
