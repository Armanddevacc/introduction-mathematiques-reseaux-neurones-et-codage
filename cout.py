import reseau


def avr(L):
    av=0
    for e in L:
        av +=e

    return av/(len(L))


def fonction_cout(picture, biais,poid,nombre_neurone, label,Matrice_des_neurones):
    costs = []
    for j in range(len(picture)//8):
        cost=0
        sorti = (reseau.predire(picture[j], biais,poid,nombre_neurone))[-1]
        for i in range(len(sorti)):
            cost += (sorti[i] -label[j][i])**2
        costs.append(cost)
    return avr(costs)