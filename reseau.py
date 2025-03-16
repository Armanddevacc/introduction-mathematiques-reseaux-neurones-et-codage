"""

partie1:


Ce code initialisera correctement le réseau avec des biais et des poids aléatoires, calculera la sortie pour chaque couche, et renverra la sortie finale du réseau.

"""

## importation
from math import *
import matplotlib.pyplot as plt
import numpy as np


def fonction_sigmoid(x):  # fonction sigmoide comme introduite
    return 1 / (1 + exp(-x))


def affichage_fonction():
    x_values = np.linspace(-50, 50, 400)  # Générer les valeurs de x de -10 à 10
    y_values = [
        fonction_sigmoid(x) for x in x_values
    ]  # Calculer les valeurs de y en utilisant la fonction sigmoïde

    # Affichage de la fonction
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="Fonction Sigmoïde")
    plt.title("Fonction Sigmoïde")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()


def fonction_neurone(i, j, biais, poid, Matrice_des_neurones):
    """
    parametre:
    L: matrice des valeurs de tout les neurones
    i+1: numéro de la couche: 3 couche de sortie
    j: indice du neurone dans sa couche
    """
    S = 0
    biais_ = biais[i - 1][j]
    for k in range(len(Matrice_des_neurones[i - 1])):
        S += (poid[i - 1][j][k]) * Matrice_des_neurones[i - 1][
            k
        ]  # i-1-ème couche, j-ème neurone de la couche i, k-ième poid du neurone j
    S += -biais_
    a = fonction_sigmoid(S + biais_)
    return a


def predire(picture, biais, poid, nombre_neurone, Matrice_des_neurones):
    """
    on parcourt et remplit simplement notre Matrice_des_neurones
    """

    for i in range(1, len(Matrice_des_neurones)):
        for j in range(len(Matrice_des_neurones[i])):
            a_i_j = fonction_neurone(i, j, biais, poid, Matrice_des_neurones)
            Matrice_des_neurones[i][j] = a_i_j
    return Matrice_des_neurones


def fonction_derive_sigmoid(x):  # fonction sigmoide comme introduite
    return exp(-x) / (1 + exp(-x))


def z_i(poids_i_L: list, a_L_1: list, b_i_L: int):  # renvoie z_i comme introduit
    z = 0
    for j in range(len(poids_i_L)):
        z += poids_i_L[j] * a_L_1[j]
    z += b_i_L
    return z


def fonction_derive_C_w(i, j, L, poids, biais, matrice_neurone, labels):
    """
    i numéro du neurone d'arrivé
    j numéro du neurone de depart
    L numéro de layer
    """
    a_i_L_1 = matrice_neurone[L - 2][j]
    poids_i_L = poids[L - 1][i]
    a_L_1 = matrice_neurone[L - 2][j]
    b_i_L = biais[L - 1][i]
    return (
        fonction_derive_C_a(i, L, matrice_neurone, labels, poids)
        * a_i_L_1
        * fonction_derive_sigmoid(z_i(poids_i_L, a_L_1, b_i_L))
    )


def fonction_derive_C_b(i, L, poids, biais, matrice_neurone, labels):
    """
    i numéro du neurone d'arrivé
    j numéro du neurone de depart
    L numéro de layer
    """
    poids_i_L = poids[L - 1][i]
    a_L_1 = matrice_neurone[L - 2][i]
    b_i_L = biais[L - 1][i]
    return fonction_derive_C_a(
        i, L, matrice_neurone, labels, poids
    ) * fonction_derive_sigmoid(z_i(poids_i_L, a_L_1, b_i_L))


def fonction_derive_z_i_L_a_k_L_1(poid, k, j, L):

    return poid[L][j][k]


def fonction_derive_C_a(i, L, matrice_neurone, label, poid):
    """
    i numéro du neurone d'arrivé
    j numéro du neurone de depart
    L numéro de layer
    """
    if L == 3:
        a_i_L = matrice_neurone[L - 1][i]
        y_i = label[i]
        return 2 * (a_i_L - y_i)
    else:
        S = 0
        for j in range(len(matrice_neurone[L])):
            S += (
                fonction_derive_C_a(i, L + 1, matrice_neurone, label, poid)
                * fonction_derive_z_i_L_a_k_L_1(poid, i, j, L)
                * fonction_derive_sigmoid(
                    z_i(poid[L][i], matrice_neurone[L - 1], label[L][i])
                )
            )
        return S


def calcul_nouveau_gradient(poids, biais, matrice_neurone, label):

    for L in range(1, len(poids) + 1):
        for i in range(len(poids[L])):
            biais[L][i] += fonction_derive_C_b(
                i, L, poids, biais, matrice_neurone, label
            )
            for j in range(len(poids[L][i])):
                poids[L][i][j] += fonction_derive_C_w(
                    i, j, L, poids, biais, matrice_neurone, label
                )
    return poids, biais
