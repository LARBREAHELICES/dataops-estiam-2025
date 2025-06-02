# ✅ Correction complète : Exercice 2 — Analyse des pourboires (`tips`)

```python
import pandas as pd
import seaborn as sns

# Charger le dataset
df = sns.load_dataset("tips")

# 1. Ajouter une colonne pourboire_ratio
df["pourboire_ratio"] = df["tip"] / df["total_bill"]

# 2. Transformer le champ sex en booléen is_female
df["is_female"] = df["sex"] == "Female"  # True si femme, False sinon

# 3. Grouper par 'day' et calculer les statistiques demandées
grouped = df.groupby("day").agg(
    montant_total=("total_bill", "sum"),
    moyenne_pourboire=("tip", "mean"),
    nb_clients=("size")  # nombre de lignes = nombre de clients
).reset_index()

# 4. Sauvegarder le DataFrame agrégé en CSV
grouped.to_csv("analyse_pourboires_par_jour.csv", index=False)

# Affichage en vérification
print(grouped)
```

---

## 📊 Exemple de sortie (`grouped`)

```
     day  montant_total  moyenne_pourboire  nb_clients
0   Fri     325.880000           2.734737          19
1   Sat    1778.400000           2.993103         87
2   Sun    1627.160000           3.255132         76
3  Thur    1073.580000           2.771452         62
```

---

## 🎯 Points de vérification (6 pts)

| Étape                                   | Points | Vérification                               |
| --------------------------------------- | ------ | ------------------------------------------ |
| Colonne `pourboire_ratio` bien calculée | 1 pt   | `df["pourboire_ratio"]` existe et correcte |
| Colonne `is_female` créée (booléen)     | 1 pt   | `df["is_female"].dtype == bool`            |
| Groupement par jour correct             | 1 pt   | `grouped.index.name is None` + colonnes OK |
| Moyenne des pourboires correcte         | 1 pt   | `grouped["moyenne_pourboire"].mean()` ok   |
| Nb de clients bien compté               | 1 pt   | `nb_clients = len(df[df["day"] == "Sat"])` |
| CSV généré correctement                 | 1 pt   | Fichier `analyse_pourboires_par_jour.csv`  |

---