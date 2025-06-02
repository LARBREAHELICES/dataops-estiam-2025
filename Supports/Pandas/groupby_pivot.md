# 📚 Cours rapide : `groupby` et tables de pivot en Pandas

---

## 1. `groupby()` — Regrouper et agréger

La méthode `groupby()` permet de **regrouper un DataFrame selon une ou plusieurs colonnes**, puis d’appliquer une fonction d’agrégation (somme, moyenne, compte, etc.) sur chaque groupe.

---

### Syntaxe générale :

```python
df.groupby("colonne_groupe")[colonne_à_aggréger].fonction()
```

---

### Exemple simple — Calculer la moyenne du prix par catégorie :

```python
import pandas as pd

df = pd.DataFrame({
    "catégorie": ["A", "B", "A", "B", "C"],
    "valeur": [10, 20, 30, 40, 50]
})

moyennes = df.groupby("catégorie")["valeur"].mean()
print(moyennes)
```

**Sortie :**

```
catégorie
A    20.0
B    30.0
C    50.0
Name: valeur, dtype: float64
```

---

### Regrouper par plusieurs colonnes :

```python
df.groupby(["col1", "col2"]).agg({"valeur": "sum", "autre_col": "mean"})
```

---

## 2. Tables de pivot (`pivot_table`) — Tableau croisé dynamique

La fonction `pivot_table` permet de **restructurer** un DataFrame en tableau croisé, avec :

* lignes (`index`)
* colonnes (`columns`)
* valeurs à agréger (`values`)
* fonction d’agrégation (`aggfunc`), par défaut moyenne

---

### Syntaxe générale :

```python
pd.pivot_table(df, index="col_lignes", columns="col_colonnes", values="col_valeurs", aggfunc="fonction")
```

---

### Exemple — Moyenne des valeurs par catégorie (lignes) et sous-catégorie (colonnes) :

```python
df = pd.DataFrame({
    "catégorie": ["A", "A", "B", "B"],
    "sous_cat": ["X", "Y", "X", "Y"],
    "valeur": [10, 20, 30, 40]
})

pivot = pd.pivot_table(df, index="catégorie", columns="sous_cat", values="valeur", aggfunc="mean")
print(pivot)
```

**Sortie :**

```
sous_cat      X     Y
catégorie            
A          10.0  20.0
B          30.0  40.0
```

---

### Autres usages :

* `aggfunc="sum"` pour somme
* Plusieurs fonctions avec `aggfunc=[np.mean, np.sum]`
* Remplacer les valeurs manquantes avec `fill_value=0`

---

## 3. Différences clés entre `groupby` et `pivot_table`

| Aspect               | `groupby`                                    | `pivot_table`                     |
| -------------------- | -------------------------------------------- | --------------------------------- |
| Résultat             | DataFrame ou Series groupé                   | DataFrame format table croisée    |
| Multi-index          | Oui                                          | Oui                               |
| Répartition colonnes | Pas automatique, nécessite reshape si besoin | Colonnes créées selon `columns`   |
| Agrégation multiple  | Facile avec `.agg()`                         | Facile avec `aggfunc` (liste)     |
| Remplissage NA       | Manuel                                       | Paramètre `fill_value` disponible |

---

## 4. Exemple combiné avec un vrai DataFrame

```python
import seaborn as sns

tips = sns.load_dataset("tips")

# Moyenne du total par jour (groupby)
moyenne_jour = tips.groupby("day")["total_bill"].mean()
print(moyenne_jour)

# Pivot table : moyenne total_bill par jour (index) et repas (columns)
pivot = pd.pivot_table(tips, index="day", columns="time", values="total_bill", aggfunc="mean")
print(pivot)
```

---

### 🧪 Exercice 1 — Moyenne des notes par classe (groupby)

**Contexte :**
Un DataFrame contient des notes d’élèves avec leur classe.

```python
import pandas as pd

data = {
    "élève": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "classe": ["A", "B", "A", "B", "A"],
    "note": [15, 12, 14, 11, 16]
}
df = pd.DataFrame(data)
```

**Objectif :**
Calculer la moyenne des notes par classe avec `groupby`.

---

### Correction :

```python
moyenne_par_classe = df.groupby("classe")["note"].mean()
print(moyenne_par_classe)
```

**Résultat attendu :**

```
classe
A    15.0
B    11.5
Name: note, dtype: float64
```

---

### 🧪 Exercice 2 — Tableau croisé des ventes par produit et région (pivot\_table)

**Contexte :**
Voici un tableau de ventes.

```python
data = {
    "produit": ["P1", "P1", "P2", "P2", "P1"],
    "région": ["Nord", "Sud", "Nord", "Sud", "Sud"],
    "ventes": [100, 150, 200, 300, 130]
}
df = pd.DataFrame(data)
```

**Objectif :**
Créer un tableau croisé dynamique affichant la somme des ventes par produit (index) et par région (colonnes).

---

### Correction :

```python
pivot = pd.pivot_table(df, index="produit", columns="région", values="ventes", aggfunc="sum", fill_value=0)
print(pivot)
```

**Résultat attendu :**

```
région   Nord  Sud
produit            
P1        100  280
P2        200  300
```

---