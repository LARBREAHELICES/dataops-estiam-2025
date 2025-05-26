# `01_generalites.md`

---

### ✅ Exo 1 — Tri à bulle (Bubble Sort)

**Énoncé :**
Implémente une fonction `bubble_sort(lst: List[int]) -> List[int]` qui trie une liste d’entiers. Le tri à bulle fonctionne en comparant les éléments adjacents et en les échangeant s’ils sont mal ordonnés.

```python
from typing import List

def bubble_sort(lst: List[int]) -> List[int]:
    pass

print(bubble_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]
```

---

## ✅ Exo 2 — Fréquence des éléments

**Énoncé :**
Écris une fonction `count_frequencies(lst: List[int]) -> dict[int, int]` qui retourne un dictionnaire associant à chaque élément le nombre de fois où il apparaît dans la liste.

```python
from typing import List

def count_frequencies(lst: List[int]) -> dict[int, int]:
    pass

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
    pass

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
   pass

print(sieve(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### ✅ Exo 5 Trouver la sous-liste contiguë (les éléments qui se suivent) qui a la plus grande somme possible.