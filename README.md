![image du projet](exemple/logo.png)


	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝


# MSE PROJECT
-------------------------------------

## MULTIPLE SUBSTITUTION ENCRYPTION
-------------------------------------
![cover](exemple/cover.jpg)


Chiffrement par substitution multiple

Projet sur un programme de chiffrement par substitution multiple,
pour but de créer des messages codés avec des phrases courtes.

**Nom de version: CRC X [ MELINGRADE ]**

## Comment sa fonction ?

### Chiffrement en 3 étapes:

    INPUT --> A --> B --> C --> output
    
    
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



## REQUIS
-------------------------------------
Pour copier le message automatiquement vous devez installez le module [pyperclip](https://pypi.org/project/pyperclip/)

	_> pip install pyperclip_


## Attention
-----------------------------------
**Ouvrir un fichier qui a pour extension _.carac_ peut entrainer un bug.**
**Lorsque vous chiffrer votre premier message un fichier _keylib.keys_ va être généré ce sont vous clés de chiffrement gardez les à tous prix !**


## Usage
---------------------------
Uasage:
	
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
	
	5) Paramètres aléatoires
		---------------------->
		main.py PA


## Astuces
-------------------------------------------------------------------
utilisez la commande **_main.py PA_** pour générer des paramètre aléatoire
modifier,mélanger vos caractères spéciaux
modifier les paramètres
Modifier la longueur des caractères.
optez plûtot pour un language de type "sms" du genre: tu fait quoi  ---> tfk
modifier la liste des "caractères spéciaux"
ajouter, modifier des fonctions

**_la version que vous avez téléchargée ne dois pas ressembler au code source officielle_**

-----------------------------------
le monde merveilleux des secrets, des lettres et des
chiffres !
---------------------------------------

Tentez de casser l'algorithme avec le programme: [MARS ATTACK](https://discord.gg/E6qJmmKaEW)

