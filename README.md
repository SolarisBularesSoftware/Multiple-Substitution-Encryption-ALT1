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


# Comment sa fonctionne ?

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

# parametres

**carac_sub** sont les caractères que vous voulez substitués


# REQUIS
-------------------------------------
Pour copier le message automatiquement vous devez installez le module [pyperclip](https://pypi.org/project/pyperclip/)

	> pip install pyperclip
	
-------------------------------------


# Usage
---------------------------
	
	1) Chiffrer / Déchiffrer message
		-------------------------------------------->
		MSE.py c "message"
		MSE.py d


	2) Chiffrer vos clés
		---------------------->
		MSE.py cry
		MSE.py des PASSWORD


	3) Supprimer vos clés
		---------------------->
		MSE.py R
		
		
	4) Mélanger vos caractères spéciaux (a le faire tous de suite !)
		---------------------->
		MSE.py M


Tantez de casser l'algorithme avec le programme: [MARS ATTACK](https://discord.gg/E6qJmmKaEW)
