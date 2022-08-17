#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import choice, randint
from string import ascii_lowercase

ress_bin = ['all.carac','asian.carac','lang.carac','emoji.carac','rand_carac.carac']


def gen_random_setting():
	f = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_lowercase

espace = " "
carac_sub = list(ascii_lowercase+espace)
len_carac_sub = len(carac_sub)

name = "configs/A"

groupe_caracteres_initial = "".join(open(name,'r',encoding='utf-8').readlines())

milieu = int(len(groupe_caracteres_initial)/2)

groupe_a = groupe_caracteres_initial[:milieu]
groupe_b = groupe_caracteres_initial[milieu:]

carac_special = 'B'

C groupe_b = groupe_b+''.join(carac_sub)*50+carac_special*50

len_caractere = (D1,D2)
longeur_carac_special = (E1,E2)
nombre_cle = (F1,F2)
mini,maxi = G1,G2"""

	f = f.replace('A',choice(ress_bin))
	
	x = 'esd '
	
	for e in range(10):
		c = choice(ascii_lowercase)
		if c not in x:
			x =x+c
	
	f = f.replace('B',x)
	
	if choice([0,1]) == 1:
		f = f.replace('C ','')
	else:
		f = f.replace('C ','#')
	
	f = f.replace('D1',str(randint(4,10)))
	f = f.replace('D2',str(randint(11,20)))
	
	f = f.replace('E1',str(randint(2,4)))
	f = f.replace('E2',str(randint(5,9)))
	
	f = f.replace('F1',str(randint(3,10)))
	f = f.replace('F2',str(randint(11,50)))
	
	f = f.replace('G1',str(randint(100,300)))
	f = f.replace('G2',str(randint(399,700)))
	
	open('parametre.py','w').write(f)

