# ✅ **Exercice 1 – Création et exploration de DataFrame**

```python
import pandas as pd

data = {
    "nom": ["Alice", "Bob", "Clara"],
    "age": [25, 30, 22],
    "ville": ["Paris", "Lyon", "Marseille"]
}

df = pd.DataFrame(data)

# 1. Afficher les 2 premières lignes
print(df.head(2))

# 2. Afficher la colonne 'ville'
print(df["ville"])

# 3. Afficher la forme du DataFrame
print(df.shape)  # (3, 3)
```

---

## ✅ **Exercice 2 – Filtrage conditionnel**

```python
# 1. Personnes ayant plus de 24 ans
print(df[df["age"] > 24])

# 2. Ville commençant par "P"
print(df[df["ville"].str.startswith("P")])
```

---

## ✅ **Exercice 3 – Ajout et modification de colonnes**

```python
# 1. Ajouter une colonne is_adult
df["is_adult"] = df["age"] >= 18

# 2. Ajouter une colonne nom_majuscules
df["nom_majuscules"] = df["nom"].str.upper()

print(df)
```

---

## ✅ **Exercice 4 – Nettoyage de données**

```python
import numpy as np

df = pd.DataFrame({
    "nom": ["Alice", "Bob", "Clara"],
    "age": [25, np.nan, 22],
    "ville": ["Paris", "Lyon", None]
})

# 1. Lignes contenant des NaN
print(df[df.isnull().any(axis=1)])

# 2. Remplacer les NaN de la colonne 'ville'
df["ville"] = df["ville"].fillna("Inconnue")

# 3. Supprimer les lignes où l'âge est NaN
df = df.dropna(subset=["age"])

print(df)
```

---

## ✅ **Exercice 5 – GroupBy et agrégation**

```python
df = pd.DataFrame({
    "nom": ["Alice", "Bob", "Alice", "Bob", "Clara"],
    "matière": ["Math", "Math", "Anglais", "Anglais", "Math"],
    "note": [15, 12, 17, 14, 18]
})

# 1. Moyenne des notes par élève
print(df.groupby("nom")["note"].mean())

# 2. Moyenne des notes par matière
print(df.groupby("matière")["note"].mean())
```

---