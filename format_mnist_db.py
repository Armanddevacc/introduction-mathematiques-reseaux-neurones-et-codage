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
    images = (df.iloc[:, 1:] / 255).values.tolist()  # Diviser chaque pixel par 255 pour normaliser
    
    return images