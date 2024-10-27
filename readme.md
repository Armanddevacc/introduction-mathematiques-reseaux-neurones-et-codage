# Introduction mathématiques aux reseaux de neurones et codage d'un reseau simple

## Description du projet

Ce dossier a pour objectif de faire apprendre à ses lecteurs comment fonctionne un réseau de neurone classique. Nous passerons par la dimmension mathématiques et nous utiliserons python pour appliquer et visualiser ce que l'on a apprit. Pour comprendre le fonctionnement de réseaux de neuronnes (RN) nous fabriquerons un RN capable de reconnaitre des chiffres écrient à la main.


## Structure
---
![Cover](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/NN.png)
---
### On définit plusieurs termes:
- **un neurone est d'abord un réel compris entre 0 et 1**
- **les poids (weights notés w1 ...wn) qui sont associers à chaques arrêtes, ils appartiennent à R (les réels)**
- **les données d'entrées (x1 ... xk) sont les données qu'on fournit à notre RN, dans l'example de la reconnaisance de chiffre à partir d'une image en nuance de gris ils représentent un pixel et un chiffre entre 0 et 1 ou 0 est un pixel blanc et 1 un pixel noire**
- **on a ensuite des couches cachées (hidden layers), ces couches permettent de faire des calculs qu'on détaillera plus tard, notre RN aura 2 couches internes**
- **la couche de sortie (output layer) renvoie un nombre entre 0 et 1 pour chaque neurone, il y a autant de neurones à la sortie que de réponses envisagées. Dans notre exemple, notre RN aura 10 neurones dans sa couche de sortie**
- **La fonction sigmoïde ou fonction logistique est une fonction (appelé fonction d'ativation) qui va de R dans [0,1]**
![Cover](https://github.com/Armanddevacc/introduction-mathematiques-reseaux-neurones-et-codage/blob/main/image/fonction-sigmoide.png)
- **le biais est un réel qui permet d'éviter l'activation de certain neurones en dessous d'une certaines valeur**

### Interconection entre un neurone de la couche n+1 et tout les neurones de la couches n
La valeur d'un neurones de la couche n dépend entierement de neurones précedents, cette valeur est définie par la formule:
![Equation](https://latex.codecogs.com/png.latex?y%20%3D%20f%5Cleft%28%5Csum_%7Bi%3D1%7D%5En%20w_i%20x_i%20%2B%20b%5Cright%29)




