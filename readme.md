# Introduction mathématiques aux reseaux de neurones et codage d'un reseau simple

## Description du projet

Ce dossier a pour objectif de faire apprendre à ses lecteurs comment fonctionne un réseau de neurone classique. Nous passerons par la dimmension mathématiques et nous utiliserons python pour appliquer et visualiser ce que l'on a apprit. Pour comprendre le fonctionnement de réseaux de neuronnes (RN) nous fabriquerons un RN capable de reconnaitre des chiffres écrient à la main.


## Structure
---
![reseau-de-neurones](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/NN.png)
---
### On définit plusieurs termes:
- **un neurone est d'abord un réel compris entre 0 et 1**
- **les poids (weights notés w1 ...wn) qui sont associers à chaques arrêtes, ils appartiennent à R (les réels)**
- **les données d'entrées (x1 ... xk) sont les données qu'on fournit à notre RN, dans l'example de la reconnaisance de chiffre à partir d'une image en nuance de gris ils représentent un pixel et un chiffre entre 0 et 1 ou 0 est un pixel blanc et 1 un pixel noire**
- **on a ensuite des couches cachées (hidden layers), ces couches permettent de faire des calculs qu'on détaillera plus tard, notre RN aura 2 couches internes**
- **la couche de sortie (output layer) renvoie un nombre entre 0 et 1 pour chaque neurone, il y a autant de neurones à la sortie que de réponses envisagées. Dans notre exemple, notre RN aura 10 neurones dans sa couche de sortie**
- **La fonction sigmoïde ou fonction logistique est une fonction (appelé fonction d'ativation) qui va de R dans [0,1]**
![fonction](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction-sigmoide.png)
- **le biais est un réel qui permet d'éviter l'activation de certains neurones en dessous d'une certaines valeur (noté b1 ... bn). Ainsi le neurone s'ative si et seulement si(ssi) la somme(S définit ci-dessous) est supérieur à ce biais. D'ou la soustraction**
![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/somme.png)

### Interconection entre un neurone de la couche n+1 et tout les neurones de la couches n
La valeur d'un neurones de la couche n dépend entierement de neurones précedents, cette valeur est définie par la formule:
![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction-neurone.png)
f est ainsi la fonction d'activation (nous utilisererons la fonction sigmoïde) et les autres valeurs ont été introduit
### Écriture:
Il est très courant d'écrire un réseau de neurone avec les notations et indices introduit dans le premier graphique. On notera aussi:
![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/notation.png)
### deuxième définition du neurone 
On peut définir un nerone comme une fonction:
![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction_R^n.png)
celle-ci prendrait un arguement les valeurs des neurones de la couches précedentes.

### Conclusion partielle:

On a apprit la structure et comment les valeurs sont determinés des neurones sont determinés dans un réseau de neurones. Celles-ci dépendent des valeurs de poids et de biais mais si on prend ces valeurs, comment alors les choisir? C'est ce qu'on va aborder dans cette deuxième partie.

