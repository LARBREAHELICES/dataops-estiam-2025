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


# 2. Ville commençant par "P"

```

---

## ✅ **Exercice 3 – Ajout et modification de colonnes**

```python
# 1. Ajouter une colonne is_adult


# 2. Ajouter une colonne nom_majuscules



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


# 2. Remplacer les NaN de la colonne 'ville'


# 3. Supprimer les lignes où l'âge est NaN


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


# 2. Moyenne des notes par matière

```

---
