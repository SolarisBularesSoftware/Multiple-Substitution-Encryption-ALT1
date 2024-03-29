#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	I) Bloc A
		Serie d'opération sur une chaine de caractère
		servant à modifier le text entré.
"""

from subdiv_mini import inverser_phrase,remettre_phrase

def complexifier(plain_text):
	"""
		example:
			hello word ---> rowdl lehol
	"""

	plain_text =  plain_text[::-1]
	plain_text = inverser_phrase(plain_text)

	return plain_text


def complexifier_inv(coded_text):
	""" 
		Remet le text dans le bon sens
		example:
			rowdl lehol ---> hello world
	"""

	coded_text = remettre_phrase(coded_text)
	coded_text =  coded_text[::-1]

	return coded_text




