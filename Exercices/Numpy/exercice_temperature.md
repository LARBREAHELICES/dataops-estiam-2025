## Exercice température

Nous avons relevé des températures au mois de Janvier. Répondez aux questions suivantes :

- 1. **Donnez toutes les températures qui sont supérieures à 0.**

- 2. **Comparez les températures supérieures et inférieures à 0.**

- 3. **Donnez le pourcentage des températures positives sur le mois.**

- 4. **Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.**

— 5. **Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.**

— 6. **Remplacez maintenant les températures négatives par la moyenne des températures positives.**


```python
january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2])
```

```python
import numpy as np 

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2], dtype='float64')

```

- 1. Donnez toutes les températures qui sont supérieures à 0.


- 2. Comparez les températures supérieures et inférieures à 0.


- 3. Donnez le pourcentage des températures positives sur le mois.


- 4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.

- 5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.


# start:end:step


6. Remplacez maintenant les températures négatives par la moyenne des températures positives."

### Exercices suites des questions

```python
import numpy as np

# Re-déclaration du tableau (avant remplacement des négatifs si besoin)
january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2], dtype='float64')

days = np.arange(1, len(january) + 1)
```

7. **Quelle est la température maximale relevée et quel jour a-t-elle été observée ?**

8. **Calculez l’écart-type des températures du mois. Que pouvez-vous en conclure sur la variation des températures ?**

9. **Donnez le nombre de jours où la température était exactement de 0 degré.**

10. **Affichez un tableau indiquant pour chaque jour si la température était "négative", "neutre" (0) ou "positive".**

11. **Affichez les 5 jours consécutifs les plus chauds (moyenne maximale sur une fenêtre glissante de 5 jours).**

12. **Créez un tableau contenant les différences de température d’un jour à l’autre.**

13. **Affichez les jours où la température a augmenté par rapport à la veille.**

14. **Créez un tableau binaire indiquant 1 si la température du jour est supérieure à celle de la veille, sinon 0.**

15. **Affichez les températures triées par ordre croissant et associez-les aux jours correspondants.**

16. **Faites une moyenne glissante (moving average) sur 3 jours et affichez-la pour le mois.**
