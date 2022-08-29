from tools import rebuild,reinitialiser,mixer
from random import choice
from MSE import mse_cipher,mse_decipher,__doc__
#import sys
from pyperclip import paste

exemple_phrases = ['Salut agent 789 !','ceci est une longue phrase un peut chiante','meeting tonight for speak','rendez vous ce soir pour parler','hello world','on se voit ce soir','ou habitez vous','que faites vous','a bientot','a la semaine prochaine','je peux te parler','on peut se voir','jusqu ici tout va bien','mec tfk quoi la','alors la je fait expres de mettre une tres longue phrase pour des test','hallo zusammen heute','mec tfk quoi']

def demo():
	print('---------- * DEMO * ----------\n')
	print('Text chiffré:\n')
	message = mse_cipher(choice(example_phrases))
	print(message,'\n\n')

	print('Texte déchiffré:\n')
	print(mse_decipher(message))

"""

NOT WORK
----------
provoque un bug qui va être corriger lors d'une mise
à jour futur.

def main():

	cip = ['cipher','c','C','cip']
	dec = ['decipher','d','D','dec']
	
	mxr = ['M','m','mixer','mix','mxr']
	reset = ['r','R','reset','delete','del']
	rebld = ['re','RE','reb','rebuild']
	h = ['H','h','Help me','help me','aide moi','A','a']
	
	_all_ = cip+dec+reset+mxr+rebld+h

	if sys.argv[1] not in _all_:
		if sys.argv[1] == "demo":
			demo()
		else:
			print('commande invalide')
		
	elif sys.argv[1] in cip:
		print(mse_cipher(sys.argv[2]))
		
	elif sys.argv[1] in dec:
		print(mse_decipher(paste()))
	
	elif sys.argv[1] in reset:
		reinitialiser()
	
	elif sys.argv[1] in mxr:
		mixer()
		
	elif sys.argv[1] in rebld:
		rebuild()
	
	elif sys.argv[1] in h:
		print(__doc__)

"""


#demo()
#reinitialiser()
#mixer()
#rebuild()
#print(__doc__)


m = mse_cipher("Salut agent 789 !")
print(m)
print(mse_decipher(m))

