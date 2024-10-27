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

Pour vous entraînez vous pouvez créer un réseau de neurones en suivant toutes les définitions données. vous trouverez la base de donnée des écritures à la main des chiffres ici: https://git-disl.github.io/GTDLBench/datasets/mnist_datasets/ depuis j'ai moi même codé ce RN simple et non vraiment fonctionnel car on n'entraine pas ce réseau. Touver ce fichier dans reseau.py.



## 2.Comment choisir les valeurs de poids et de biais:

### Entraînement d'un réseau de neurones

### Introduction de la fonction Coût
Supposons que nous prenons des valeurs de biais et des poids aléatoires. Les résultats seront alors très confus comme on l'a vu en partie1. On introduit alors la fonction coût

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction-cout.png)

avec g la fonction qui donne la valeur de y_i à travers le réseau de nerones,  z_i nul sauf pour la valeur qu’on est censé obtenir à la fin. Dans l’exemple précedent si les données d’entrées correspondent à un 9 alors z_10 = 1 et les autres sont nulles. Ainsi plus la fonction coût est petite plus le reseau est bon. Evidemment pour exécuter cette fonction on est cencé avoir avoir les résultats attendus d'ou la nécésité de disposer de données d'entrainement. Pour information dans notre exemple la fonction prend en arguement 13.002 éléments.

Un autre indicateur est la moyenne sur toutes les données d'entrainement de cette fonction. On cherche bien evidemment à le diminuer

On comprend l'intérêt de trouver les valeurs qui minimisent ces indicateurs. Plus spéfiquement si le cout moyen est diminué alors l'ensemble du RN est optimisé. Vous pouvez implementez cette fonction coût en python vous aussi. Je l'ai fait dans cout.py

D'ailleurs cette fonction nous permet de comprendre l'entéret de l'encodage hot-one: cette encodage qui est très fréquence en RN permet à un nombre d'être traduit en vecteur: par exemple:
    0: Résultat attendu: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    5: Résultat attendu: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
Ainsi pour appelé la fonction cout il est plus pratique de lui fournir le résultat attendu dans ce format.

### Méthodes de minimisation: descente de gradiant

#### en 1D

Juste pour l'évoquer en 1D: On peut penser à dériver mais c'est pas toujours possible, on peut alors utiliser les méthodes d'euler ou de newton. On imagine bien que le cas 1D n'arrive pas.

#### en 2D et plus: La descente de gradiant

Pour ceux qui ne sont pas familier avec le concept de descente de gradient chez les fonctions à plusieurs vairables, on pourrait expliquer ça par la recherche en un point donné de la direction vers laquelle notre fonction va le plus décroite. Je va calculer ce gradient jusqu'à que la fonction cout moyen en dessous d'une certaine valeur (comme pour la méthode d'euler et newton nous n'arriverons pas à un 0 stricte). Ce gradient est calculé par la méthode de backpropagation qui est considéré comme le centre de l'apprentissage des RN. Ainsi quand on parle d'un RN qui apprend, on veut dire qu'il minimise sa fonction coût. 
La méthode de descente de gradiant permet de savoir quelles biais et poids doivent être augmentés ou baissés et à quelle force. Cette méthode nous donnera un vecteur colonne avec des valeurs positive ou négative et de même longueur que le nombre de biais et de poids.

prenons un exemple en 2D pour comprendre et visualiser/

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/expression_courbe.png)
![photo-d-une-courbe](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/courbe_dessin.png)

Ainsi calculons le gradiant de cette fonction

![Equation](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/gradiant_courbe.png
)

Ainsi calculons le gradiant de cette fonction en (1,1), on obtient alors le vecteur (2,2). Ce vecteur pointe alors vers l'endroit de la pente la plus raide, l'impacte est alors le même si on modifie (x,y) pareilement. Mais si on prend le point (1/2,1), on observe alors qu'il faut qu'on fasse une modification deux fois plus importe sur x que y pour arriver au même stade. On mets ici en exergue l'impacte différent de certains poid par rapport à d'autre. En outre certains point aurons plus d'etre modifier avec plus de force que d'autre.




### Backpropagation

#### explication:

















## on pourrait croire que les layers reperes les formes mais c'est faux





