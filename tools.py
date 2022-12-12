#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle,choice,randint
import shutil
from configs.init import fichier_jeux_carac,carac_sub
from configs.generateur_parametre import creat_


def reinitialiser():
	"""
	Supprime vos clés de chiffrement !
	"""
	
	if os.path.exists("keylib.keys"):
		os.remove("keylib.keys")
		
	try:
		shutil.rmtree('__pycache__')
		shutil.rmtree('configs/__pycache__')
	except FileNotFoundError:
		pass


def mixer():
	"""
	Mélange l'ordre des caractères
	exemple:
		AAAZZZ ---> | mixer | ---> ZAAZAZ
	"""
	reinitialiser()
	
	old_data = list(open(fichier_jeux_carac,'r',encoding='utf-8').read())

	shuffle(old_data)

	new_data = "".join(old_data)

	new_file = open(fichier_jeux_carac,'w',encoding='utf-8').write(new_data)


def rebuild():
	"""
	reconstruit le fichier des caractères spéciaux
	en supriment les doublons et aussi les caractères
	indiqués dans carac_sub
	"""
	reinitialiser()
	
	old_carac = open(fichier_jeux_carac,'r',encoding='utf-8').read()
	new_carac = []
	
	for c in old_carac:
		if c not in carac_sub and c not in new_carac:
			if c != "\n":
				new_carac.append(c)
	
	new_carac = "".join(new_carac)
	
	open(fichier_jeux_carac,'w',encoding='utf-8').write(new_carac)
	

def gen_version():
	"""
		Génère une autre version du programme
	"""
	generer_para()
	mixer()


def first_mixer():
	"""
	Mélange l'ordre des caractères, si
	l'utilisateur utilise pour la première fois
	le programme
	"""

	if not os.path.exists("user.data"):
		mixer()
		open("user.data","w").close()

first_mixer()

