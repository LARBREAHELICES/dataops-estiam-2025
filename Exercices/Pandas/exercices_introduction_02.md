Parfait ! Voici **5 exercices intermédiaires à avancés** sur **Pandas**, conçus pour approfondir la manipulation des données :

---

### 🧠 **Exercice 1 – Analyse temporelle (datetime)**

Un DataFrame contient les dates de commandes d’un site e-commerce :

```python
import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "order_date": ["2023-01-01", "2023-01-05", "2023-01-07", "2023-01-15", "2023-01-20"],
    "amount": [100, 150, 200, 130, 90]
})
```

**Tâches :**

1. Convertis la colonne `order_date` en format datetime.
2. Ajoute une colonne `weekday` avec le jour de la semaine.
3. Calcule le total des ventes par jour de la semaine.

---

### 🧠 **Exercice 2 – Jointures entre deux DataFrames**

```python
clients = pd.DataFrame({
    "client_id": [1, 2, 3],
    "nom": ["Alice", "Bob", "Clara"]
})

commandes = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "client_id": [1, 1, 2, 3],
    "montant": [50, 75, 100, 30]
})
```

**Tâches :**

1. Effectue une jointure (`merge`) entre les clients et leurs commandes.
2. Calcule le total des dépenses par client.
3. Trie les clients par dépense totale décroissante.

---

### 🧠 **Exercice 3 – Remplissage avancé et valeurs manquantes**

```python
df = pd.DataFrame({
    "date": pd.date_range("2023-01-01", periods=6),
    "temperature": [10, None, None, 15, None, 20]
})
```

**Tâches :**

1. Remplis les `NaN` par la moyenne des températures connues.
2. Remplis les `NaN` par interpolation linéaire.
3. Quelle différence entre les deux résultats ?

---

### 🧠 **Exercice 4 – Pivot et regroupement complexe**

```python
df = pd.DataFrame({
    "année": [2022, 2022, 2023, 2023],
    "ville": ["Paris", "Lyon", "Paris", "Lyon"],
    "ventes": [200, 150, 300, 100]
})
```

**Tâches :**

1. Crée un tableau croisé (pivot) avec les années en ligne, villes en colonnes, et la somme des ventes.
2. Calcule l’évolution en pourcentage des ventes entre 2022 et 2023 pour chaque ville.

---

### 🧠 **Exercice 5 – Manipulation avancée avec `apply`**

```python
df = pd.DataFrame({
    "produit": ["Livre", "Stylo", "Ordinateur", "Clé USB"],
    "prix_ht": [20, 1.5, 900, 10],
    "TVA": [0.05, 0.2, 0.2, 0.2]
})
```

**Tâches :**

1. Crée une colonne `prix_ttc` en appliquant une fonction via `apply`.
2. Crée une fonction qui classe les produits en `"bon marché"`, `"moyen"` ou `"cher"` selon le prix TTC.
3. Applique-la pour créer une colonne `catégorie`.

---

Souhaites-tu que je corrige et explique l’un d’eux tout de suite ?
