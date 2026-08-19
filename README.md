# Snake Clone

Projet 14 de la roadmap "40 projets" — Niveau 1 (Fondamentaux, Scripts & Logique de base).

Un clone de Snake en Python/Pygame, avec une logique de jeu séparée du rendu (facile à tester unitairement) et une CI GitHub Actions qui lint + teste à chaque push.

## Fonctionnalités

- Grille configurable, vitesse qui augmente avec le score
- Déplacement au clavier (flèches ou ZQSD/WASD)
- Détection de collision (murs + corps du serpent)
- Écran de game over avec relance (`R`) sans quitter le jeu
- Logique du serpent et de la nourriture 100% testable sans fenêtre graphique

## Structure du projet

```
snake-clone/
├── src/
│   ├── main.py        # point d'entrée
│   ├── game.py         # boucle de jeu et rendu pygame
│   ├── snake.py         # logique pure du serpent (testable)
│   ├── food.py           # placement de la nourriture
│   └── settings.py        # constantes (taille grille, couleurs, FPS...)
├── tests/
│   └── test_snake.py       # tests unitaires (pytest)
├── .github/workflows/ci.yml # lint (ruff) + tests (pytest) sur push/PR
├── requirements.txt
└── requirements-dev.txt
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
pip install -r requirements-dev.txt
```

> **Note Python 3.14** : le projet utilise `pygame-ce` (fork communautaire, drop-in
> compatible, `import pygame` inchangé) plutôt que `pygame` classique, car ce dernier
> ne fournit pas encore de wheel précompilée pour Python 3.14 sur Windows (il tente
> de compiler depuis les sources et échoue avec `distutils` retiré du langage).
> `pygame-ce` fournit des wheels cp314 prêtes à l'emploi.

## Lancer le jeu

```bash
python -m src.main
```

Commandes : flèches directionnelles ou `Z`/`Q`/`S`/`D` (ou `W`/`A`/`S`/`D`) pour diriger le serpent, `R` pour rejouer après un game over, `Échap` pour quitter.

## Lancer les tests

```bash
pytest
```

## Lint

```bash
ruff check .
```

## Prochaines étapes possibles

- Ajouter un mode "murs traversants" (le serpent réapparaît de l'autre côté)
- Sauvegarder le meilleur score localement
- Conteneuriser avec Docker (voir le projet transversal #25 de la roadmap)
# Snake-Clone
