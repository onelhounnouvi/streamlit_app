import numpy as np
import random
import math
import time
from fonct_aff import *

#Fonction permettant de créer un monde représenter par une matrice 
def monde(taille): 
    MONDE = []
    tab = []
    for i in range(taille):
        for j in range(taille): 
            tab.append('S')
        MONDE.append(tab)
        tab = []
    return MONDE 

#Fonction permettant de placer un nbre d'infectés aléatoirement dans le monde 
def point_de_depart(monde, taille, nb_infectes): 
    for i in range(nb_infectes):
        x = random.choice(range(taille))
        y = random.choice(range(taille))
        while (monde[x][y] == 'I'):
            x = random.choice(range(taille))
            y = random.choice(range(taille))
        monde[x][y] = 'I'

#Fonction permettant de créer une liste des voisins
def neighborhood(cells,x,y,neigh): 
    V = []
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if (i,j) != (x,y) and (max(abs(x-i),abs(y-j)) <= neigh):
                V.append((i,j))
    return V

#Fonction permettant d'infecter le voisinage d'un individu infecté
def propagation1(monde,x,y,p_infection): 
    if(monde[x][y]=='I'):
        voisinage = neighborhood(monde,x,y,1)
        nb_a_inf = math.floor(p_infection*len(voisinage))
        pers_a_inf = random.sample(voisinage, nb_a_inf)
        for (i,j) in pers_a_inf:
            if (monde[i][j] == 'S'):
                monde[i][j] = 'I'
               
#Fontion propagation1 a l'échelle de toute la matrice 
def propagation2(monde,taille,p_infection):
    monde_cp = [ligne[:] for ligne in monde]
    for i in range(taille):
        for j in range (taille):
            if (monde_cp[i][j] == 'I'):
                propagation1(monde,i,j,p_infection)
 
#Fonctions de résistance et d'immunité   
def resistant_mort1(monde,x,y,p_mortalite,p_resistance): 
    if monde[x][y]=='I':
        a=random.random()
        if a < p_mortalite:
            monde[x][y]='D'
        if a >= (1 - p_resistance):
            monde[x][y]='R'

def resistant_mort2(monde, taille, p_mortalite, p_resistance):
    for i in range(taille):
        for j in range(taille):
            resistant_mort1(monde, i, j, p_mortalite, p_resistance)

def res_saint1(monde,x,y,glück,immunite):
    if(monde[x][y]=='R'):
        a=random.random()
        if a<=immunite:
            monde[x][y]='i'
        elif a<=glück:
        	monde[x][y]='S'
        
def res_saint2(monde, taille, glück,immunite):
    for i in range(taille):
        for j in range(taille):
            res_saint1(monde, i, j, glück, immunite)
         
def R_fin(monde,immunite):
	taille = len(monde)
	for i in range(taille):
		for j in range(taille):
			if(monde[i][j]=="R"):
				a=random.random()
				if a<=immunite:
					monde[i][j]='i'
				else:
					monde[i][j]='S'

#Fonctions renvoyant le nombre d'infectés, de guéris, d'immunisés et de morts   
def nombre_sains(monde,taille):
    nb = 0
    for i in range(taille):
        for j in range (taille):
            if monde[i][j]=='S':
                nb = nb + 1
    return nb; 
def nombre_infectes(monde,taille):
    nb = 0
    for i in range(taille):
        for j in range (taille):
            if monde[i][j]=='I':
                nb = nb + 1
    return nb;
def nombre_immunises(monde,taille):
    nb = 0
    for i in range(taille):
        for j in range (taille):
            if (monde[i][j]=='i'):
                nb = nb + 1
    return nb;
def nombre_morts(monde,taille):
    nb = 0
    for i in range(taille):
        for j in range (taille):
            if monde[i][j]=='D':
                nb = nb + 1
    return nb;
           			        			  			
#Fonction renvoyer un aperçu global de l'evolution du monde sous forme de listes
def evolution_monde_liste(monde, taille, p_infection, p_mortalite, chance,immunite):
    jours = []
    sains = []
    morts = []
    infectes = []
    immu = []
    nb_jours = 1
    while nombre_infectes(monde, taille) > 0:
        if (nb_jours % 3 == 0):
            propagation2(monde, taille, p_infection)
        if (nb_jours % 10 == 0):
            resistant_mort2(monde, taille, p_mortalite, chance)
        if (nb_jours % 20 == 0):
            res_saint2(monde, taille, chance,immunite)
        jours.append(nb_jours)
        sains.append(nombre_sains(monde, taille))
        morts.append(nombre_morts(monde, taille))
        infectes.append(nombre_infectes(monde, taille))
        immu.append(nombre_immunises(monde, taille))
        nb_jours += 1
        
    R_fin(monde,immunite)
    
    jours.append(nb_jours+1)
    sains.append(nombre_sains(monde, taille))
    morts.append(nombre_morts(monde, taille))
    infectes.append(nombre_infectes(monde, taille))
    immu.append(nombre_immunises(monde, taille))
    return sains, jours, morts, infectes, immu
        			
#Fonction renvoyer un aperçu de l'evolution du monde sous forme d'image (pour simulation)
def evolution_monde(monde, taille, p_infection, p_mortalite, chance, immunite):
    jours = []
    sains = []
    morts = []
    infectes = []
    immu = []
	
    espace_animation = st.empty()

    nb_jours = 1
    while nombre_infectes(monde, taille) > 0:
        img = afficher_matrice_image(monde)
        time.sleep(0.2)
        
        if (nb_jours % 3 == 0):
            propagation2(monde, taille, p_infection)
            espace_animation.image(img, caption=f"Jour {nb_jours}")
        if (nb_jours % 10 == 0):
            resistant_mort2(monde, taille, p_mortalite, chance)
            espace_animation.image(img, caption=f"Jour {nb_jours}")
        if (nb_jours % 20 == 0):
            res_saint2(monde, taille, chance,immunite)
            espace_animation.image(img, caption=f"Jour {nb_jours}")

        jours.append(nb_jours)
        sains.append(nombre_sains(monde, taille))
        morts.append(nombre_morts(monde, taille))
        infectes.append(nombre_infectes(monde, taille))
        immu.append(nombre_immunises(monde, taille))
        
        nb_jours += 1
    img = afficher_matrice_image(monde)
    espace_animation.image(img, caption=f"Jour {nb_jours}")
    
    R_fin(monde,immunite)
    
    img = afficher_matrice_image(monde)
    espace_animation.image(img, caption=f"Fin de l'épidemie (Jour {nb_jours+1})")
    
    jours.append(nb_jours+1)
    sains.append(nombre_sains(monde, taille))
    morts.append(nombre_morts(monde, taille))
    infectes.append(nombre_infectes(monde, taille))
    immu.append(nombre_immunises(monde, taille))
    
    return sains, jours, morts, infectes, immu
