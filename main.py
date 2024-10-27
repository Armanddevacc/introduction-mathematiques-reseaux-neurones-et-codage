import format_mnist_db
import cout
import random as rd



##initialisation
# Exemple d'utilisation
fichier = "database/mnist_train.csv"  # Remplace par le chemin de ton fichier
picture,label = format_mnist_db.charger_mnist_format_liste(fichier)#liste de 784 valeurs qui definisent l'image de 28*28 qui represente un nombre



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





if __name__ == '__main__':

    print(cout.fonction_cout(picture, biais, poid,nombre_neurone, label))