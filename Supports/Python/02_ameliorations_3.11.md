## ⚡️ Nouveautés clés de Python 3.11

### ✅ 1. **Amélioration des performances**

Python 3.11 est **environ 10 à 60 % plus rapide** que Python 3.10, grâce à la gestion des exceptions dite **"Zero-cost exception handling"** ainsi qu’à des optimisations internes du bytecode.

---

### 🧩 2. **Tracebacks améliorés**

Les messages d’erreur sont maintenant **plus précis**, indiquant :

* la **ligne exacte** dans l’expression,
* des **annotations claires** sur les erreurs.

**Exemple avant vs après :**

```python
# Exemple avec une erreur volontaire
result = 3 + "5"
```

**Avant :** erreur sur toute la ligne

**Python 3.11 :**

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
         -->    result = 3 + "5"
                         ^^^^^^^
```

---

### 🧵 3. **Groupes d’exceptions et `except*`**

Fonctionnalité utile pour **le traitement concurrent ou asynchrone** :

```python
try:
    raise ExceptionGroup("multi-erreurs", [ValueError(), TypeError()])
except* ValueError:
    print("Une ou plusieurs ValueError interceptées")
```

> 🔸 Cela permet de capturer **plusieurs exceptions en parallèle** de manière propre.

---

### 🧠 4. **Améliorations du module `typing`**

Notamment avec :

* `Self` pour annoter les méthodes retournant l’instance courante :

```python
from typing import Self

class MaClasse:
    def reset(self) -> Self:
        ...
```

* `typing.LiteralString` pour sécuriser les fonctions sensibles aux injections (ex. SQL).

---

### 🔄 5. **Intégration native de `tomllib`** (lecture des fichiers `.toml`)

Il est désormais possible de charger des fichiers `.toml` **sans dépendance externe** :

```python
import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)
```

---

### 🔍 6. **Méthodes `str.removeprefix()` et `str.removesuffix()`**

Introduites en 3.9, elles restent très utiles pour le traitement de chaînes de caractères :

```python
"HelloWorld".removeprefix("Hello")  # "World"
```

---

## 🎯 Résumé des points marquants

| Domaine             | Nouveauté                 | Intérêt pratique                            |
| ------------------- | ------------------------- | ------------------------------------------- |
| Performance         | Gain de vitesse           | Scripts, ETL, IA plus rapides               |
| Debugging           | Tracebacks améliorés      | Repérage plus précis des erreurs            |
| Concurrence / async | ExceptionGroup, `except*` | Gestion plus propre avec `asyncio`          |
| Typage              | `Self`, `LiteralString`   | Typage plus sûr et lisible                  |
| Fichiers de config  | `tomllib`                 | Gestion native du `.toml` sans installation |
| Syntaxe             | `match-case`              | Alternative claire et scalable à `if/elif`  |

---

## 📦 À quoi sert un fichier `.toml` ?

Le fichier `.toml` est utilisé pour **définir des paramètres de configuration** dans de nombreux projets Python modernes, notamment :

* `pyproject.toml` → configuration des outils de build (Poetry, Flit, Black, Ruff, etc.)
* Configuration d’applications ou d’outils en ligne de commande

---

## 🧾 Exemple de fichier `.toml`

```toml
[tool.poetry]
name = "mon-projet"
version = "0.1.0"
description = "Un projet Python"
authors = ["Alice <alice@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
numpy = "^1.24"

[tool.poetry.dev-dependencies]
pytest = "^7.2"
```

### Lecture en Python (depuis la version 3.11) :

```python
import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

print(config["tool"]["poetry"]["name"])  # affiche "mon-projet"
```

---

## ✅ Avantages du format TOML

* **Lisibilité accrue** (plus clair que JSON pour la configuration)
* **Support des types natifs** (dates, booléens, tableaux, etc.)
* **Support natif en Python 3.11** via `tomllib` (pas besoin d’installer de paquet externe)

---

Ce format est incontournable pour les projets modernes utilisant Poetry, Black, Ruff, pytest ou d’autres outils récents.
