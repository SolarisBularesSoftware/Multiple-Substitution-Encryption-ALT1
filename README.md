![image du projet](exemple/logo.png)


	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝


# MSE PROJECT
-------------------------------------

# MULTIPLE SUBSTITUTION ENCRYPTION
-------------------------------------
![cover](exemple/cover.jpg)


Chiffrement par substitution multiple

projet sur un programme de chiffrement par substitution multiple,
pour but de créer des messages codés avec des phrases courtes.


# Comment sa fonction ?

# I) chiffrement en 3 étapes:

    INPUT --> A --> B --> C --> output
    
--------------------------------------------------------------------------
    I) Bloc A
        Le texte est légèrement modifié.
--------------------------------------------------------------------------
    II) Bloc B
        Chaque caractère est substitué.
--------------------------------------------------------------------------
    II) Bloc C
        Ajoute des caractères dans le code après la substitution.



# REQUIS
-------------------------------------
Pour copier le message automatiquement vous devez installez le module [pyperclip](https://pypi.org/project/pyperclip/)

	> pip install pyperclip
	
[pyAesCrypt](https://pypi.org/project/pyAesCrypt/) pour chiffrer et envoyer vos clés de chiffrement

	> pip install pyAesCrypt

	
-------------------------------------


# Usage
---------------------------
	
	1) Chiffrer / Déchiffrer message
		-------------------------------------------->
		MSE.py c "message"
		MSE.py d


	2) Supprimer vos clés
		---------------------->
		MSE.py R
		
		
	3) Mélanger vos caractères spéciaux (a le faire tous de suite !)
		---------------------->
		MSE.py M


# Astuces
-------------------------------------------------------------------
modifier,mélanger vos caractères spéciaux

modifier les paramètres

Modifier la longueur des caractères.

optez plûtot pour un language de type "sms" du genre: tu fait quoi  ---> tfk

modifier la liste des "caractères spéciaux"

ajouter, modifier des fonctions



-----------------------------------
le monde merveilleux des secrets, des lettres et des
chiffres !
---------------------------------------

Tantez de casser l'algorithme avec le programme: [MARS ATTACK](https://discord.gg/E6qJmmKaEW)


