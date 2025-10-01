from enum import Enum, auto

import pygame


class CellState(Enum):
    BLOCKED = auto()
    AVAILABLE = auto()
    OCCUPIED = auto()


class Cell:
    def __init__(self, row, col, size, state=CellState.AVAILABLE, occupant=None):
        self.state = state
        self.row = row
        self.col = col
        self.size = size
        self.occupant = occupant
        self.hovered = False

    def set_available(self):
        if self.state != CellState.BLOCKED:
            self.state = CellState.AVAILABLE
            self.occupant = None

    def occupy(self, occupant):
        if self.state != CellState.BLOCKED:
            self.state = CellState.OCCUPIED
            self.occupant = occupant

    def block_cell(self):
        self.state = CellState.BLOCKED
        self.occupant = None

    def draw(self, screen):
        colors = {
            CellState.BLOCKED: (100, 100, 100),  # Gray
            CellState.AVAILABLE: (0, 200, 0),  # Green
            CellState.OCCUPIED: (200, 0, 0),  # Red
        }

        pygame.draw.rect(
            screen,
            colors[self.state],
            (self.col * self.size, self.row * self.size, self.size, self.size),
        )
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (self.col * self.size, self.row * self.size, self.size, self.size),
            1,
        )

    def __repr__(self):
        return f"Cell(id={self.id}, state={self.state.name}, occupant={self.occupant})"
