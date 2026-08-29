"""Constantes de configuration du jeu."""

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

FPS_START = 8
FPS_MAX = 20
FPS_STEP_EVERY = 5  # augmente la vitesse tous les N points

# Arcade palette: near-black field, phosphor snake and warm target.
COLOR_BG = (10, 18, 16)
COLOR_GRID = (22, 48, 42)
COLOR_SNAKE_HEAD = (119, 235, 145)
COLOR_SNAKE_BODY = (45, 177, 102)
COLOR_FOOD = (242, 132, 73)
COLOR_TEXT = (232, 245, 232)

FONT_NAME = None  # police par défaut de pygame
