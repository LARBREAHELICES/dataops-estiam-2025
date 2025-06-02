# 🧪 **Jour 1 – Préparer les données avec Pandas (6h)**

---

### 🕘 **Matin (3h) — Obtenir et nettoyer les données**

#### 🎯 Objectifs pédagogiques

* Charger des données depuis différents formats
* Comprendre les structures fondamentales de Pandas (Series, DataFrame)
* Nettoyer et normaliser les données

#### 🧱 Contenu pédagogique

##### 1. Introduction à Pandas (30 min)

* Qu’est-ce qu’une Series ? un DataFrame ?
* Méthodes clés : `head()`, `info()`, `describe()`, `shape`

##### 2. Charger des données (30 min)

* Lecture depuis un fichier CSV : `pd.read_csv()`
* Lecture depuis Excel, JSON (bonus)
* Gestion des encodages, séparateurs, valeurs manquantes à l'import

```python
import pandas as pd
df = pd.read_csv("data/ventes.csv", na_values=["NA", "n/a", ""])
```

##### 3. Nettoyage des données (1h30)

* Supprimer des colonnes / lignes inutiles : `drop()`
* Renommer : `rename(columns={...})`
* Gestion des valeurs manquantes :

  * Suppression : `dropna()`
  * Remplissage : `fillna()`, `interpolate()`
* Détection et suppression des doublons : `duplicated()`, `drop_duplicates()`
* Conversion de types (`astype`, dates avec `pd.to_datetime`)

```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['prix'] = df['prix'].fillna(0).astype(float)
```

#### 🧪 Exercice guidé (30 min)

> Charger un fichier CSV contenant des ventes en ligne avec des valeurs manquantes et des doublons, puis :

* Nettoyer les noms de colonnes
* Supprimer les doublons
* Remplacer les valeurs manquantes
* Convertir les dates

---

### 🕑 **Après-midi (3h) — Transformer et structurer les données**

#### 🎯 Objectifs pédagogiques

* Transformer les données pour les rendre exploitables
* Préparer les données pour l’analyse
* Exporter les données nettoyées

#### 🧱 Contenu pédagogique

##### 4. Manipulation de colonnes (30 min)

* Création de colonnes dérivées
* Extraction de texte, dates (`.str`, `.dt`)
* Conditions : `np.where`, `apply()`, `loc[]`

```python
import numpy as np
df['remise'] = np.where(df['prix'] > 100, 0.1, 0.05)
```

##### 5. Transformation des données (1h30)

* Regrouper et agréger : `groupby()`
* Trier et filtrer : `sort_values()`, `query()`
* Pivot / depivot : `pivot_table()`, `melt()`
* Fusionner des DataFrames : `merge()`, `join()`

```python
total_par_jour = df.groupby('date')['prix'].sum().reset_index()
```

##### 6. Exportation / sauvegarde (30 min)

* Enregistrer les données : `to_csv()`, `to_excel()`
* Aperçu d'une sauvegarde dans une base SQLite (bonus)

```python
df.to_csv("data/ventes_clean.csv", index=False)
```

---

### 🧪 Mini-projet de fin de journée (1h)

> Trouvez un fichier à étudier sur des ventes:

1. De nettoyer les colonnes, supprimer les lignes incohérentes
2. De créer des colonnes : total TTC, jour de la semaine, catégorie
3. De grouper par date ou produit et calculer des totaux
4. D’exporter le fichier nettoyé en CSV

💡 Option : corriger en live avec un notebook modèle

---

### 📁 Fichiers nécessaires

* `ventes.csv` (données brutes avec erreurs volontaires)
* `produits.csv` (données de référence pour `merge()`)
* Notebook Jupyter vierge et corrigé
