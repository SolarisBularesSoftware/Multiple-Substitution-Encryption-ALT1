#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

I) Je choisit un groupe de caractère que je veut substituer

II) Je choisit un groupe de caractères spéciaux

III) Je divise le groupe en deux groupes:
	groupe A pour générer mes clés de chiffrement
	groupe B pour ajouter des caractères après la substitution

IV) Je définie mes carcatères spéciaux
	ces caractères auront un groupe de carcatère d'une longeur plus petit

---------------------------------------------------------------------------
faite votre propre version et le montrer à personne !
Regénèrer vos clés de chiffrement si vous modifier ce fichier !!

"""

from string import ascii_lowercase
from random import shuffle
import os

carac_sub = list(ascii_lowercase+' ')
len_carac_sub = len(carac_sub)

name = "configs/all.carac"

groupe_caracteres_initial = "".join(open(name,'r',encoding='utf-8').readlines())

milieu = int(len(groupe_caracteres_initial)/2)

groupe_a = groupe_caracteres_initial[:milieu]
groupe_b = groupe_caracteres_initial[milieu:]


carac_special = 'esuwfdntzcapv '

# Cette ligne est purement esthétique
groupe_b = groupe_b+''.join(carac_sub)*50+carac_special*50

len_caractere = (5,7)
longeur_carac_special = (2,4)

nombre_cle = (10,30)

mini,maxi = 100,300
