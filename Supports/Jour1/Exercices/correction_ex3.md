Voici une **séquence pédagogique complète et corrigée** pour la partie **Nettoyage des données (1h30)** avec des exercices progressifs, fondés sur des bibliothèques connues (Pandas, Seaborn) et des manipulations classiques : suppression, renommage, valeurs manquantes, doublons, types.

---

## 🧪 Atelier : Nettoyage des données (1h30)

**Dataset utilisé :** `seaborn.load_dataset("diamonds")`
📦 (`diamonds.csv` très riche et réaliste : plus de 50 000 lignes)

---

### ⚙️ Mise en place (0–5 min)

```python
import pandas as pd
import seaborn as sns

# Charger les données
df = sns.load_dataset("diamonds")
df.head()
```

---

## ✅ Exercice 1 — Suppression de colonnes / lignes inutiles (15 min)

### 🔧 Consignes :

* Supprimer la colonne `table` (inutile ici)
* Supprimer les lignes où le prix (`price`) est inférieur à 350 (valeurs aberrantes)

### ✅ Correction :

```python
# Suppression de colonne
df = df.drop(columns=["table"])

# Suppression de lignes avec prix < 350
df = df[df["price"] >= 350]
```

---

## ✅ Exercice 2 — Renommer proprement (10 min)

### 🔧 Consignes :

* Renommer `x`, `y`, `z` en `length`, `width`, `depth`

### ✅ Correction :

```python
df = df.rename(columns={"x": "length", "y": "width", "z": "depth"})
```

---

## ✅ Exercice 3 — Gérer les valeurs manquantes (25 min)

### 🔧 Préparation (simulation de valeurs manquantes) :

```python
import numpy as np

# Simuler des valeurs manquantes
df.loc[df.sample(frac=0.01).index, "depth"] = np.nan
df.loc[df.sample(frac=0.005).index, "length"] = np.nan
```

### 🔧 Consignes :

1. Compter les valeurs manquantes
2. Supprimer les lignes avec plus d'une valeur manquante
3. Remplir les `depth` manquants par la **médiane**
4. Remplir les `length` manquants par interpolation

### ✅ Correction :

```python
# 1. Compter
print(df.isnull().sum())

# 2. Supprimer les lignes avec > 1 NaN
df = df[df.isnull().sum(axis=1) <= 1]

# 3. Remplissage par médiane
df["depth"] = df["depth"].fillna(df["depth"].median())

# 4. Interpolation linéaire
df["length"] = df["length"].interpolate()
```

---

## ✅ Exercice 4 — Supprimer les doublons (10 min)

### 🔧 Consignes :

* Vérifier les doublons exacts
* Les supprimer

### ✅ Correction :

```python
# Vérification
print("Doublons :", df.duplicated().sum())

# Suppression
df = df.drop_duplicates()
```

---

## ✅ Exercice 5 — Conversion de types (20 min)

### 🔧 Préparation (ajout d'une colonne simulée) :

```python
df["date"] = pd.date_range(start="2022-01-01", periods=len(df), freq="H")
df.loc[df.sample(frac=0.01).index, "date"] = None  # valeurs manquantes
df["price"] = df["price"].astype(str)  # price devient objet
```

### 🔧 Consignes :

1. Convertir `date` au format datetime (avec erreurs en NaT)
2. Convertir `price` en float
3. Remplacer les `NaT` dans `date` par la **date minimale**

### ✅ Correction :

```python
# 1. Conversion en datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 2. Conversion de price en float
df["price"] = df["price"].astype(float)

# 3. Remplacer les dates manquantes
min_date = df["date"].min()
df["date"] = df["date"].fillna(min_date)
```

---

## 🎓 Vérification finale / évaluation rapide

| Étape                           | Points |
| ------------------------------- | ------ |
| Suppression correcte (`drop()`) | 1 pt   |
| Renommage (`rename`)            | 1 pt   |
| Valeurs manquantes bien gérées  | 2 pts  |
| Doublons supprimés              | 1 pt   |
| Types bien convertis            | 2 pts  |
| Code propre et reproductible    | 1 pt   |

---

Souhaitez-vous que je vous prépare une **version notebook prête à distribuer** (énoncés + cellules de correction) ?
