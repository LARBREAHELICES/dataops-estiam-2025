# 🐍 Cours synthétique et complet sur l’objet en Python

---

## 1. Qu’est-ce qu’un objet ?

Un **objet** est une **instance** d’une **classe**. En Python, tout est objet : nombres, chaînes de caractères, fonctions, classes, etc.
Un objet regroupe des **données** (appelées *attributs*) et des **fonctions** (appelées *méthodes*) qui opèrent sur ces données.

---

## 2. Classe et instance

* **Classe** : modèle ou plan qui définit la structure et le comportement d’un objet.
* **Instance** : objet concret créé à partir d’une classe.

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("Alice", 30)
p.introduce()  # Hello, my name is Alice and I am 30 years old.
```

---

## 3. Les attributs

* **Attributs d’instance** : propres à chaque objet, définis dans `__init__` avec `self`.
* **Attributs de classe** : partagés par toutes les instances.

```python
class Car:
    wheels = 4  # class attribute

    def __init__(self, brand):
        self.brand = brand  # instance attribute

c1 = Car("Toyota")
c2 = Car("Tesla")

print(c1.wheels)  # 4
print(c2.wheels)  # 4
```

---

## 4. Les méthodes

* Fonctions définies dans une classe.
* Le premier paramètre est toujours `self`, qui fait référence à l’instance.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print(c.count)  # 1
```

---

## 5. Encapsulation

* Utiliser un underscore `_` avant le nom d’un attribut pour indiquer qu’il est protégé (convention).
* Utiliser deux underscores `__` pour rendre l’attribut privé via le name mangling.

```python
class Example:
    def __init__(self):
        self._protected = 42
        self.__num1 = 99
        self.__num2 = .0001

e = Example()

try:
    print(e__num1)
except:
    print("attribute error")

print(e._Example__num1)   # 99 (accès via name mangling)
print(e._Example__num2)   # .0001 (accès via name mangling)

## Voir avec l'héritage chapitre suivant mais noté 
class Parent:
    def __init__(self):
        self.__private = "secret"

class Child(Parent):
    def reveal(self):
        # print(self.__private)  # Cela provoquera une erreur
        print(self._Parent__private)  # Accès possible via le nom manglé
```

---

## 6. Héritage

* Permet de créer une classe basée sur une autre, héritant de ses attributs et méthodes.

```python
class Animal:
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

d = Dog()
d.speak()  # Woof
```

---

## 7. Polymorphisme

* Une même méthode peut avoir un comportement différent selon la classe.

```python
class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
# Woof
# Meow
```

---

## 8. Méthodes spéciales (magiques)

* Méthodes encadrées par double underscore comme `__init__`, `__str__`, `__repr__`.
* Permettent de définir des comportements natifs des objets.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 5)
print(p)  # (3, 5)
```

---

## 9. Résumé rapide

| Concept           | Description                      | Exemple                      |
| ----------------- | -------------------------------- | ---------------------------- |
| Classe            | Modèle / plan                    | `class Car:`                 |
| Instance          | Objet concret                    | `c = Car()`                  |
| Attribut          | Donnée dans un objet             | `self.color = "red"`         |
| Méthode           | Fonction dans un objet           | `def start(self):`           |
| Héritage          | Classe enfant dérivée de parent  | `class Dog(Animal):`         |
| Polymorphisme     | Même méthode, comportement diff. | `speak()` dans `Dog` & `Cat` |
| Encapsulation     | Protection des attributs         | `_protected`, `__private`    |
| Méthodes magiques | `__init__`, `__str__`, etc.      | `def __str__(self):`         |

---
