# 🔍 **Exercice : Nettoyage et préparation des données Titanic**

### Objectif pédagogique

* Charger un jeu de données
* Nettoyer des valeurs manquantes
* Supprimer des colonnes inutiles
* Créer des variables pertinentes

---

## 💾 Données

* Jeu de données : `titanic.csv`
* Colonnes clés : `age`, `sex`, `fare`, `embarked`, `class`, `survived`

---

## ✏️ Consignes

1. Charger les données dans un DataFrame `df`
2. Supprimer les colonnes peu informatives : `deck`, `embark_town`, `alive`, `class`, `who`, `adult_male`
3. Supprimer les lignes ayant **plus de 2 valeurs manquantes**
4. Remplir les valeurs manquantes de la colonne `age` avec sa **médiane**
5. Ajouter une colonne `is_child` : `True` si `age < 12`
6. Supprimer toutes les lignes restantes contenant des `NaN`
7. Sauvegarder le jeu de données nettoyé dans `titanic_clean.csv`

---

## ✅ Correction détaillée

```python
import pandas as pd

# 1. Charger les données (ajuster le chemin si nécessaire)
df = pd.read_csv("titanic.csv")

# Aperçu initial
print("Forme initiale :", df.shape)
print(df.isnull().sum())

# 2. Supprimer les colonnes inutiles
cols_to_drop = ["deck", "embark_town", "alive", "class", "who", "adult_male"]
df = df.drop(columns=cols_to_drop)

# 3. Supprimer les lignes avec plus de 2 valeurs manquantes
df = df[df.isnull().sum(axis=1) <= 2]

# 4. Remplacer les NaN de la colonne 'age' par sa médiane
age_median = df['age'].median()
df['age'] = df['age'].fillna(age_median)

# 5. Créer une colonne 'is_child'
df['is_child'] = df['age'] < 12

# 6. Supprimer les lignes restantes avec des valeurs manquantes
df = df.dropna()

# 7. Sauvegarder le fichier nettoyé
df.to_csv("titanic_clean.csv", index=False)

# Vérification finale
print("Forme après nettoyage :", df.shape)
print(df.head())
```

---

## 🎯 Points de contrôle pour l'évaluation

| Étape                              | Points | Vérification                                       |
| ---------------------------------- | ------ | -------------------------------------------------- |
| Données bien chargées              | 1 pt   | `df.head()` et `df.info()`                         |
| Colonnes inutiles supprimées       | 1 pt   | `df.columns` ne contient pas les colonnes retirées |
| Lignes trop incomplètes supprimées | 1 pt   | `df.isnull().sum(axis=1).max() <= 2`               |
| Age complété correctement          | 1 pt   | `df['age'].isnull().sum() == 0`                    |
| Colonne `is_child` créée           | 1 pt   | `df['is_child'].dtype == bool`                     |
| Plus aucun NaN                     | 1 pt   | `df.isnull().sum().sum() == 0`                     |
| Export du CSV                      | 1 pt   | Fichier bien généré et lisible                     |

**Total : 7 points**

---
