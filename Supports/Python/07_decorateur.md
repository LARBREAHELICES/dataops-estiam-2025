# Les décorateurs en Python

## 1. Qu’est-ce qu’un décorateur ?

Un **décorateur** est une fonction qui **prend une autre fonction en argument**, la modifie ou l’enrichit, puis retourne une nouvelle fonction.
C’est un moyen propre et puissant d’ajouter du comportement à des fonctions ou méthodes sans toucher à leur code.

---

## 2. Pourquoi utiliser des décorateurs ?

* Ajouter un comportement avant ou après une fonction (ex : logging, vérification d’accès, chronométrage).
* Réutiliser du code commun à plusieurs fonctions.
* Garder un code propre et éviter la duplication.

---

## 3. Syntaxe de base

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Code à exécuter avant la fonction
        print("Before the function call")
        
        result = func(*args, **kwargs)  # Appel de la fonction originale
        
        # Code à exécuter après la fonction
        print("After the function call")
        
        return result
    return wrapper
```

---

## 4. Utiliser un décorateur avec `@`

```python
@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

Equivalent à :

```python
def say_hello(name):
    print(f"Hello, {name}!")

say_hello = decorator(say_hello)
say_hello("Alice")
```

---

## 5. Exemple complet

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Bob"))  # Affiche "HELLO, BOB"
```

---

## 6. Décorateurs avec arguments

Si vous voulez passer des arguments à un décorateur, vous devez imbriquer les fonctions :

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# Hello!
# Hello!
# Hello!
```

---

## 7. Décorateurs intégrés utiles en Python

* `@staticmethod` : méthode statique, pas besoin d’instance.
* `@classmethod` : méthode de classe, reçoit la classe comme premier argument.
* `@property` : méthode accessible comme un attribut (getter).

---

## 8. Décorateurs avancés

### Préserver le nom et la docstring

Utilisez `functools.wraps` pour que la fonction décorée conserve son nom et sa docstring d’origine.

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## 9. En résumé

* Un décorateur modifie ou enrichit une fonction ou méthode.
* S’écrit souvent sous la forme `@decorator` juste avant la définition d’une fonction.
* Permet d’éviter la répétition et de séparer les préoccupations (ex : log, contrôle, timing).
* Peut prendre des arguments si nécessaire, mais la syntaxe devient alors une fonction retournant un décorateur.

---