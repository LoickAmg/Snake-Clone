"""Boucle de jeu et rendu pygame."""

from __future__ import annotations

import sys
from pathlib import Path

import pygame

from .food import Food
from .high_score import HighScoreStore
from .settings import (
    CELL_SIZE,
    COLOR_BG,
    COLOR_FOOD,
    COLOR_GRID,
    COLOR_SNAKE_BODY,
    COLOR_SNAKE_HEAD,
    COLOR_TEXT,
    FONT_NAME,
    FPS_MAX,
    FPS_START,
    FPS_STEP_EVERY,
    GRID_HEIGHT,
    GRID_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from .snake import Direction, Snake

KEY_TO_DIRECTION = {
    pygame.K_UP: Direction.UP,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_RIGHT: Direction.RIGHT,
    pygame.K_w: Direction.UP,
    pygame.K_s: Direction.DOWN,
    pygame.K_a: Direction.LEFT,
    pygame.K_d: Direction.RIGHT,
}


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_NAME, 24)
        self.high_score_store = HighScoreStore(Path.home() / ".snake-clone" / "high-score.json")
        self.best_score = self.high_score_store.load()
        self.reset()

    def reset(self) -> None:
        self.snake = Snake(GRID_WIDTH, GRID_HEIGHT)
        self.food = Food(GRID_WIDTH, GRID_HEIGHT)
        self.food.respawn(self.snake)
        self.score = 0
        self.game_over = False

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_TO_DIRECTION:
                    self.snake.set_direction(KEY_TO_DIRECTION[event.key])
                elif event.key == pygame.K_r and self.game_over:
                    self.reset()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

    def update(self) -> None:
        if self.game_over:
            return

        self.snake.move()

        if self.snake.is_dead():
            self.game_over = True
            self.best_score = self.high_score_store.save_if_new_record(self.score)
            return

        if self.snake.head == self.food.position:
            self.snake.grow(1)
            self.score += 1
            self.best_score = self.high_score_store.save_if_new_record(self.score)
            self.food.respawn(self.snake)

    def current_fps(self) -> int:
        boost = self.score // FPS_STEP_EVERY
        return min(FPS_START + boost, FPS_MAX)

    def draw(self) -> None:
        self.screen.fill(COLOR_BG)

        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y))

        fx, fy = self.food.position
        pygame.draw.rect(
            self.screen,
            COLOR_FOOD,
            (fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

        for i, (x, y) in enumerate(self.snake.body):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            pygame.draw.rect(
                self.screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

        score_surface = self.font.render(
            f"Score: {self.score}   Best: {self.best_score}", True, COLOR_TEXT
        )
        self.screen.blit(score_surface, (8, 8))

        if self.game_over:
            msg = self.font.render(
                "Game over — R pour rejouer, Echap pour quitter", True, COLOR_TEXT
            )
            rect = msg.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(msg, rect)

        pygame.display.flip()

    def run(self) -> None:
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.current_fps())
