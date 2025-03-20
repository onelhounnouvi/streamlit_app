Ce projet a pour objectifs de modéliser une <b>épidémie</b>, et de simuler sa propagation au sein d'une population d'individus. 
## Présentation du modèle

Plusieurs paramètres sont pris en compte, notamment le nombre d'individus et les probabilités d'infection, de guérison, de mortalité et d'immunité. Ces probabilités varient entre 0 et 1. Les individus sont disposés dans une matrice carrée, où chaque individu est en contact direct avec ses voisins. Ils sont représentés par les états suivants :'S' Saint, 'I' : Infecté, 'R' : Résistant, 'D' : Mort. Le schéma ci-après résume notre modèle :


<p align="center">
	<img src="https://i.goopics.net/rg959v.png" height="300" width="580">
<p/>

Gràce à l'optimisation, une version <b>online du site</b> pour la simulation est disponible <a href="https://simulationepidemie.streamlit.app/" target="_blank"><b>ici</b>.</a>
