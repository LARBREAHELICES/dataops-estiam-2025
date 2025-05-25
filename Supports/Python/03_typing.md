# Introduction au Typing en Python

Le **typing** en Python permet d'annoter explicitement les types des variables, paramètres de fonctions et valeurs de retour. Cette pratique n'est pas obligatoire, car Python reste un langage dynamique, mais elle apporte plusieurs avantages :

* **Meilleure lisibilité** du code, en explicitant les attentes sur les types,
* **Détection précoce d'erreurs** grâce à des outils externes,
* **Meilleure complétion et analyse** dans les environnements de développement (IDE),
* **Facilitation de la maintenance** et de la compréhension du code sur le long terme.

### Exemple simple d'annotations de types :

```python
def addition(a: int, b: int) -> int:
    return a + b

nom: str = "Alice"
age: int = 30
```

---

## Comment vérifier les annotations de types en développement ?

Python ne fait pas de vérification des types à l'exécution. Cependant, il existe des outils spécialisés qui permettent d'analyser le code source **statistiquement** (sans exécuter le programme) pour détecter les incohérences de type :

* **mypy** : l'outil le plus populaire pour effectuer la vérification statique du typage Python.
* **Pyright** : un autre vérificateur de types rapide, souvent intégré dans VSCode.
* **Pylance** : extension VSCode qui utilise Pyright pour l'analyse de type.

### Utilisation basique de `mypy` :

```bash
mypy mon_script.py
```

Cela affichera les erreurs de type détectées dans le fichier.

---

## Résumé

* Le typing améliore la robustesse et la clarté du code.
* Les annotations sont facultatives mais recommandées dans les projets moyens à grands.
* La vérification est réalisée **hors exécution**, grâce à des outils comme `mypy`.
* L'IDE peut également fournir un retour instantané sur les erreurs de type.

---

Voici un exemple complet d'utilisation du typing en Python, avec un petit script, ses annotations, et la manière de vérifier les types avec `mypy`.

---

## Exemple complet avec typing et vérification

### 1. Script Python annoté (`exemple_typing.py`)

```python
from typing import List, Optional

def moyenne(notes: List[float]) -> Optional[float]:
    """
    Calcule la moyenne d'une liste de notes.
    Retourne None si la liste est vide.
    """
    if not notes:
        return None
    return sum(notes) / len(notes)

def presentation(nom: str, age: int) -> str:
    return f"Bonjour, je m'appelle {nom} et j'ai {age} ans."

# Exemple d'utilisation
notes = [12.5, 15.0, 14.0]
print("Moyenne :", moyenne(notes))

print(presentation("Alice", 30))
```

---

### 2. Vérification des types avec mypy

* Installer mypy si ce n'est pas déjà fait :

```bash
pip install mypy
```

* Lancer la vérification :

```bash
mypy exemple_typing.py
```

* Résultat attendu :

```
Success: no issues found in 1 source file
```

---

### 3. Que se passe-t-il en cas d'erreur de type ?

Modifiez par exemple la dernière ligne pour y passer un entier au lieu d'une chaîne pour `nom` :

```python
print(presentation(123, 30))
```

Puis relancez `mypy` :

```bash
mypy exemple_typing.py
```

Vous aurez une erreur :

```
example_typing.py:17: error: Argument 1 to "presentation" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

---

## Conclusion

Avec ce workflow, on écrit du code Python clair, robuste, facile à maintenir, et on détecte rapidement les erreurs potentielles de typage **avant l'exécution**.

Vous pouvez également installer un plugin, comme `Pyright`, dans **vscode** pour avoir les erreurs de type directement souligné dans le code, pratique si l'on ne souhaite pas utiliser un module supplémentaire.
