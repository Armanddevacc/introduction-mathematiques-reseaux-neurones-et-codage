import format_mnist_db
import cout
import random as rd


import reseau

##initialisation
# Exemple d'utilisation
fichier = "database/mnist_train.csv"  # Remplace par le chemin de ton fichier
picture, label = format_mnist_db.charger_mnist_format_liste(
    fichier
)  # liste de 784 valeurs qui definisent l'image de 28*28 qui represente un nombre


nombre_layer = 2  # nombre de couche
nombre_neurone = [
    0 for _ in range(nombre_layer + 2)
]  # disons 16 neurones par couches mais c'est comment vous voulez
nombre_neurone[0] = 784
nombre_neurone[1] = 16
nombre_neurone[2] = 16
nombre_neurone[3] = 10

biais = []  # on les définit aléatoirement:
biais.append([rd.randint(0, 5) for _ in range(16)])
biais.append([rd.randint(0, 5) for _ in range(16)])
biais.append([rd.randint(0, 5) for _ in range(10)])

poids = []  # de même
poids.append([[rd.randint(-1, 1) for _ in range(784)] for _ in range(16)])
poids.append([[rd.randint(-1, 1) for _ in range(16)] for _ in range(16)])
poids.append([[rd.randint(-1, 1) for _ in range(16)] for _ in range(10)])

couche_sortie = [0 for _ in range(10)]


if __name__ == "__main__":
    Matrice_des_neurones = [
        [0 for _ in range(nombre_neurone[i])] for i in range(len(nombre_neurone))
    ]  # ce n'est pas vraiment une matrice en vrai
    Matrice_des_neurones[0] = picture
    Matrice_des_neurones = reseau.predire(
        picture, biais, poids, nombre_neurone, Matrice_des_neurones
    )
    for i in range(1, len(picture), 10):
        Matrice_des_neurones = reseau.predire(
            picture[i : i + 100], biais, poids, nombre_neurone, Matrice_des_neurones
        )
        print(
            cout.fonction_cout(
                picture[i : i + 100],
                biais,
                poids,
                nombre_neurone,
                label,
                Matrice_des_neurones,
            )
        )

        for _ in range(10):
            biais, poids = reseau.calcul_nouveau_gradient(
                poids, biais, Matrice_des_neurones, label
            )
