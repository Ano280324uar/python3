from tkinter import * #import all element
from tkinter import ttk #import ttk
import pyautogui
import time


window = Tk()
window.title("Auto print")
window.geometry("300x300+650+250")






#firt entery
la=ttk.Label(window, text="Enter your text:").grid(row=0, column=0, padx=5, pady=5)
e1=ttk.Entry(window)
e1.grid(row=0,column=1)

#2nd entry
lb=ttk.Label(window, text="Enter number of time:").grid(row=2, column=0, padx=5, pady=5)
e2=ttk.Entry(window)
e2.grid(row=2,column=1)

#3rd entry
lc=ttk.Label(window, text="Enter time (S):").grid(row=3, column=0, padx=5, pady=5)
e3=ttk.Entry(window)
e3.grid(row=3,column=1)
def submit():
      time.sleep(5)
      for i in range(int(e2.get())):
           pyautogui.typewrite(e1.get())
           pyautogui.typewrite("\n")
           time.sleep(int(e3.get())/int(e2.get())) #intger number is a float 10 = 10.0 //but float is not an intger 10.8 = 10

#submit
bu1=ttk.Button(window, text="enter" ,cursor="hand2", command=submit).grid(row=4,column=0, columnspan=3)
quite=ttk.Button(window, text="Quit", command=quit, cursor="hand2").grid(row=6, column=0, columnspan=3, padx=30 ,pady=5)






window.mainloop()