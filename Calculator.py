from  tkinter import *
from  tkinter import ttk
from  tkinter import messagebox
import operator
#system
def insert(numbers):
      global operator
      operator+=str(numbers)
      screen_entry.set(operator)
def clr():
      global operator
      operator=" "
      screen_entry.set("")
def equal():
      global operator
      ope=str(eval(operator))
      screen_entry.set(ope)
      operator=""
      def Ans():
            screen_entry.set(ope)
def delet():
      length=len(screen.get())
      screen.delete(length-1, 'end')

      


window=Tk()
window.title("Calculator")
window.iconbitmap(r'python\Calculator.ico')
operator=""
screen_entry=StringVar()
#grafical
#calculator screen

screen= ttk.Entry(window, width=62,state=DISABLED, textvariable=screen_entry, cursor="hand2",)
screen.grid(row=0, column=0, columnspan=4, ipady=15, ipadx=15, pady=5, padx=5)
#enable edite on screen
#( button )button
buRight=ttk.Button(window, text="(", cursor="hand2", command= lambda:insert("(")).grid(row=2, column=0, ipady=15, ipadx=15)
buLeft=ttk.Button(window, text=")", cursor="hand2", command= lambda:insert(")")).grid(row=2, column=1, ipady=15, ipadx=15)
#Del
Dele=ttk.Button(window, text="Del", cursor="hand2", command=lambda:delet()).grid(row=2, column=3, ipady=15, ipadx=10)
#CE
Ce=ttk.Button(window, text="CE", cursor="hand2", command= lambda:clr()).grid(row=2, column=2, ipady=15, ipadx=15)
#row1
bu7=ttk.Button(window, text="7", cursor="hand2", command= lambda:insert(7)).grid(row=3, column=0,ipady=15, ipadx=15)
bu8=ttk.Button(window, text="8",cursor="hand2" , command= lambda:insert(8)).grid(row=3, column=1,ipady=15, ipadx=15)
bu9=ttk.Button(window, text="9", cursor="hand2",  command= lambda:insert(9) ).grid(row=3, column=2,ipady=15, ipadx=15)
#plus button
bu_plus=ttk.Button(window, text="+",  command= lambda:insert("+")).grid(row=3, column=3, ipady=15, ipadx=10)
#row2
bu4=ttk.Button(window, text="4", cursor="hand2",  command= lambda:insert(4)).grid(row=4, column=0,ipady=15, ipadx=15)
bu5=ttk.Button(window, text="5", cursor="hand2",  command= lambda:insert(5)).grid(row=4, column=1,ipady=15, ipadx=15)
bu6=ttk.Button(window, text="6", cursor="hand2",  command= lambda:insert(6)).grid(row=4, column=2,ipady=15, ipadx=15)
#min button
bu_mins=ttk.Button(window, text="-", cursor="hand2",  command= lambda:insert("-")).grid(row=4, column=3,ipady=15, ipadx=10)
#row3
bu1=ttk.Button(window, text="1", cursor="hand2",  command= lambda:insert(1)).grid(row=5, column=0,ipady=15, ipadx=15)
bu2=ttk.Button(window, text="2", cursor="hand2",  command= lambda:insert(2)).grid(row=5, column=1,ipady=15, ipadx=15)
bu3=ttk.Button(window, text="3", cursor="hand2",  command= lambda:insert(3)).grid(row=5, column=2,ipady=15, ipadx=15)
#mult button
bu_Multi=ttk.Button(window, text="x", cursor="hand2",  command= lambda:insert("*")).grid(row=5, column=3,ipady=15, ipadx=10)
#row4
bu0=ttk.Button(window, text="0", cursor="hand2",  command= lambda:insert(0)).grid(row=6, column=0,ipady=15, ipadx=15)
bu_dot=ttk.Button(window, text=".", cursor="hand2",  command= lambda:insert(".")).grid(row=6, column=1,ipady=15, ipadx=15)
bu_mod=ttk.Button(window, text="Mod", cursor="hand2",  command= lambda:insert("%")).grid(row=8, column=3,ipady=15, ipadx=10)
#dev button
bu_dev=ttk.Button(window, text="/", cursor="hand2",  command= lambda:insert("/")).grid(row=6, column=3,ipady=15, ipadx=10)
#dubl dev
bu_dbl=ttk.Button(window, text="//", cursor="hand2",  command= lambda:insert("//")).grid(row=6, column=2,ipady=15, ipadx=15)
#Ans button
bu_Ans=ttk.Button(window, text="Ans", cursor="hand2", command=lambda:equal()).grid(row=7, column=0,ipady=15, ipadx=15)
#equal
eq=ttk.Button(window, text="=",width=34, cursor="hand2", command= lambda:equal())
eq.grid(row=8, column=1, columnspan=2,ipady=15)
#additionalo row
buint=ttk.Button(window, text="int", cursor="hand2",  command= lambda:insert("int(")).grid(row=7, column=1,ipady=15, ipadx=15)
bufloat=ttk.Button(window, text="flo", cursor="hand2",  command= lambda:insert("float(")).grid(row=7, column=2,ipady=15, ipadx=15)
bucomplex=ttk.Button(window, text="cpx", cursor="hand2",  command= lambda:insert("complex(")).grid(row=7, column=3,ipady=15, ipadx=10)
quite=ttk.Button(window, text="Exit", cursor="hand2",  command=quit).grid(row=8, column=0,ipady=15, ipadx=15)



window.mainloop()
