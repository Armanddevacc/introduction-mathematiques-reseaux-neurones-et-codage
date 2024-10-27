"""

partie1:


Ce code initialisera correctement le réseau avec des biais et des poids aléatoires, calculera la sortie pour chaque couche, et renverra la sortie finale du réseau.

"""

## importation
from math import *
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import format_mnist_db 





def fonction_sigmoid(x): #fonction sigmoide comme introduite
    return (1/(1+exp(-x)))


def affichage_fonction():
    x_values = np.linspace(-50, 50, 400)    # Générer les valeurs de x de -10 à 10
    y_values = [fonction_sigmoid(x) for x in x_values]  # Calculer les valeurs de y en utilisant la fonction sigmoïde

    # Affichage de la fonction
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="Fonction Sigmoïde")
    plt.title("Fonction Sigmoïde")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()



def fonction_neurone(i,j): 
    """
    parametre:
    L: matrice des valeurs de tout les neurones
    i+1: numéro de la couche: 3 couche de sortie
    j: indice du neurone dans sa couche
    """
    S=0
    biais_ = biais[i-1][j]
    for k in range(len(Matrice_des_neurones[i-1])):
        S += (poid[i-1][j][k])*Matrice_des_neurones[i-1][k] #i-1-ème couche, j-ème neurone de la couche i, k-ième poid du neurone j
    S+= -biais_
    a = fonction_sigmoid(S + biais_)
    return a


def tester_reseau():
    """
    on parcourt et remplit simplement notre Matrice_des_neurones
    """
    for i in range(1,len(Matrice_des_neurones)):
        for j in range(len(Matrice_des_neurones[i])):
            a_i_j =fonction_neurone(i,j)
            Matrice_des_neurones[i][j]=a_i_j
    return Matrice_des_neurones[-1]








##initialisation
# Exemple d'utilisation
fichier = "database/mnist_train.csv"  # Remplace par le chemin de ton fichier
picture = format_mnist_db.charger_mnist_format_liste(fichier)[0]#liste de 784 valeurs qui definisent l'image de 28*28 qui represente un nombre
print(picture)
nombre_layer=2 # nombre de couche 
nombre_neurone = [0 for _ in range(nombre_layer+2)] #disons 16 neurones par couches mais c'est comment vous voulez
nombre_neurone[0]=784
nombre_neurone[1]=16
nombre_neurone[2]=16
nombre_neurone[3]=10

biais= [] # on les définit aléatoirement:
biais.append([rd.randint(0, 5) for _ in range(16)])
biais.append([rd.randint(0, 5) for _ in range(16)])
biais.append([rd.randint(0, 5) for _ in range(10)])

poid = [] # de même
poid.append([[rd.randint(-1, 1) for _ in range(784)] for _ in range(16)])
poid.append([[rd.randint(-1, 1) for _ in range(16)] for _ in range(16)])
poid.append([[rd.randint(-1, 1) for _ in range(16)] for _ in range(10)])

couche_sortie = [0 for _ in range(10)]
Matrice_des_neurones = [[0 for _ in range(nombre_neurone[i])] for i in range(len(nombre_neurone))] # ce n'est pas vraiment une matrice en vrai
Matrice_des_neurones[0]= picture





if __name__ == '__main__':
    print(tester_reseau())