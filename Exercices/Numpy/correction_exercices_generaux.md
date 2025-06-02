## ✅ Exercice 1 : Inverser des mots

```python
import numpy as np

words = np.array(["apple", "banana", "cherry"])
reversed_words = np.char[::-1](words)

print(reversed_words)  # ['elppa' 'ananab' 'yrrehc']
```

---

## ✅ Exercice 2 : Supprimer les doublons successifs

```python
def remove_consecutive_duplicates(arr: List[int]) -> List[int]:
    # Crée un masque booléen indiquant où les éléments consécutifs sont différents
    # arr[1:] décale le tableau d'un élément vers la gauche (tous sauf le premier)
    # arr[:-1] décale le tableau d'un élément vers la droite (tous sauf le dernier)
    # La comparaison element-wise renvoie True quand deux éléments consécutifs sont différents
    mask = arr[1:] != arr[:-1]
    
    # Initialise un tableau booléen de la même longueur que arr avec des False
    keep = np.zeros(len(arr), dtype=bool)
    
    # Le premier élément doit toujours être gardé, donc on marque sa position comme True
    keep[0] = True
    
    # Remplit le reste du masque avec les résultats de la comparaison précédente
    # Ainsi, on garde tous les éléments qui diffèrent de leur prédécesseur immédiat
    keep[1:] = mask
    
    # Retourne un tableau ne contenant que les éléments dont le masque est True,
    # c'est-à-dire sans doublons consécutifs
    return arr[keep]

arr = np.array([1, 1, 2, 2, 2, 3, 1, 1])
print(remove_consecutive_duplicates(arr))  # [1 2 3 1]
```

---

## ✅ Exercice 3 : Fenêtrage glissant (sliding window)

```python
def sliding_windows(arr, seq):
    """
    Génère des fenêtres glissantes de taille `seq` à partir du tableau 1D `arr`.
    Chaque fenêtre est une tranche de `arr` de longueur `seq`, décalée d’un élément.
    """
    assert 0 < seq <= len(arr)
    # On s'arrête à len(arr) - seq + 1 pour ne pas dépasser la fin du tableau
    return [arr[i:i + seq] for i in range(len(arr) - seq + 1)]

# Test 1 : tableau de taille 5, fenêtres de taille 3
arr = np.array([1, 2, 3, 4, 5])
print(sliding_windows(arr, 3))
# Résultat attendu : [array([1, 2, 3]), array([2, 3, 4]), array([3, 4, 5])]

# Test 2 : tableau de taille 6, fenêtres de taille 3
arr = np.array([1, 2, 3, 4, 5, 6])
print(sliding_windows(arr, 3))
```

---

## ✅ Exercice 4 : Compression RLE (Run-Length Encoding)

```python
def run_length_encode(arr):
    n = len(arr)
    if n == 0:
        return np.array([]), np.array([])
    change_indices = np.where(np.diff(arr) != 0)[0] + 1
    indices = np.concatenate(([0], change_indices, [n]))
    values = arr[indices[:-1]]
    counts = np.diff(indices)
    return values, counts

arr = np.array([1, 1, 2, 2, 2, 3, 1, 1])
vals, cnts = run_length_encode(arr)
print(vals)  # [1 2 3 1]
print(cnts)  # [2 3 1 2]


def count_seq_pos(arr_bool, arr):
    i = 0
    positions = []
    lengths= []
    while i < len(arr_bool):
        el = int(arr[i])
        if arr_bool[i] == True:
            # début d'une séquence
            start = i
            length = 1  # on compte le True
    
            # on avance dans le tableau pour compter les False qui suivent
            j = i + 1
            while j < len(arr_bool) and arr_bool[j] == False:
                length += 1
                j += 1
            
            # enregistrer la position et la longueur
            positions.append(el)
            lengths.append(length)
    
            # continuer à partir de la fin de cette séquence
            i = j
        else:
            i += 1

    return positions, lengths

def rle(arr : List[int]) -> List[int]:
    mask = arr[1:] != arr[:-1]
    # on crée un mask de meme longueur
    keep = np.zeros(len(arr), dtype=bool)

    keep[0] = True  # le premier élément est toujours gardé
    keep[1:] = mask
    positions, lengths =  count_seq_pos(keep, arr)
            

    return  positions, lengths
```

---

## ✅ Exercice 5 : Masquer les e-mails

```python
emails = np.array(["alice@gmail.com", "bob@yahoo.com"])

def mask_email(email):
    name, domain = email.split('@')
    return '*' * len(name) + '@' + domain

masked = np.vectorize(mask_email)(emails)
print(masked)  # ['*****@gmail.com' '***@yahoo.com']
```

---

## ✅ Exercice 6 : Split avec sommes équilibrées (brute-force pour petits tableaux)

```python
from itertools import combinations
import numpy as np

def best_split(arr):
    total = arr.sum()
    best_diff = float('inf')
    best_pair = ([], [])

    for i in range(1, len(arr)):
        for indices in combinations(range(len(arr)), i):
            left = np.array([arr[j] for j in indices])
            right = np.delete(arr, list(indices))
            diff = abs(left.sum() - right.sum())
            if diff < best_diff:
                best_diff = diff
                best_pair = (left, right)
    return best_pair

arr = np.array([1, 2, 3, 6])
left, right = best_split(arr)
print(left, right)
```

---

## ✅ Exercice 7 : Générateur de codes alphanumériques

```python
import string
import numpy as np

def generate_codes(n, length=6):
    chars = np.array(list(string.ascii_uppercase + string.digits))
    codes = set()
    while len(codes) < n:
        arr = np.random.choice(chars, size=(n*2, length))
        new_codes = {"".join(code) for code in arr}
        codes.update(new_codes)
    return np.array(list(codes)[:n])

print(generate_codes(5))
```

---

## ✅ Exercice 8 : Trouver les doublons

```python
def find_duplicates(arr):
    unique, counts = np.unique(arr, return_counts=True)
    return unique[counts > 1]

ids = np.array([1001, 1002, 1001, 1003, 1002, 1004])
print(find_duplicates(ids))  # [1001 1002]
```
