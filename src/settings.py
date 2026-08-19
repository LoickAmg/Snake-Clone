"""Constantes de configuration du jeu."""

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

FPS_START = 8
FPS_MAX = 20
FPS_STEP_EVERY = 5  # augmente la vitesse tous les N points

COLOR_BG = (17, 17, 17)
COLOR_GRID = (30, 30, 30)
COLOR_SNAKE_HEAD = (0, 200, 120)
COLOR_SNAKE_BODY = (0, 150, 90)
COLOR_FOOD = (220, 60, 60)
COLOR_TEXT = (240, 240, 240)

FONT_NAME = None  # police par défaut de pygame
