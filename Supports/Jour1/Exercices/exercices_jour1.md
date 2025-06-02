# 📦 Bibliothèques utilisées :

* `pandas` : manipulation de données
* `numpy` : opérations conditionnelles
* `seaborn` : accès à des jeux de données classiques (`titanic`, `tips`, etc.)
* `os`, `glob`, `json`, `csv` : manipulation de fichiers si besoin

---

## 🧠 Objectifs : Nettoyer, transformer, structurer, exporter

---

### 🧪 Exercice 1 — Titanic Cleanup (20 min)

**Dataset :** `seaborn.load_dataset("titanic")`

**Objectif :** Nettoyer les données du Titanic.

**Étapes :**

1. Charger le dataset
2. Identifier les colonnes inutiles (`deck`, `embark_town`, etc.)
3. Supprimer les lignes avec plus de 2 valeurs manquantes
4. Remplir la colonne `age` par la médiane
5. Créer une colonne `is_child` si `age < 12`
6. Sauvegarder les données nettoyées

```python
import seaborn as sns
df = sns.load_dataset("titanic")
```

---

### 🧪 Exercice 2 — Analyse de tickets de restaurant (30 min)

**Dataset :** `seaborn.load_dataset("tips")`

**Objectif :** Transformer les données pour analyse.

**Étapes :**

1. Ajouter une colonne `pourboire_ratio = tip / total_bill`
2. Transformer le champ `sex` en booléen (`is_female`)
3. Grouper par jour (`day`) et calculer :

   * Montant total
   * Moyenne des pourboires
   * Nombre de clients
4. Sauvegarder en CSV

---

### 🧪 Exercice 3 — Simulation de fusion de fichiers CSV (30 min)

**Dataset :** 3 fichiers CSV simulés : `jan.csv`, `feb.csv`, `mar.csv` avec les colonnes `date, produit, quantite, prix_unitaire`

**Objectif :** Fusionner, nettoyer et enrichir les données.

**Étapes :**

1. Lire tous les fichiers du dossier avec `glob.glob("data/*.csv")`
2. Les concaténer avec `pd.concat()`
3. Calculer `total = quantite * prix_unitaire`
4. Créer une colonne `mois` à partir de la date
5. Sauvegarder le fichier final

💡 *Astuce : tu peux créer ces CSV artificiellement avec du code.*

---

### 🧪 Exercice 4 — House Prices Cleanup (Kaggle dataset) (40 min)

**Dataset :** [House Prices - Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
(fichier : `train.csv`)

**Objectif :** Préparer un dataset pour la modélisation.

**Étapes :**

1. Supprimer les colonnes à plus de 30% de valeurs manquantes
2. Remplacer les valeurs manquantes de `LotFrontage` par la médiane
3. Transformer les colonnes `YearBuilt` et `YrSold` en `age_bien`
4. Supprimer les outliers de prix (`SalePrice > 500000`)
5. Créer une version allégée contenant 10 features clés

---

### 🧪 Mini-projet — Nettoyage et préparation d’un jeu e-commerce (1h+)

**Dataset :** Fichier `ecommerce_data.csv` fictif ou réel (OpenFoodFacts, Olist, etc.)

**Objectif :** Nettoyage complet + enrichissement + agrégation

**Étapes :**

1. Nettoyer les colonnes mal nommées, normaliser les types
2. Créer des colonnes `total_HT`, `TVA`, `total_TTC`
3. Extraire la catégorie à partir d’un champ `produit`
4. Grouper les ventes par `jour`, `catégorie` et calculer :

   * Total HT, nombre de ventes
5. Exporter 2 fichiers : un "dataset\_clean", un "report\_par\_catégorie"

---
