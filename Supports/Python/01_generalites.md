# Généralités

## 🧠 1. Portée des variables (Scope)

### 🔹 Portée locale vs globale

```python
x = 10  # variable globale

def ma_fonction():
    x = 5  # variable locale
    print("Dans la fonction:", x)

ma_fonction()
print("En dehors de la fonction:", x)
```

### 🔹 `global` et `nonlocal`

```python
def ex1():
    global x
    x = 20

def ex2():
    y = 5
    def inner():
        nonlocal y
        y += 1
        return y
    return inner()

print(ex2())  # y devient 6
```

---

## 🧩 2. Conditions (`if`, `elif`, `else`)

### 🔹 Syntaxe

```python
x = 7

if x > 10:
    print("x est grand")
elif x > 5:
    print("x est moyen")
else:
    print("x est petit")
```

### 🔹 Expressions conditionnelles (ternaire)

```python
age = 17
status = "majeur" if age >= 18 else "mineur"
print(status)
```

---

## 🔁 3. Boucles (`for`, `while`, `break`, `continue`)

### 🔹 Boucle `for`

```python
for i in range(5):  # de 0 à 4
    print(i)
```

### 🔹 Boucle `while`

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

### 🔹 `break` et `continue`

```python
for i in range(10):
    if i == 5:
        break  # stoppe tout
    if i % 2 == 0:
        continue  # saute les pairs
    print(i)
```

---

## 📦 4. Structures de données

### 🔸 Listes (mutable, ordonnées)

```python
fruits = ["pomme", "banane", "kiwi"]
fruits.append("orange")
fruits[1] = "fraise"
print(fruits)
```

### 🔸 Tuples (immutables)

```python
coord = (10, 20)
x, y = coord
```

### 🔸 Dictionnaires (clé-valeur)

```python
user = {"nom": "Alice", "âge": 25}
user["ville"] = "Paris"
print(user["nom"])
```

### 🔸 Ensembles (non ordonnés, uniques)

```python
nums = {1, 2, 3, 3, 2}
nums.add(4)
print(nums)  # {1, 2, 3, 4}
```

---

## 🛠️ BONUS : Compréhensions

```python
carrés = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
pairs = [x for x in range(10) if x % 2 == 0]
```

---

## ⚙️ Version Python 3.11 : nouveautés utiles (en résumé)

* **`match-case`** (pattern matching) pour remplacer `if/elif`

```python
def jour(j):
    match j:
        case 1:
            return "Lundi"
        case 2:
            return "Mardi"
        case _:
            return "Autre jour"
```

---

## Le slicing (tranchage) en Python

Le slicing permet d'extraire une **sous-partie** d'une séquence (liste, tableau, chaîne…) en utilisant la notation :

```python
sequence[start:stop:step]
```

* **start** : indice de début (inclusif), par défaut `0`
* **stop** : indice de fin (exclusif), par défaut la fin de la séquence
* **step** : pas d'incrément, par défaut `1`

---

### Exemples

```python
arr = np.array([10, 20, 30, 40, 50, 60])
```

* `arr[1:4]` → éléments aux indices 1 à 3 : `[20, 30, 40]`
* `arr[:3]` → du début à l'indice 2 : `[10, 20, 30]`
* `arr[3:]` → de l'indice 3 jusqu'à la fin : `[40, 50, 60]`
* `arr[::2]` → tous les 2 éléments (pas = 2) : `[10, 30, 50]`
* `arr[::-1]` → inverse le tableau : `[60, 50, 40, 30, 20, 10]`

---

### Particularités avec NumPy

* Le slicing retourne une **vue mémoire**, pas une copie. Modifier le slice modifie l'original.
* On peut slicer sur plusieurs dimensions : `arr[1:3, 2:5]` (2D).
* On peut utiliser des indices négatifs : `arr[-3:]` (les 3 derniers éléments).

---

### Conseils pratiques

* `start` inclus, `stop` exclu → ça veut dire que le slice s'arrête juste avant `stop`.
* Attention aux erreurs de `IndexError` si on sort des bornes, mais en slicing Python, on est généralement toléré (ex: `arr[2:100]` ne pose pas problème même si 100 est hors borne).
* Pour manipuler des fenêtres glissantes, on peut combiner slicing et boucles, ou utiliser `sliding_window_view` en NumPy.

---