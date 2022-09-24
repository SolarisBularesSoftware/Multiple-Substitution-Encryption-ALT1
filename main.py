#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import choice
from pyperclip import paste

from MSE import mse_cipher,mse_decipher
from MSE import mse_cipher_file,mse_decipher_file,__doc__
from tools import rebuild,reinitialiser,mixer


exemple_phrases = ['salut agent','ceci est une longue phrase un peut chiante',
                   'meeting tonight for speak','rendez vous ce soir pour parler',
				   'hello world','on se voit ce soir','ou habitez vous',
				   'que faites vous','a bientot','a la semaine prochaine',
				   'je peux te parler','on peut se voir','jusqu ici tout va bien',
				   'mec tfk quoi la',
				   'alors la je fait expres de mettre une tres longue phrase pour des test',
				   'hallo zusammen heute','mec tfk quoi']


def demo():
	print('---------- * DEMO * ----------\n')
	print('Text chiffré:\n')
	message = mse_cipher(choice(exemple_phrases))
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message))



#mixer()
#rebuild()
#print(__doc__)

#mse_cipher_file('result.txt',exemple_phrases)
#mse_decipher_file('result.txt')

#reinitialiser()

"""
m = mse_cipher("bonjour tous le monde")
print(m)

print(mse_decipher(m))
"""
demo()







