"""Placement de la nourriture sur la grille."""

from __future__ import annotations

import random
from dataclasses import dataclass

from .snake import Point, Snake


@dataclass
class Food:
    grid_width: int
    grid_height: int
    position: Point = (0, 0)

    def __post_init__(self) -> None:
        self.respawn(Snake(self.grid_width, self.grid_height, body=[]))

    def respawn(self, snake: Snake) -> Point:
        """Replace la nourriture sur une case libre (hors corps du serpent)."""
        free_cells = [
            (x, y)
            for x in range(self.grid_width)
            for y in range(self.grid_height)
            if (x, y) not in snake.body
        ]
        self.position = random.choice(free_cells) if free_cells else self.position
        return self.position
