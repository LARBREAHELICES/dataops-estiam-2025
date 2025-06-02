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

<details>
<summary>🧠 Cliquez ici pour afficher/masquer la correction</summary>

```python
import numpy as np 

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2], dtype='float64')

print( "1. Donnez toutes les températures qui sont supérieures à 0.")

print( january[january > 0] )

print("2. Comparez les températures supérieures et inférieures à 0.")

print( sum(january > 0 ) > sum(january <= 0 )   )

print("3. Donnez le pourcentage des températures positives sur le mois.")

print( f" { round( ( sum( january > 0 )  / len(january) ) * 100 , 2 ) } % " )

print("4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.")

days = np.array( range(1, len(january) + 1))
# print(days)
print(days[january > 0])

print( "5. Donnez toutes les températures supérieures à 0 à partir du dixième jour du mois.")
# start:end:step
print( january[9:] [ january[9:] > 0 ] )

# rappels slicing
l = [1, 2, 3, 4, 5, 6]
# à partir de l'indice 3 jusqu'à la fin
print(l[3:])
# par step de 2
print(l[3::2])

print( "6. Remplacez maintenant les températures négatives par la moyenne des températures positives." )

average_positif =  round ( sum ( january[(january > 0)] ) / len(january), 2 )
print(average_positif)
january[ january < 0] = average_positif

print(january)

```

</details>
---

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


<details>
<summary>🧠 Cliquez ici pour afficher/masquer la correction</summary>
### Corrections

```python

print("7. Température maximale et jour correspondant")
max_temp = january.max()
day_max = days[january.argmax()]
print(f"Max: {max_temp}° le jour {day_max}")

print("\n8. Écart-type des températures")
std_temp = np.round(np.std(january), 2)
print(f"Écart-type : {std_temp}°")

print("\n9. Nombre de jours avec température exactement 0°")
zero_days = np.sum(january == 0)
print(f"{zero_days} jours avec exactement 0°")

print("\n10. Tableau des états : négatif, neutre ou positif")
etat = np.where(january < 0, "négative", np.where(january == 0, "neutre", "positive"))
print(etat)

print("\n11. Moyenne glissante maximale sur 5 jours")
# Utilisation d'une convolution avec une fenêtre de taille 5
window_size = 5
rolling_means = np.convolve(january, np.ones(window_size)/window_size, mode='valid')
max_window_idx = np.argmax(rolling_means)
print(f"Du jour {max_window_idx + 1} au jour {max_window_idx + window_size} avec moyenne {round(rolling_means[max_window_idx], 2)}°")

print("\n12. Différences de température d’un jour à l’autre")
diffs = np.diff(january)
print(diffs)

print("\n13. Jours où la température a augmenté par rapport à la veille")
up_days = days[1:][diffs > 0]
print(up_days)

print("\n14. Tableau binaire (1 si la température monte, sinon 0)")
binary_change = (diffs > 0).astype(int)
print(binary_change)

print("\n15. Températures triées par ordre croissant avec jours correspondants")
sorted_indices = np.argsort(january)
print("Températures triées :", january[sorted_indices])
print("Jours correspondants :", days[sorted_indices])

print("\n16. Moyenne glissante sur 3 jours")
rolling_means_3 = np.convolve(january, np.ones(3)/3, mode='valid')
print(rolling_means_3)
```
</details>