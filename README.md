#Introduction à la cryptographie (M1 S8)


Devoir maison réalisé par :
* BOUCHER Yohan
* JACQUIER Timéo


Langage utilisé : Python


##Configuration


Compilation du à la racine du projet : **python3 cryptographie.py**


###Question 1

_Quel langage de programmation avez-vous choisi ?_

Nous avons utilisé le langage Python pour réaliser l'entièreté du devoir maison.

_Quelle bibliothèque permettant de gérer des nombres entiers de grande taille allez-vous utiliser ? Quelles sont les oṕerations implémentées dans cette bibliothèque (multiplication, addition,...)_

En python, il n'est pas nécessaire d'utiliser une bibliothèque afin de générer des nombres entier de grande taille puisqu'en Python, il n'y a pas de limite de taille dans les nombres. 
En revanche, nous avons importer le module **sys** qui nous a permis de modifier le nombre maximal de récursion dans une même fonction et la taille maximum d'une chaîne de caractère pour l'enregister dans les fichiers .txt.

> sys.setrecursionlimit(2048)
> sys.set_int_max_str_digits(8192)

###Question 2

_En vous aidant d’internet, donnez la définition d’un nombre aléatoire cryptographiquement sûr._

**Nombre aléatoire cryptographiquement sûr** :

Un Nombre aléatoire cryptographiquement sûr est un générateur de nombre pseudo-aléatoire ayant des propriétés adaptées pour le domaine de la cryptographie. Il s'agit entre autre d'une fonction qui prend une valeur d'entrée appelé _graine_ et qui sort un nombre qui à lapparence d'un nombre généré aléatoirement.

Source : https://boowiki.info/art/les-generateurs-de-nombres-pseudo-aleatoires/generateur-de-nombres-pseudo-aleatoires-cryptographiquement-securise.html
https://openclassrooms.com/fr/courses/1757741-securisez-vos-donnees-avec-la-cryptographie/6031863-generez-des-nombres-aleatoires

En Python, le module **random** permet de générer ces nombres aléatoires.

###Question 3

Fonction **Euclide()** implémentée avec 10 000 test enregistrés dans le fichier **Euclid.txt

###Question 4

Fonction **ExpoMod()** implémentée avec 10 000 test enregistrés dans le fichier **ExpoMod.txt

###Question 5

Fonction **KeyGen()** implémentée avec 10 000 test enregistrés dans le fichier **KeyGen.txt

Fonction **Encrypt()** implémentée avec 10 000 test enregistrés dans le fichier **Encrypt.txt

Fonction **Decrypt()** implémentée avec 10 000 test enregistrés dans le fichier **Decrypt.txt

###Question 6

Fonction **Homomorphique()** implémentée avec 10 000 test enregistrés dans le fichier **Homomorphique.txt









