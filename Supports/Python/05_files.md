# Cours sur la gestion des fichiers en Python

Python offre des fonctionnalités simples et puissantes pour lire, écrire et manipuler des fichiers. Voici les notions clés à connaître.

---

## 1. Ouvrir un fichier

Pour travailler avec un fichier, il faut d'abord l'ouvrir avec la fonction `open()` :

```python
file = open("nom_fichier.txt", mode)
```

* `"nom_fichier.txt"` : chemin ou nom du fichier
* `mode` : mode d'ouverture (lecture, écriture, etc.)

Modes courants :

* `"r"` : lecture (par défaut)
* `"w"` : écriture (écrase le fichier existant)
* `"a"` : ajout à la fin du fichier
* `"b"` : mode binaire (ex : `"rb"`, `"wb"`)
* `"x"` : création, échoue si le fichier existe

---

## 2. Lire un fichier

Pour lire le contenu :

```python
with open("fichier.txt", "r") as file:
    content = file.read()  # lit tout le fichier en une chaîne
    print(content)
```

On peut aussi lire ligne par ligne :

```python
with open("fichier.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() enlève les retours à la ligne
```

---

## 3. Écrire dans un fichier

Pour écrire (ou réécrire) un fichier :

```python
with open("fichier.txt", "w") as file:
    file.write("Bonjour, monde!\n")
    file.write("Nouvelle ligne.\n")
```

Pour ajouter du contenu sans écraser :

```python
with open("fichier.txt", "a") as file:
    file.write("Texte ajouté à la fin.\n")
```

---

## 4. Le mot-clé `with`

Le plus sûr est d’ouvrir un fichier avec `with` :

```python
with open(...) as file:
    # traitement
```

Cela garantit la fermeture automatique du fichier même en cas d’erreur, évitant les fuites de ressources.

---

## 5. Travailler avec des fichiers CSV

Pour manipuler des fichiers CSV, on peut utiliser le module `csv` de Python :

```python
import csv

# Lire un CSV
with open("data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Écrire un CSV
with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["nom", "âge", "ville"])
    writer.writerow(["Alice", 30, "Paris"])
```

---

## 6. Fichiers JSON

Pour lire et écrire des fichiers JSON, on utilise le module `json` :

```python
import json

# Lire JSON
with open("data.json") as f:
    data = json.load(f)
print(data)

# Écrire JSON
data = {"nom": "Alice", "âge": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

---

## 7. Autres conseils

* Pour manipuler les chemins de fichiers de manière portable, utilisez le module `pathlib` (Python 3.4+) :

```python
from pathlib import Path

path = Path("mon_dossier") / "fichier.txt"
with path.open("r") as f:
    content = f.read()
```

* Toujours fermer les fichiers après usage (automatique avec `with`).

* Gérer les exceptions peut être utile pour capturer les erreurs d'ouverture ou lecture :

```python
try:
    with open("fichier.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Fichier non trouvé !")
```
