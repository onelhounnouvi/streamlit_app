import streamlit as st
from fonct_aff import *
from fonctions import *
from matplotlib import pyplot as plt

st.title('Simulation épidémologique')

with st.sidebar.form(key='Parametres de la simulation'):
    taille = st.slider(label="Taille de la matrice", min_value=1, max_value=100, value=20)
    p_infection = st.slider(label="Probabilité d'infection", min_value=0., max_value=1., value=0.5, step=0.01)
    p_guerison = st.slider(label="Probabilité de guérison", min_value=0., max_value=1., value=0.3, step=0.01)
    p_mort = st.slider(label="Probabilité de mortalité", min_value=0., max_value=1., value=0.3, step=0.01)
    p_immunite = st.slider(label="Probabilité d'immunité", min_value=0., max_value=1., value=0.3, step=0.01)
    submit_button = st.form_submit_button(label='Lancer la simulation')
st.sidebar.subheader("La simulation prend un moment")

m = monde(taille)
point_de_depart(m, taille,1)
sains,jours,morts,infectes,immu = evolution_monde(m, taille, p_infection, p_mort, p_guerison,p_immunite)

# Création de la figure Matplotlib
fig, ax = plt.subplots()

ax.plot(jours, morts, color='red', label='Evolution du nbre de morts')
ax.plot(jours, infectes, color='yellow', label="Evolution du nbre d'infectes")
ax.plot(jours, immu, color='blue', label="Evolution du nbre d'immunises")
ax.plot(jours, sains, color='black', label="Evolution du nbre d'individus sains")

ax.set_xlabel("Nombre de jours")
ax.set_ylabel("Nombre d'individus")
ax.set_title("Courbe d'évolution")

ax.legend()

st.pyplot(fig)
