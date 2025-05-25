# Cours avancé : Classes en Python — méthodes statiques et métaclasses

---

## 1. Rappel rapide : classes et objets

* Une **classe** est un plan de fabrication d'objets (instances).
* Une **instance** est un objet créé à partir d'une classe.
* Une **métaclasse** est une classe qui crée des classes.

---

## 2. Méthodes statiques (`@staticmethod`)

### Qu'est-ce qu'une méthode statique ?

* C'est une méthode attachée à la classe, mais qui **ne dépend ni de l'instance ni de la classe** (pas d'accès à `self` ni `cls`).
* Utilisée pour regrouper des fonctions liées à la classe, mais qui ne modifient ni l'état de la classe ni celui des instances.

### Exemple simple :

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(3, 5))  # 8
```

* Ici, `add` ne reçoit ni `self` ni `cls`, elle est indépendante de toute instance ou état de classe.
* On peut appeler `MathUtils.add()` directement, sans créer d'objet.

---

### Différences avec :

| Méthode normale                          | Méthode de classe (`@classmethod`)          | Méthode statique (`@staticmethod`)          |
| ---------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Reçoit `self` (instance)                 | Reçoit `cls` (classe)                       | Ne reçoit ni `self` ni `cls`                |
| Modifie/accède aux données de l'instance | Modifie/accède aux données de la classe     | Utilitaire indépendant                      |
| Nécessite une instance                   | Peut être appelée sur la classe ou instance | Peut être appelée sur la classe ou instance |

---

### Exemple complet pour voir la différence :

```python
class Demo:
    class_var = 10
    
    def instance_method(self):
        print(f"Instance method called, self={self}")

    @classmethod
    def class_method(cls):
        print(f"Class method called, cls={cls}, class_var={cls.class_var}")

    @staticmethod
    def static_method():
        print("Static method called, no self or cls")

d = Demo()
d.instance_method()  # Instance method called, self=<Demo instance>
Demo.class_method()  # Class method called, cls=<class Demo>, class_var=10
Demo.static_method() # Static method called, no self or cls
```

---

## 3. Métaclasses — approfondissement

### Rappel

* Métaclasse = classe qui crée des classes.
* Par défaut, toutes les classes en Python sont créées par la métaclasse `type`.

### Comment ça marche concrètement ?

Quand tu écris :

```python
class MyClass:
    pass
```

Python fait :

```python
MyClass = type('MyClass', (), {})
```

Ici, `type` est la métaclasse qui crée `MyClass`.

---

### 3.1. Créer sa propre métaclasse

On hérite de `type` et on redéfinit la méthode `__new__` (ou `__init__`), qui est appelée **au moment de la création de la classe**.

---

### Méthode `__new__` d'une métaclasse

Signature :

```python
def __new__(cls, name, bases, dct):
    # cls = la métaclasse
    # name = nom de la classe à créer
    # bases = classes parentes (tuple)
    # dct = dict des attributs/méthodes
    # retourner la classe créée
```

---

### Exemple : ajouter un attribut automatique

```python
class AutoAttrMeta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'AutoAttrMeta'
        return super().__new__(cls, name, bases, dct)

class User(metaclass=AutoAttrMeta):
    pass

print(User.created_by)  # AutoAttrMeta
```

---

### 3.2. Contrôler la définition d'une classe (exemple obligatoire)

```python
class MustHaveMethodMeta(type):
    def __new__(cls, name, bases, dct):
        if 'hello' not in dct:
            raise TypeError(f"Class {name} must define a hello() method")
        return super().__new__(cls, name, bases, dct)

class Correct(metaclass=MustHaveMethodMeta):
    def hello(self):
        print("Hello!")

# class Wrong(metaclass=MustHaveMethodMeta):
#     pass  # Provoque une erreur TypeError
```

---

### 3.3. Utilité réelle des métaclasses

* **Frameworks** : Django, SQLAlchemy utilisent des métaclasses pour enregistrer automatiquement des modèles, vérifier les définitions, générer du code.
* **Validation automatique** des classes.
* **Création d'API dynamiques** (par exemple, ajout automatique de méthodes).
* **Singleton, design patterns avancés**.

---

## 4. Résumé et bonne pratique

| Concept             | Rôle                                   | Utilisation typique                                              |
| ------------------- | -------------------------------------- | ---------------------------------------------------------------- |
| `@staticmethod`     | Fonction liée à la classe sans état    | Méthode utilitaire, calcul sans contexte                         |
| `@classmethod`      | Méthode liée à la classe               | Usine de création, accès/modif classe                            |
| Métaclasse (`type`) | Crée la classe, contrôle sa définition | Personnalisation de la création de classe, framework, validation |

---

## 5. Bonus : Exemple combiné

```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        dct['category'] = 'MetaClass Example'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    @staticmethod
    def greet():
        print("Hello from static method!")

MyClass.greet()                  # Hello from static method!
print(MyClass.category)          # MetaClass Example
```

---

## Remarques sur cls à ne pas confondre avec self

* Sans `@classmethod`, une méthode est **méthode d'instance**, elle attend un objet (une instance) en premier argument (`self`).
* Avec `@classmethod`, la méthode reçoit la classe en premier argument (`cls`), pas une instance.

---

### Exemple sans `@classmethod` :

```python
class Test:
    def foo(cls):
        print(cls)

Test.foo()  # Erreur car on n'a pas passé d'instance, et la méthode attend un argument.
```

---

### Exemple avec `@classmethod` :

```python
class Test:
    @classmethod
    def foo(cls):
        print(cls)

Test.foo()  # Affiche <class '__main__.Test'>
```

---

### En résumé

* `@classmethod` **indique à Python** que la méthode est appelée sur la classe et doit recevoir la classe en premier paramètre.
* Sans ce décorateur, la méthode est appelée sur une instance et reçoit l'instance (`self`) en premier paramètre.

---