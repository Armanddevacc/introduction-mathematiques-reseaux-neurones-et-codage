"""

partie1:


Ce code initialisera correctement le réseau avec des biais et des poids aléatoires, calculera la sortie pour chaque couche, et renverra la sortie finale du réseau.

"""

## importation
from math import *
import matplotlib.pyplot as plt
import numpy as np





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



def fonction_neurone(i,j, biais,poid,Matrice_des_neurones): 
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


def predire(picture, biais, poid,nombre_neurone):
    """
    on parcourt et remplit simplement notre Matrice_des_neurones
    """
    Matrice_des_neurones = [[0 for _ in range(nombre_neurone[i])] for i in range(len(nombre_neurone))] # ce n'est pas vraiment une matrice en vrai

    Matrice_des_neurones[0]= picture

    for i in range(1,len(Matrice_des_neurones)):
        for j in range(len(Matrice_des_neurones[i])):
            a_i_j =fonction_neurone(i,j, biais, poid,Matrice_des_neurones)
            Matrice_des_neurones[i][j]=a_i_j
    return Matrice_des_neurones[-1]






