import streamlit as st
from PIL import Image, ImageDraw

def afficher_matrice_image(matrice):
    taille = len(matrice)
    taille_cellule_min = 20  # Taille minimale de la cellule en pixels
    taille_affichage = max(500, taille * taille_cellule_min)  # Ajuster la taille de l'affichage

    taille_cellule = taille_affichage // taille  # Calculer la nouvelle taille de cellule

    # Créer une image blanche de la nouvelle taille
    img = Image.new('RGB', (taille_affichage, taille_affichage), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Dessiner les grilles
    for i in range(taille + 1):
        draw.line([(i * taille_cellule, 0), (i * taille_cellule, taille_affichage)], fill=(200, 200, 200), width=1)
        draw.line([(0, i * taille_cellule), (taille_affichage, i * taille_cellule)], fill=(200, 200, 200), width=1)

    # Remplir les cellules en fonction de l'état dans la matrice
    for i in range(taille):
        for j in range(taille):
            couleur = (255, 255, 255)  # Blanc par défaut
            if matrice[i][j] == 'S':
                couleur = (255, 255, 255)  # Blanc
            elif matrice[i][j] == 'I':
                couleur = (255, 255, 0)  # Jaune
            elif matrice[i][j] == 'R':
                couleur = (0, 128, 0)  # Vert
            elif matrice[i][j] == 'i':
                couleur = (0, 0, 255) #bleu
            elif matrice[i][j] == 'D':
                couleur = (255, 0, 0)  # Rouge
            draw.rectangle([(j * taille_cellule, i * taille_cellule),
                            ((j + 1) * taille_cellule - 1, (i + 1) * taille_cellule - 1)],
                           fill=couleur, outline=(200, 200, 200))

    return img
