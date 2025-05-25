# 🎢 Pourquoi c’est "drôle" mais utile de glisser ainsi ?

Tu peux voir ça comme :

* **Un filtre mobile** : à chaque pas, tu "regardes" un petit groupe de valeurs proches (ex : jours voisins), puis tu avances d’un cran.
* **Une loupe** que tu déplaces sur les données pour voir la tendance locale.
* Une façon de **suivre l’évolution sans se laisser tromper par un seul pic ou une seule chute**.

---

### 🔍 Petite analogie :

Imagine un élève qui a les notes suivantes :

```
10, 12, 15, 9, 8, 14, 13, 16
```

Plutôt que de juger la progression avec chaque note isolée (trop bruité), on regarde la **moyenne glissante sur 3 contrôles** :

* (10 + 12 + 15) / 3 → 12.33
* (12 + 15 + 9) / 3 → 12.00
* (15 + 9 + 8) / 3 → 10.67
  etc.

➡️ On voit que la moyenne glissante **baisse**, ce qui alerte peut-être un prof, même si certaines notes sont bonnes.

---
