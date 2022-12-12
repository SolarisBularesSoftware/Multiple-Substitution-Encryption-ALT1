#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from string import ascii_lowercase,ascii_uppercase, ascii_letters, digits, punctuation
import json
import os.path

accent = 'ÄÀÂÉÈÊËÎÏÔÙÛÜÇàâéèêëîïôùûüç'

nom_fichier_parametre = "configs/setting.json"

if os.path.exists(nom_fichier_parametre) is False:
	raise Exception(f'Erreur --> Fichier {nom_fichier_parametre} introuvable')

file = open(nom_fichier_parametre, 'r')
data = json.load(file)
file.close()

carac_sub = data['cipher']

# 3 options: ascii_lowercase, ascii_uppercase, ascii_letters

if data['cipher'] == 'ascii_lowercase':
	carac_sub = ascii_lowercase
elif data['cipher'] == 'ascii_uppercase':
	carac_sub = ascii_uppercase
elif data['cipher'] == 'ascii_letters':
	carac_sub = ascii_letters
else:
	raise Exception('[ Erreur --> setting.json: Option incconue ]')


if data["cipher punctuation"] == True:
	carac_sub = carac_sub+ punctuation
if data["cipher space"] == True:
	carac_sub = carac_sub+ ' '
if data["cipher digits"] == True:
	carac_sub = carac_sub+ digits
if data["cipher accent"] == True:
	carac_sub = carac_sub+ accent

len_carac_sub = len(carac_sub)

fichier_jeux_carac = data['substitue with']

if os.path.exists(fichier_jeux_carac) is False:
	raise Exception('Erreur --> Fichier de jeux de caractères introuvable')


len_caractere = data['len_caractere']
longeur_carac_special = data['len_carac_special']
nombre_cle = data['nombre_cle']
mini,maxi = data['mini'],data['maxi']


groupe_caracteres_initial = "".join(open(fichier_jeux_carac,'r',encoding='utf-8').readlines())
milieu = int(len(groupe_caracteres_initial)/2)
groupe_a = groupe_caracteres_initial[:milieu]
groupe_b = groupe_caracteres_initial[milieu:]

carac_special = 'esantirulodcpxwv '

if data['confusion'] == True:
	groupe_b = groupe_b+carac_sub*randint(5,100)+carac_special*randint(5,50)




