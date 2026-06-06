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
        self.is_top_left = (
            False  # Indique si c'est la cellule "maître" qui affiche le nom
        )

    def set_available(self):
        if self.state != CellState.BLOCKED:
            self.state = CellState.AVAILABLE
            self.occupant = None
            self.is_top_left = False

    def occupy(self, occupant, is_top_left=False):
        if self.state != CellState.BLOCKED:
            self.state = CellState.OCCUPIED
            self.occupant = occupant
            self.is_top_left = is_top_left

    def block_cell(self):
        self.state = CellState.BLOCKED
        self.occupant = None
        self.is_top_left = False

    def _get_occupant_color(self):
        """Retourne une couleur selon le type de l'occupant."""
        if self.occupant is None:
            return (200, 0, 0)
        class_name = type(self.occupant).__name__
        color_map = {
            "Chair": (52, 152, 219),  # Bleu
            "Scene": (155, 89, 182),  # Violet
            "Ramp": (230, 126, 34),  # Orange
            "Vending_machine": (26, 188, 156),  # Turquoise
            "Speaker": (241, 196, 15),  # Jaune
            "Tent": (231, 76, 60),  # Rouge
            "Toilet": (149, 165, 166),  # Gris clair
            "Water_fountain": (52, 73, 94),  # Gris foncé
            "Stand": (39, 174, 96),  # Vert
            "Bodyguard": (44, 62, 80),  # Bleu nuit
        }
        return color_map.get(class_name, (200, 0, 0))

    def draw(self, screen):
        colors = {
            CellState.BLOCKED: (100, 100, 100),
            CellState.AVAILABLE: (220, 240, 220),
        }

        if self.state == CellState.OCCUPIED:
            color = self._get_occupant_color()
        else:
            color = colors[self.state]

        x = self.col * self.size
        y = self.row * self.size

        pygame.draw.rect(screen, color, (x, y, self.size, self.size))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, self.size, self.size), 1)

        # Afficher le nom uniquement sur la cellule "maître" (top-left du bloc)
        if self.state == CellState.OCCUPIED and self.is_top_left and self.occupant:
            occupant_width = getattr(self.occupant, "width", 1)
            occupant_height = getattr(self.occupant, "height", 1)

            block_pixel_w = occupant_width * self.size
            block_pixel_h = occupant_height * self.size

            class_name = type(self.occupant).__name__
            font_size = max(9, min(16, self.size // 2))
            font = pygame.font.SysFont("Arial", font_size, bold=True)
            text_surf = font.render(class_name, True, (255, 255, 255))

            # Centrer le texte dans le bloc complet
            text_x = x + (block_pixel_w - text_surf.get_width()) // 2
            text_y = y + (block_pixel_h - text_surf.get_height()) // 2
            screen.blit(text_surf, (text_x, text_y))

    def __repr__(self):
        return f"Cell(row={self.row}, col={self.col}, state={self.state.name}, occupant={self.occupant})"
