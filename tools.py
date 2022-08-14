#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle,choice,randint
import shutil
from string import ascii_letters,digits,punctuation
import pyAesCrypt
from configs.parametre import name

def reinitialiser():
	"""
	Suprime vos clé de chiffrement !
	et le dossier __pycache__
	"""
	
	print('Vos clés de chiffrement vont être supprimés !')
	user = input('Etes-vous sur ? ')
		
	if user in ['y','yes','oui','o','da','Y','1']:
	
		if os.path.exists("keylib.keys"):
			os.remove("keylib.keys")
		shutil.rmtree('__pycache__')
		shutil.rmtree('configs/__pycache__')
		
		print('[ les clés de chiffrement ont été supprimés ]')


def gen_mdp():
	p = ""
	char = ascii_letters+digits+punctuation
	for c in range(randint(15,30)):
		p = p + choice(char)
	return p
	

def mixer():
	"""
	Mélange l'ordre des caractères
	example:
		AAAZZZ ---> | mixer(2) | ---> ZAAZAZ
	"""
	reinitialiser()
	
	init = open(name,'r',encoding='utf-8').readlines()
	init = "".join(init)
	init = list(init)

	shuffle(init)

	res = "".join(init)

	f = open(name,'w',encoding='utf-8')
	f.write(res)
	f.close()


def rebuild(filtre,name):
	"""
	reconstruit le fichier des caractères spéciaux
	en supriment les doublons et aussi les caractères
	indiqués dans filtre
	"""
	
	old_carac = open(name,'r',encoding='utf-8').read()
	new_carac = []
	
	for e in old_carac:
		if e not in filtre and e not in new_carac:
			if e != "\n":
				print('!')
				new_carac.append(e)
	
	new_carac = "".join(new_carac)
	
	open(name,'w',encoding='utf-8').write(new_carac)
	

