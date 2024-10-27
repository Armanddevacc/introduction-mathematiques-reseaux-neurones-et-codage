# Introduction mathématique aux reseaux de neurones et codage d'un reseau simple

## Description du projet

Ce dossier a pour objectif de d'apprendre à ses lecteurs comment fonctionne un réseau de neurones classique. Nous passerons par la dimension mathématiques et nous utiliserons python pour appliquer et visualiser ce que l'on a appris. Pour comprendre le fonctionnement de réseaux de neurones (RN) nous fabriquerons un RN capable de reconnaître des chiffres écrits à la main.


## 1.Structure
---
![reseau-de-neurones](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/NN.png)
---
### On définit plusieurs termes:
- **un neurone est d'abord un réel compris entre 0 et 1**
- **les poids (weights notés w1 ...wn) qui sont associers à chaque arêtes, ils appartiennent à R (les réels)**
- **les données d'entrée (x1 ... xk) sont les données qu'on fournit à notre RN, dans l'exemple de la reconnaisance de chiffre à partir d'une image en nuance de gris ils représentent un pixel et un chiffre entre 0 et 1 ou 0 est un pixel blanc et 1 un pixel noir**
- **Nous avons ensuite des couches cachées (hidden layers), ces couches permettent de faire des calculs qu'on détaillera plus tard, notre RN aura 2 couches internes**
- **la couche de sortie (output layer) renvoie un nombre entre 0 et 1 pour chaque neurone, il y a autant de neurones à la sortie que de réponses envisagées. Dans notre exemple, notre RN aura 10 neurones dans sa couche de sortie**
- **La fonction sigmoïde ou fonction logistique est une fonction (appelée fonction d'ativation) qui va de R dans [0,1]**
![fonction](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction-sigmoide.png)
- **le biais est un réel qui permet d'éviter l'activation de certains neurones en dessous d'une certaine valeur (noté b1 ... bn). Ainsi le neurone s'active si et seulement si (ssi) la somme(S définit ci-dessous) est supérieur à ce biais. D'ou la soustraction**

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/somme.png)

### Interconnection entre un neurone de la couche n+1 et tout les neurones de la couche n
La valeur d'un neurones de la couche n dépend entièrement de neurones précédents, cette valeur est définie par la formule:

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction-neurone.png)
f est ainsi la fonction d'activation (nous utiliserons la fonction sigmoïde) et les autres valeurs ont été introduites.
### Écriture:
Il est très courant d'écrire un réseau de neurones avec les notations et indices introduits dans le premier graphique. On notera aussi:

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/notation.png)
### deuxième définition du neurone 
On peut définir un neurone comme une fonction:

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction_R^n.png)

celle-ci prendrait en arguements les valeurs des neurones de la couches précedentes.

### Conclusion partielle:

On a appris la structure et comment les valeurs des neurones sont determinées dans un réseau de neurones. Celles-ci dépendent des valeurs de poids et de biais mais si on prend ces valeurs, comment alors les choisir? C'est ce qu'on va aborder dans cette deuxième partie.

### Teste et exercice

Pour vous entraînez vous pouvez créer un réseau de neurones en suivant toutes les définitions données. vous trouverez la base de donnée des écritures à la main des chiffres ici: https://git-disl.github.io/GTDLBench/datasets/mnist_datasets/ depuis j'ai moi même codé ce réseau de neurones simple et non vraiment fonctionnel car on n'entraine pas ce réseau. Touver ce fichier dans reseau.py.



## 2.Comment choisir les valeurs de poids et de biais:

### Entraînement d'un réseau de neurones

### Introduction de la fonction Coût
Supposons que nous prenons des valeurs de biais et des poids aléatoires. Les résultats seront alors très confus comme on l'a vu en partie1. On introduit alors la fonction coût

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction_cout.png)

avec g la fonction qui donne la valeur de y_i à travers le réseau de nerones,  z_i nul sauf pour la valeur qu’on est censé obtenir à la fin. Dans l’exemple précedent si les données d’entrées correspondent à un 9 alors z_10 = 1 et les autres sont nulles. Ainsi plus la fonction coût est petite plus le reseau est bon. Evidemment pour exécuter cette fonction on est cencé avoir avoir les résultats attendus d'ou la nécésité de disposer de données d'entrainement. Pour information dans notre exemple la fonction prend en arguement 13.002 éléments.

Un autre indicateur est la moyenne sur toutes les données d'entrainement de cette fonction. On cherche bien evidemment à le diminuer

On comprend l'intérêt de trouver les valeurs qui minimisent ces indicateurs.

### Méthode de minimisation: descente de gradiant

#### en 1D

Juste pour l'évoquer en 1D: On peut penser à dériver mais c'est pas toujours possible, on peut alors utiliser les méthodes d'euler ou de newton. On imagine bien que le cas 1D n'arrive pas.

#### en 2D et plus

