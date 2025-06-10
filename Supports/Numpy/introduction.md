# 📌 1. Qu’est-ce que NumPy ?

NumPy (**Numerical Python**) est une **bibliothèque** Python pour :

* le calcul scientifique rapide,
* la manipulation de **tableaux multidimensionnels (ndarray)**,
* les **opérations vectorielles** et matricielles (linéaires, statistiques, etc.).

👉 Elle sert de **base** à d'autres bibliothèques comme `Pandas`, `SciPy`, `scikit-learn` ou `TensorFlow`.

---

## ⚙️ 2. Installation

```bash
pip install numpy
```

---

## 🧱 3. Tableau NumPy (`ndarray`)

```python
import numpy as np

a = np.array([1, 2, 3])
print(a)          # [1 2 3]
print(a.shape)    # (3,)
```

### ⚠️ Différence avec une liste Python :

* `np.array` = **tableau typé, rapide, vectorisé**
* `list` = objet générique, lent pour le calcul scientifique

---

## 📏 4. Dimensions

```python
# 1D
a = np.array([1, 2, 3])

# 2D
b = np.array([[1, 2], [3, 4]])

# 3D
c = np.array([[[1], [2]], [[3], [4]]])
```

---

## 🔁 5. Création rapide de tableaux

```python
np.zeros((2, 3))     # Tableau de zéros (2 lignes, 3 colonnes)
np.ones((3, 3))      # Tableau de uns
np.eye(4)            # Matrice identité 4x4
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 1, 5) # [0.  0.25 0.5  0.75 1. ]
```

---

## 🔢 6. Opérations vectorielles

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b     # [5 7 9]
a * b     # [ 4 10 18]
a @ b     # 32 (produit scalaire)
a ** 2    # [1 4 9]
np.sqrt(a)  # [1. 1.41 1.73]
```

> ✔️ Les opérations sont **élémentaires** (pas besoin de boucle).

---

## 🔁 7. Indexation, slicing, masques

```python
a = np.array([10, 20, 30, 40, 50])

a[0]      # 10
a[-1]     # 50
a[1:4]    # [20 30 40]
a[a > 25] # [30 40 50]
```

---

## 🔄 8. Reshape et transposition

```python
a = np.arange(6).reshape((2, 3))  # [[0 1 2]
                                  #  [3 4 5]]
a.T       # Transpose
a.flatten()  # Transforme en 1D
```

---

## 📈 9. Statistiques et agrégats

```python
a = np.array([[1, 2], [3, 4]])

a.sum()         # 10
a.mean()        # 2.5
a.max(axis=0)   # [3 4] (par colonne)
a.min(axis=1)   # [1 3] (par ligne)
```

---

## 💡 10. Broadcasting

Permet de faire des opérations entre tableaux de **formes différentes** :

```python
a = np.array([[1], [2], [3]])   # shape (3,1)
b = np.array([10, 20, 30])      # shape (3,)

a + b   # Résultat : (3x3) → broadcasting automatique
```

---

## 🧪 Exemple d’application

### Crible d’Ératosthène en NumPy :

```python
def sieve_np(n: int) -> np.ndarray:
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = False
    return np.flatnonzero(sieve)  # retourne les indices True
```

---

## 🧠 En résumé

| Concept            | Exemple                    |
| ------------------ | -------------------------- |
| Création tableau   | `np.array([1, 2, 3])`      |
| Formes & reshaping | `.shape`, `.reshape()`     |
| Broadcasting       |  `a + b`, `a @ b`, `a > 0`  |
| Agrégats           | `sum()`, `mean()`, `max()` |
| Slicing / Masquage | `a[a > 10]`                |

---
