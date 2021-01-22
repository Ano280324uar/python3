from hashlib import *
import hashlib
#------------------------#
from tkinter import *
from tkinter import ttk
#------------------------#
import time
#------------------------#
import pyperclip
#----Create window-------#
window=Tk()
window.title("Word encryptor")
window.geometry("600x450+500+200")
#----Create fonction------#
def hex_md5():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexmd5=md5(encoded).hexdigest()
      out.insert(0, hexmd5)
      time.sleep(0.1)
      

def hex_sha1():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexsha1=sha1(encoded).hexdigest()
      out.insert(0, hexsha1)
      time.sleep(0.1)


def hex_sha256():
      out.delete(0, END)
      time.sleep(0.5)
      encoded=word.get().encode('utf-8')
      hexsha256=sha256(encoded).hexdigest()
      out.insert(0, hexsha256)
      time.sleep(0.1)


def hex_sha512():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexsha512=sha512(encoded).hexdigest()
      out.insert(0, hexsha512)
      time.sleep(0.1)

def hex_shake128():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexshake128=shake_128(encoded).hexdigest()
      out.insert(0, hexshake128)
      time.sleep(0.1)

def hex_shake256():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexshake256=shake_256(encoded).hexdigest()
      out.insert(0, hexshake256)
      time.sleep(0.1)

def hex_sha224():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexsha224=sha224(encoded).hexdigest()
      out.insert(0, hexsha224)
      time.sleep(0.1)

def hex_sha3512():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexsha3512=sha3_512(encoded).hexdigest()
      out.insert(0, hexsha3512)
      time.sleep(0.1)

def hex_blake2s():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexblake2s=blake2s(encoded).hexdigest()
      out.insert(0, hexblake2s)
      time.sleep(0.1)

def hex_blake2b():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexblake2b=blake2b(encoded).hexdigest()
      out.insert(0, hexblake2b)
      time.sleep(0.1)

def hex_sha3384():
      out.delete(0, END)
      time.sleep(0.2)
      encoded=word.get().encode('utf-8')
      hexsha3384=sha3_384(encoded).hexdigest()
      out.insert(0, hexsha3384)
      time.sleep(0.1)

def copy():
      pyperclip.copy(out.get())
      out.delete(0, END)
      time.sleep(0.2)
      out.insert(0, "Thanks for using this encryptor tool")
      

#----Create Content-------#
title=ttk.Label(window, text="Welcome to word encryptor", font='Bold')
title.grid(row=0, column=1, columnspan=2, pady=20)
#-------------------------#
word=ttk.Entry(window, width=90)
word.grid(row=1, column=0, columnspan=4, padx=20, pady=5, ipadx=5, ipady=10)
#----------Buttons--------#
bu_md5=ttk.Button(window, text="md5", cursor='hand2',command= lambda:hex_md5())
bu_md5.grid(row=2, column=0, ipadx=20, ipady=10,  pady=20, )

bu_sha1=ttk.Button(window, text="sha1", cursor='hand2',command= lambda:hex_sha1())
bu_sha1.grid(row=2, column=1, ipadx=20, ipady=10,  pady=20)

bu_sha256=ttk.Button(window, text="sha256", cursor='hand2',command= lambda:hex_sha256())
bu_sha256.grid(row=2, column=2, ipadx=20, ipady=10,  pady=20)

bu_sha384=ttk.Button(window, text="sha384", cursor='hand2',command= lambda:hex_sha512())
bu_sha384.grid(row=2, column=3, ipadx=20, ipady=10,  pady=20)
##
bu_shake_128=ttk.Button(window, text="shake128", cursor='hand2',command= lambda:hex_shake128())
bu_shake_128.grid(row=3, column=0, ipadx=20, ipady=10,  )

bu_shake_256=ttk.Button(window, text="shake256", cursor='hand2',command= lambda:hex_shake256())
bu_shake_256.grid(row=3, column=1, ipadx=20, ipady=10, )

bu_sha224=ttk.Button(window, text="sha224", cursor='hand2',command= lambda:hex_sha224())
bu_sha224.grid(row=3, column=2, ipadx=20, ipady=10, )

bu_sha3512=ttk.Button(window, text="sha3/512", cursor='hand2',command= lambda:hex_sha3512())
bu_sha3512.grid(row=3, column=3, ipadx=20, ipady=10,)
#""
bu_blake2s=ttk.Button(window, text="blake2s", cursor='hand2',command= lambda:hex_blake2s())
bu_blake2s.grid(row=4, column=0, ipadx=20, ipady=10,  pady=20)

bu_blake2b=ttk.Button(window, text="blake2b", cursor='hand2',command= lambda:hex_blake2b())
bu_blake2b.grid(row=4, column=1, ipadx=20, ipady=10, pady=20)

bu_whirlpool=ttk.Button(window, text="sha3/384", cursor='hand2',command= lambda:hex_sha3384())
bu_whirlpool.grid(row=4, column=2, ipadx=20, ipady=10, pady=20)

bu_sha512=ttk.Button(window, text="sha512", cursor='hand2',command= lambda:hex_sha512())
bu_sha512.grid(row=4, column=3, ipadx=20, ipady=10, pady=20)


#-----------------------#
out=ttk.Entry(window, width=90)
out.grid(row=6, column=0, columnspan=4, padx=20, pady=5, ipadx=5, ipady=10)
#-----------------------#
bu_cp=ttk.Button(window, text="Copy", cursor='hand2', command= lambda:copy())
bu_cp.grid(row=7, column=1, columnspan=2, ipadx=20, ipady=10,  pady=20)




window.mainloop()
