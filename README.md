# Graph Ville

## Introduction

**Graph Ville** est un projet universitaire réalisé dans le cadre de l'apprentissage de la **théorie des graphes** en informatique.

L'objectif du projet est de modéliser un réseau de villes et de routes sous forme de **graphe**, puis d'utiliser des algorithmes classiques pour analyser ce réseau. En particulier, le programme implémente l'algorithme de **Dijkstra** afin de déterminer le **plus court chemin entre plusieurs villes**.

Les villes sont représentées comme des **nœuds** et les routes comme des **arêtes pondérées** correspondant à la distance entre deux villes. Le projet permet également de **visualiser le graphe** et le chemin calculé grâce à une représentation graphique.

Ce projet a pour but de mettre en pratique plusieurs notions importantes :

* la **modélisation d'un problème avec des graphes**
* l'utilisation de **structures de données**
* l'implémentation d'un **algorithme de plus court chemin**
* la **visualisation de graphes avec Python**

---

## Comment utiliser

### 1. Dépendances

Avant d'exécuter le programme, il est nécessaire d'installer les bibliothèques Python utilisées dans le projet.

Les principales dépendances sont :

* **json** (bibliothèque standard de Python)
* **math** (bibliothèque standard de Python)
* **matplotlib**
* **networkx**

Vous pouvez installer les bibliothèques nécessaires avec la commande suivante :

```bash
pip install matplotlib networkx
```

---

### 2. Génération du fichier JSON

Le projet utilise un fichier **JSON** pour stocker :

* la liste des **villes**
* la liste des **routes** et leurs distances

Un script permet de créer ce fichier en ajoutant interactivement :

* des **villes**
* des **routes entre les villes**

Le fichier JSON sera ensuite utilisé pour construire le graphe.

---

### 3. Calcul du chemin

Une fois le fichier JSON généré :

1. lancer le programme principal
2. entrer le **nom du fichier JSON**
3. choisir la **ville de départ**
4. entrer une ou plusieurs **villes à visiter**
5. le programme calcule alors le **plus court chemin** entre les villes sélectionnées

---

### 4. Visualisation du graphe

Le programme affiche une représentation graphique du réseau de villes :

* les **villes** sont représentées par des nœuds
* les **routes** par des arêtes
* le **chemin calculé** est mis en évidence en rouge

Cette visualisation permet de mieux comprendre la structure du graphe et le trajet obtenu.
