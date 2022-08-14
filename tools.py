#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle,choice,randint
import shutil
from string import ascii_letters,digits,punctuation
import pyAesCrypt
from configs.parametre import name,carac_sub

def reinitialiser():
	"""
	Suprime vos clé de chiffrement !
	et le dossier __pycache__
	"""
	
	reponse = input('Etes-vous sur ? ')
		
	if reponse in ['y','yes','oui','o','da','Y','1','True','true']:
	
		if os.path.exists("keylib.keys"):
			os.remove("keylib.keys")
		shutil.rmtree('__pycache__')
		shutil.rmtree('configs/__pycache__')


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


def rebuild():
	"""
	reconstruit le fichier des caractères spéciaux
	en supriment les doublons et aussi les caractères
	indiqués dans filtre
	"""
	reinitialiser()
	
	old_carac = open(name,'r',encoding='utf-8').read()
	new_carac = []
	
	for e in old_carac:
		if e not in carac_sub and e not in new_carac:
			if e != "\n":
				new_carac.append(e)
	
	new_carac = "".join(new_carac)
	
	open(name,'w',encoding='utf-8').write(new_carac)
	




