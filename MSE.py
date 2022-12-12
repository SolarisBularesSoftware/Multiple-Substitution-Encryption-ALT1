#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Copyright 2019-2022 by Motion Kerling. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Motion Kerling
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# Motion Kerling DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# Motion Kerling BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝
	
	MSE (multiple substitution encryption)

	Créer le mardi 22 janvier 2019 à 01:10 

"""

__author__  = "SSB"
__version__ = "1.0.0"
__date__    = "12 decembre 2022"

from random import randint,choice
from pyperclip import copy

from bloc_a import complexifier,complexifier_inv
from bloc_b import cipher,decipher
from bloc_c import ajout_carac_b,enleve_carac_b

from configs.init import*


def mse_cipher(msg):
	"""
	|A| --> |B| --> |C|
	"""
	a  = complexifier(msg)
	b = cipher(a)
	c = ajout_carac_b(b,randint(mini,maxi))
	ca = ajout_carac_b(c,randint(mini,maxi))
	cb = ajout_carac_b(ca,randint(mini,maxi))
	
	copy(cb)
	return cb


def mse_decipher(msg):
	"""
	|C| --> |B| --> |A|
	"""
	c = enleve_carac_b(msg)
	b = decipher(c)
	a = complexifier_inv(b)
	
	return a


def mse_cipher_file(filename,list):

	file = open(filename,'w',encoding="utf-8")

	for e in list:
		file.write(mse_cipher(e))
		file.write('\n\n')

	file.close()


def mse_decipher_file(filename):

	file = open(filename,'r',encoding="utf-8").read()

	file = file.split('\n\n')

	for line in file:
		print(mse_decipher(line))


def gen_false_positive():
	x = randint(100,900)

	s = ""

	for e in range(x):
		s = s + choice(groupe_c)

	copy(s)

