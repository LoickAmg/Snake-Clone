"""Logique pure du serpent (sans dépendance à pygame) -> facilement testable."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def opposite(self) -> "Direction":
        dx, dy = self.value
        return Direction((-dx, -dy))


Point = tuple[int, int]


@dataclass
class Snake:
    grid_width: int
    grid_height: int
    body: list[Point] = field(default_factory=list)
    direction: Direction = Direction.RIGHT
    grow_pending: int = 0

    def __post_init__(self) -> None:
        if not self.body:
            cx, cy = self.grid_width // 2, self.grid_height // 2
            self.body = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]

    @property
    def head(self) -> Point:
        return self.body[0]

    def set_direction(self, new_direction: Direction) -> None:
        """Ignore les demi-tours sur soi-même (fait aussi mourir le jeu sinon)."""
        if new_direction.opposite == self.direction and len(self.body) > 1:
            return
        self.direction = new_direction

    def next_head(self) -> Point:
        dx, dy = self.direction.value
        hx, hy = self.head
        return (hx + dx, hy + dy)

    def grow(self, amount: int = 1) -> None:
        self.grow_pending += amount

    def move(self) -> Point:
        """Avance le serpent d'une case et renvoie la nouvelle position de tête."""
        new_head = self.next_head()
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
        return new_head

    def collides_with_wall(self) -> bool:
        hx, hy = self.head
        return not (0 <= hx < self.grid_width and 0 <= hy < self.grid_height)

    def collides_with_self(self) -> bool:
        return self.head in self.body[1:]

    def is_dead(self) -> bool:
        return self.collides_with_wall() or self.collides_with_self()

    def occupies(self, point: Point) -> bool:
        return point in self.body
