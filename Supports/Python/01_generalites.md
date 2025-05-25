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