![image du projet](exemple/logo.png)

# MSE PROJECT
-------------------------------------

## MULTIPLE SUBSTITUTION ENCRYPTION
-------------------------------------

Chiffrement par substitution multiple

Programme de chiffrement de text par substitution multiple,
pour but de créer des messages codés avec des phrases.


**Nom de version: CRC X [ MELINGRADE ]**

## Comment sa fonctionne ?

### Chiffrement en 3 étapes:

### INPUT --> A --> B --> C --> output
    
    
    0) Initiation
        génération des clés de chiffrement
--------------------------------------------------------------------------
	
    I) Bloc A
        Le texte est modifié.
--------------------------------------------------------------------------
    II) Bloc B
        Une clé est choisie au hasard.
        Chaque caractère est substitué avec cette clé.
--------------------------------------------------------------------------
    II) Bloc C
        Ajoute des caractères dans le code après la substitution.


## Exemple
![Exemple](exemple/exemple.jpg)
En bleu vous avez les caractères qui ont été substitués et en rouge les caractères qui ont été ajoutés **après** la substitution.


## d'autre exemples
![Exemple](exemple/ex2.PNG)
![Exemple](exemple/ex3.PNG)
![Exemple](exemple/ex4.PNG)


## Exemple de clé de chiffrement
![Exemple](exemple/ex_keys.PNG)


## REQUIS
-------------------------------------
Pour copier le message automatiquement vous devez installez le module [pyperclip](https://pypi.org/project/pyperclip/)

	pip install pyperclip


## Attention
-----------------------------------
**Lorsque vous chiffrer votre premier message un fichier _keylib.keys_ va être généré ce sont vous clés de chiffrement gardez les à tous prix !**

## Usage
---------------------------
Usage:
	
	1) Chiffrer et déchiffrer un message
		-------------------------------------------->
		main.py c "message"
		main.py d (déchiffre un message qui est dans le presse papier)

	2) Supprimer les clés
		---------------------->
		main.py R
		
	3) Mélanger les caractères spéciaux
		---------------------->
		main.py M
	
	4) Reconstruit le fichier de caractères spéciaux actuelle
		---------------------->
		main.py RE


## Conseille et Astuces
-------------------------------------------------------------------
modifier,mélanger vos caractères spéciaux

modifier les paramètres du programme dans configs/setting.json

optez plûtot pour un language de type "sms" du genre: tu fait quoi  ---> tfk

modifier la liste des "caractères spéciaux"

ajouter, modifier des fonctions


**_la version que vous avez téléchargée ne dois pas ressembler au code source officielle_**


## Ressources
-------------------------------------------------------------------


Tentez de casser l'algorithme avec le programme: [MARS ATTACK](https://discord.gg/E6qJmmKaEW)

Exemple visuelle de message codé: [result.vu](https://zpuf06s8huajolm3byvojg.on.drv.tw/public_html/MSE%20VISUAL%20CODE/)

mon twitter: [twitter](https://twitter.com/motionkerling)

le monde merveilleux des secrets, des lettres et des chiffres !
