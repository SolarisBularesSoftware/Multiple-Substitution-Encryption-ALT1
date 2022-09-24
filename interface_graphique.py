#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
user interface
	
"""

from MSE import mse_cipher,mse_decipher

from tkinter import*

def get_user_entry():
	return entree.get("1.0",'end-1c')


def mse_cip():
	msg = get_user_entry()

	code = mse_cipher(msg)

	entree.delete('1.0', END)
	entree.insert(1.0, code)


def mse_dec():
	code = get_user_entry()

	msg = mse_decipher(code)

	entree.delete('1.0', END)
	entree.insert(1.0, msg)


app = Tk()
app.title("MSE UI V2")
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))

app.config(bg="#192D46")

larg_cons = 400
larg_entry = w-larg_cons
font_size = 20

entree = StringVar()
entree = Text(app, width=w, height=20,bg="#864149",fg='#fff',
font=("Monospace", font_size))
entree.config(insertbackground="#fff")
entree.pack(side='top')
entree.focus()

cip_btn = Button(app,text="Chiffrer",bg="#19D1A4",fg="#fff",
relief=FLAT,font=("Monospace", font_size),command=mse_cip)
cip_btn.pack(side='left',padx=20,pady=20)

dec_btn = Button(app,text="Déchiffrer",bg="#C9787D",fg="#fff",
relief=FLAT,font=("Monospace", font_size),command=mse_dec)
dec_btn.pack(side='left',padx=20,pady=20)


app.mainloop()
