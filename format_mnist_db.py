import pandas as pd


def charger_mnist_format_liste(fichier_csv):
    """
    Cette fonction lit un fichier CSV de données MNIST et retourne une liste d'images,
    où chaque image est une liste de 784 valeurs de pixels normalisées entre 0 et 1.

    :param fichier_csv: Chemin vers le fichier CSV contenant les données MNIST
    :return: Liste de listes de valeurs de pixels normalisées, chaque sous-liste contient 784 valeurs


    """
    # Charger le fichier CSV dans un DataFrame
    df = pd.read_csv(fichier_csv, header=None)

    # Récupérer les valeurs de pixels sans le label (première colonne) et normaliser entre 0 et 1
    images = (
        df.iloc[:, 1:] / 255
    ).values.tolist()  # Diviser chaque pixel par 255 pour normaliser
    label = (df.iloc[:, :1]).values.tolist()
    for i in range(len(label)):
        label[i] = from_label_to_number(label[i][0])
    return images, label


def from_label_to_number(chiffre):
    """
    Prend un chiffre entre 0 et 9 et retourne son encodage one-hot, c'est le nom de cette ecriture des nombres.

    :param chiffre: Un entier entre 0 et 9
    :return: Une liste représentant l'encodage one-hot du chiffre

    exemple:
    0: Résultat attendu: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    5: Résultat attendu: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    """
    if 0 <= chiffre <= 9:
        one_hot = [0] * 10
        one_hot[chiffre] = 1
        return one_hot
    else:
        raise ValueError("Le chiffre doit être entre 0 et 9")


# Exemple d'utilisation
