# 🔧 Préparation : Importer et charger le fichier

```python
import pandas as pd

# Charger le fichier (en local après téléchargement sur Kaggle)
df = pd.read_csv("train.csv")

# Aperçu des données
df.head()
```

---

## ✅ Étape 1 – Supprimer les colonnes à plus de 30% de valeurs manquantes

```python
# Calcul du pourcentage de valeurs manquantes
missing_ratio = df.isnull().mean()

# Colonnes à supprimer
cols_to_drop = missing_ratio[missing_ratio > 0.3].index

# Suppression
df = df.drop(columns=cols_to_drop)

print(f"Colonnes supprimées : {list(cols_to_drop)}")
```

---

## ✅ Étape 2 – Remplacer les valeurs manquantes de `LotFrontage` par la médiane

```python
median_lotfrontage = df["LotFrontage"].median()
df["LotFrontage"] = df["LotFrontage"].fillna(median_lotfrontage)
```

---

## ✅ Étape 3 – Transformer `YearBuilt` et `YrSold` en `age_bien`

```python
# Création de la colonne âge du bien
df["age_bien"] = df["YrSold"] - df["YearBuilt"]

# Facultatif : Supprimer les anciennes colonnes
df = df.drop(columns=["YearBuilt", "YrSold"])
```

⚠️ Vérifier que l’âge est toujours positif :

```python
assert (df["age_bien"] >= 0).all(), "Erreur : des biens ont un âge négatif"
```

---

## ✅ Étape 4 – Supprimer les outliers (`SalePrice > 500000`)

```python
# Taille avant
print("Avant :", df.shape)

# Filtrage
df = df[df["SalePrice"] <= 500000]

# Taille après
print("Après :", df.shape)
```

---

## ✅ Étape 5 – Créer une version allégée avec 10 variables pertinentes

### 🎯 Exemple de 10 features clés (d'après l'analyse EDA commune du dataset) :

```python
features = [
    "SalePrice",
    "OverallQual",   # Qualité globale
    "GrLivArea",     # Surface habitable
    "GarageCars",    # Nb de places au garage
    "GarageArea",    # Surface garage
    "TotalBsmtSF",   # Surface sous-sol
    "FullBath",      # Salles de bain complètes
    "LotArea",       # Surface du terrain
    "YearRemodAdd",  # Année de rénovation
    "age_bien"       # Âge du bien
]

# Extraction
df_small = df[features]

# Vérification
df_small.info()
```

---

## 💾 Sauvegarde optionnelle

```python
df_small.to_csv("cleaned_house_prices.csv", index=False)
```

---

## ✅ Résumé des points pédagogiques

| Étape                       | Compétence mobilisée                |
| --------------------------- | ----------------------------------- |
| Suppression conditionnelle  | `isnull()`, `mean()`, `drop()`      |
| Remplissage par médiane     | `fillna()`                          |
| Feature engineering (âge)   | Calcul de nouvelles colonnes        |
| Outliers                    | Filtres conditionnels (`df[cond]`)  |
| Sélection de variables clés | Bonnes pratiques d’EDA + `df[cols]` |

---