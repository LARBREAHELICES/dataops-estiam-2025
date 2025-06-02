# `01_generalites.md`

---

### ✅ Exo 1 — Tri à bulle (Bubble Sort)

**Énoncé :**
Implémente une fonction `bubble_sort(lst: List[int]) -> List[int]` qui trie une liste d’entiers. Le tri à bulle fonctionne en comparant les éléments adjacents et en les échangeant s’ils sont mal ordonnés.

```python
from typing import List

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]
```

---

## ✅ Exo 2 — Fréquence des éléments

**Énoncé :**
Écris une fonction `count_frequencies(lst: List[int]) -> dict[int, int]` qui retourne un dictionnaire associant à chaque élément le nombre de fois où il apparaît dans la liste.

```python
from typing import List

def count_frequencies(lst: List[int]) -> dict[int, int]:
    frequencies = {}
    for number in lst:
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1
    return frequencies

print(count_frequencies([1, 2, 2, 3, 1, 2, 4]))  
# {1: 2, 2: 3, 3: 1, 4: 1}
```

---

### ✅ Exo 3 — Trouver l’élément majoritaire (Boyer-Moore)

**Énoncé :**
Écrire une fonction `majority_element(lst: List[int]) -> Optional[int]` qui retourne l’élément apparaissant plus de `n // 2` fois s’il existe, sinon `None`.

```python
from typing import List, Optional

def majority_element(lst: List[int]) -> Optional[int]:
    count = 0
    candidate = None
    for num in lst:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    # Vérification
    if lst.count(candidate) > len(lst) // 2:
        return candidate
    return None

print(majority_element([3, 3, 4, 2, 3, 3, 3]))  # 3
print(majority_element([1, 2, 3, 4]))           # None
```

---

### ✅ Exo 4 — Calcul des nombres premiers jusqu’à N (Crible d’Ératosthène)

**Énoncé :**
Écrire une fonction `sieve(n: int) -> List[int]` qui retourne la liste de tous les nombres premiers ≤ `n`. Utilise le **crible d’Ératosthène**, un algorithme efficace pour cela.

```python
from typing import List

def sieve(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

print(sieve(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### ✅ Exo 5 Trouver la sous-liste contiguë (les éléments qui se suivent) qui a la plus grande somme possible.

```python

from typing import List

def max_subarray_sum(lst: List[int]) -> int:
    if not lst:
        return 0  # cas où la liste est vide
    
    max_current = max_global = lst[0]  # on commence avec le premier élément
    
    for x in lst[1:]:
        # Choix : soit on repart de x, soit on continue la somme précédente
        max_current = max(x, max_current + x)

        # Mise à jour du max global si nécessaire
        max_global = max(max_global, max_current)

    return max_global

```

Parfait ! Voici **une version commentée pas à pas** de l'algorithme de Kadane, qui permet de trouver **la plus grande somme possible d’une sous-liste contiguë** dans une liste d’entiers :

---

### 💡 Objectif

Trouver la sous-liste contiguë (les éléments qui se suivent) qui a **la plus grande somme possible**.

L'algorithme de Kadane trouve la meilleure sous-liste contiguë, c’est-à-dire celle qui a la somme maximale, parmi toutes les sous-listes dont les éléments se suivent dans la liste d’origine.

---

### 🧠 Algorithme de Kadane commenté

```python
from typing import List

def max_subarray_sum(lst: List[int]) -> int:
    if not lst:
        return 0  # cas où la liste est vide
    
    max_current = max_global = lst[0]  # on commence avec le premier élément
    
    for x in lst[1:]:
        # Choix : soit on repart de x, soit on continue la somme précédente
        max_current = max(x, max_current + x)

        # Mise à jour du max global si nécessaire
        max_global = max(max_global, max_current)

    return max_global
```


### 🔍 Exemple 1 pas à pas

```python
lst = [4, -1, 2, 1, -5, 4]
```

| Étape | x  | max\_current + x | max\_current   | max\_global |
| ----- | -- | ---------------- | -------------- | ----------- |
| init  | 4  | —                | 4              | 4           |
| 1     | -1 | 4 + (-1) = 3     | max(-1, 3) = 3 | 4           |
| 2     | 2  | 3 + 2 = 5        | max(2, 5) = 5  | 5 ✅         |
| 3     | 1  | 5 + 1 = 6        | max(1, 6) = 6  | 6 ✅         |
| 4     | -5 | 6 + (-5) = 1     | max(-5, 1) = 1 | 6           |
| 5     | 4  | 1 + 4 = 5        | max(4, 5) = 5  | 6           |

### ✅ Résultat final : `6`

La sous-liste `[4, -1, 2, 1]` donne la plus grande somme possible.

---

### 🧠 En résumé

* À chaque étape, on choisit :

  * Soit de **continuer la somme** avec l’élément suivant.
  * Soit de **repartir à zéro** avec ce nouvel élément.
* On garde toujours le meilleur score global vu jusqu’ici.

---

### 🔍 Exemple 2 pas à pas

```python
lst = [1, 2, 3, 4]
```

| Étape | x | max\_current + x | max\_current    | max\_global |
| ----- | - | ---------------- | --------------- | ----------- |
| init  | 1 | —                | 1               | 1           |
| 1     | 2 | 1 + 2 = 3        | max(2, 3) = 3   | 3           |
| 2     | 3 | 3 + 3 = 6        | max(3, 6) = 6   | 6           |
| 3     | 4 | 6 + 4 = 10       | max(4, 10) = 10 | 10 ✅        |
