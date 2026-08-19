"""Tests unitaires de la logique pure (pas de dépendance à pygame)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.snake import Direction, Snake  # noqa: E402


def test_initial_body_length():
    snake = Snake(grid_width=10, grid_height=10)
    assert len(snake.body) == 3


def test_move_advances_head_without_growing():
    snake = Snake(grid_width=10, grid_height=10)
    initial_len = len(snake.body)
    snake.move()
    assert len(snake.body) == initial_len


def test_grow_increases_length_on_next_move():
    snake = Snake(grid_width=10, grid_height=10)
    initial_len = len(snake.body)
    snake.grow(1)
    snake.move()
    assert len(snake.body) == initial_len + 1


def test_cannot_reverse_into_itself():
    snake = Snake(grid_width=10, grid_height=10, direction=Direction.RIGHT)
    snake.set_direction(Direction.LEFT)
    assert snake.direction == Direction.RIGHT


def test_wall_collision_detected():
    snake = Snake(
        grid_width=5,
        grid_height=5,
        body=[(4, 2), (3, 2), (2, 2)],
        direction=Direction.RIGHT,
    )
    snake.move()
    assert snake.collides_with_wall()
    assert snake.is_dead()


def test_self_collision_detected():
    # Serpent replié sur lui-même : la tête va percuter le corps au prochain déplacement.
    snake = Snake(
        grid_width=10,
        grid_height=10,
        body=[(5, 5), (6, 5), (6, 6), (5, 6), (4, 6), (4, 5)],
        direction=Direction.DOWN,
    )
    snake.move()
    assert snake.collides_with_self()
    assert snake.is_dead()


def test_food_respawns_outside_snake_body():
    from src.food import Food

    snake = Snake(grid_width=4, grid_height=1, body=[(0, 0), (1, 0), (2, 0)])
    food = Food(grid_width=4, grid_height=1)
    food.respawn(snake)
    assert food.position == (3, 0)
