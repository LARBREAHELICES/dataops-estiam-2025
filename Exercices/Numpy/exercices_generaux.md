### 🧩 Exercice 1 : Inverser des mots

**Énoncé :**
Vous avez un tableau **NumPy** de chaînes de caractères. 
Inversez chaque mot individuellement (sans changer l’ordre global du tableau).

```python
words = np.array(["apple", "banana", "cherry"])
# Résultat attendu : ["elppa", "ananab", "yrrehc"]
```

**Indications :**
Utilisez les fonctions de la sous-bibliothèque `np.char`.

---

### 🔁 Exercice 2 : Supprimer les doublons successifs

**Énoncé :**
Écrivez une fonction `remove_consecutive_duplicates(arr)` qui supprime uniquement les **doublons consécutifs** dans un tableau 1D.

```python
arr = np.array([1, 1, 2, 2, 2, 3, 1, 1])
# Résultat : [1, 2, 3, 1]
```

**Indications :**
Utilisez des mask et np.zeros, pensez à l'initialiser avec des `bool`

---

## 🔄 Niveau 2 – Algorithmes de transformation

### 🪟 Exercice 3 : Fenêtrage glissant (sliding window)

**Énoncé :**
Écrivez une fonction `sliding_windows(arr, size)` qui retourne une vue glissante sur un tableau 1D, avec des fenêtres de taille fixe.

```python
arr = np.array([1, 2, 3, 4, 5])
size = 3
# Résultat : [[1,2,3], [2,3,4], [3,4,5]]
```

**Indications :**
Utilisez le principe du slicing

---

### 🧮 Exercice 4 : Compression RLE (Run-Length Encoding)

**Énoncé :**
Écrivez une fonction qui compresse un tableau 1D en deux tableaux :

1. Les valeurs uniques **consécutives**,
2. Leur **nombre de répétitions**.

```python
arr = np.array([1, 1, 2, 2, 2, 3, 1, 1])
# Résultat : values=[1,2,3,1], counts=[2,3,1,2]
```

**Indications :**
Découpez l'exercice en plusieurs fonctions et utilisez la fonction `remove_consecutive_duplicates`

---
