### Exo 1 — Somme des entiers pairs

**Énoncé :**
Écrire une fonction `sum_even(n: int) -> int` qui calcule la somme des nombres pairs de 0 à n inclus.

```python
def sum_even(n: int) -> int:
    pass

print(sum_even(10))  # 30 (0+2+4+6+8+10)
```

---

### Exo 2 — Inversion d’une chaîne

**Énoncé :**
Écrire une fonction `reverse_string(s: str) -> str` qui retourne la chaîne `s` inversée.

```python
def reverse_string(s: str) -> str:
    pass

print(reverse_string("python"))  # nohtyp
```

---

### Exo 3 — Recherche d’un élément dans une liste

**Énoncé :**
1. Écrire une fonction `contains(lst: list, val) -> bool` qui renvoie `True` si `val` est dans `lst`, sinon `False`.

2. Écrire une fonction `contains(lst: list, val) -> bool` qui renvoie `True` si `une liste de données` est dans `liste de liste`, sinon `False`.


```python
def contains(lst: list, val) -> bool:
    pass

print(contains([1, 3, 5], 3))  # True
print(contains([1, 3, 5], 2))  # False

def contains_seq(data: list, seq : list) -> bool:
   pass
```

---

# 02\_ameliorations\_3.11.md

---

### Exo 4 — Utiliser `match` pour classifier un animal

**Énoncé :**
Écrire une fonction `classify_animal(animal: str) -> str` qui renvoie `"mammifère"`, `"oiseau"`, ou `"inconnu"` selon `animal`, en utilisant `match-case`.

```python
def classify_animal(animal: str) -> str:
    pass

print(classify_animal("chat"))  # mammifère
print(classify_animal("canard"))  # oiseau
print(classify_animal("poisson"))  # inconnu
```

---

### Exo 5 — Extraction d’éléments avec `match`

**Énoncé :**
Écrire une fonction `extract_point(data: tuple) -> str` qui renvoie `"Point 2D"` si `data` est `(x, y)`, `"Point 3D"` si `(x, y, z)`, sinon `"Autre"`.

```python
def extract_point(data: tuple) -> str:
    pass

print(extract_point((1, 2)))        # Point 2D
print(extract_point((1, 2, 3)))     # Point 3D
print(extract_point((1, 2, 3, 4)))  # Autre
```

---

# 04\_objet.md

---

### Exo 6 — Classe simple `Person`

**Énoncé :**
Créer une classe `Person` avec un attribut `name` et une méthode `greet()` qui retourne `"Bonjour, je suis {name}"`.

```python
class Person:
    pass

p = Person("Alice")
print(p.greet())  # Bonjour, je suis Alice
```

---

### Exo 7 — Classe `Rectangle` avec méthode surface

**Énoncé :**
Créer une classe `Rectangle` avec `width` et `height` en attributs, et une méthode `area()` qui retourne l’aire.

```python
class Rectangle:
    pass

rect = Rectangle(3, 4)
print(rect.area())  # 12
```

---

### Exo 8 — Méthode de classe pour un carré

**Énoncé :**
Ajouter une méthode de classe `square(cls, side)` à `Rectangle` qui crée un rectangle carré.

```python
class Rectangle:
   pass

sq = Rectangle.square(5)
print(sq.area())  # 25
```

---

# 05\_files.md

---

### Exo 9 — Écrire une liste dans un fichier

**Énoncé :**
Écrire une fonction `write_list(filename: str, items: list)` qui écrit chaque élément de `items` sur une ligne dans un fichier.

```python
def write_list(filename: str, items: list):
  pass

write_list("fruits.txt", ["pomme", "banane", "cerise"])
```

---

### Exo 10 — Lire un fichier et compter les lignes

**Énoncé :**
Écrire une fonction `count_lines(filename: str) -> int` qui retourne le nombre de lignes dans un fichier.

```python
def count_lines(filename: str) -> int:
    pass

print(count_lines("fruits.txt"))  # 3
```
