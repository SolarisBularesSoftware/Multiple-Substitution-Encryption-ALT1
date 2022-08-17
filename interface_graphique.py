#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
user interface
	
"""

from random import choice,randint
from pyperclip import copy,paste

from configs.parametre import*

from bloc_a import complexi,decomplex
from bloc_b import cipher,decipher
from bloc_c import chaos,dechaos

#from tools import rebuild,reinitialiser,mixer,gen_para_aleatoire

from tkinter import*

def get_user_entry():
	return entree.get("1.0",'end-1c')

def mse_cipher():
	"""
	|A| --> |B| --> |C|
	"""
	msg = get_user_entry()
	
	a  = complexi(msg)
	b = cipher(a)
	c = chaos(b,randint(mini,maxi))
	
	copy(c)
	
	entree.delete('1.0', END)
	entree.insert(1.0, c)


def mse_decipher():
	"""
	|C| --> |B| --> |A|
	"""
	code = get_user_entry()
	
	c = dechaos(code)
	b = decipher(c)
	a = decomplex(b)
	
	entree.delete('1.0', END)
	entree.insert(1.0, a)


app = Tk()
app.title("MSE UI V1")
w, h = app.winfo_screenwidth(), app.winfo_screenheight()
app.geometry("%dx%d+0+0" % (w, h))

app.config(bg="#192D46")

larg_cons = 400
larg_entry = w-larg_cons
font_size = 20

entree = StringVar()
entree = Text(app, width=w, height=20,bg="#864149",fg='#fff', font=("Monospace", font_size))
entree.config(insertbackground="#fff")
entree.pack(side='top')
entree.focus()

cip_btn = Button(app,text="Chiffrer",bg="#19D1A4",fg="#fff",relief=FLAT,font=("Monospace", font_size),command=mse_cipher)
cip_btn.pack(side='left',padx=20,pady=20)

dec_btn = Button(app,text="Déchiffrer",bg="#C9787D",fg="#fff",relief=FLAT,font=("Monospace", font_size),command=mse_decipher)
dec_btn.pack(side='left',padx=20,pady=20)


app.mainloop()
