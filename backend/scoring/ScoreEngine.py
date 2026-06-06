from backend.scoring.ScoreRule import ScoreRule
from backend.structure.Chair import Chair
from backend.structure.Vending_machine import Vending_machine
from backend.structure.Speaker import Speaker
from backend.structure.Water_fountain import Water_fountain
from backend.structure.Ramp import Ramp
from backend.structure.Scene import Scene
from backend.structure.Stand import Stand
from backend.structure.Tent import Tent
from backend.structure.Toilet import Toilet
from backend.structure.Bodyguard import Bodyguard
from frontend.Cell import CellState

RULES = [
    ScoreRule(Scene, Tent, -150, "Scène près de Tente -50"),
    ScoreRule(Scene, Chair, 50, "Scène près de Chaise +50"),
    ScoreRule(Scene, Bodyguard, 150, "Scène près d'un vigile +150"),
    ScoreRule(Scene, Toilet, -150, "Scène près de toilette -150"),
    ScoreRule(Scene, Ramp, 100, "Scène près de Rampe +100"),
    ScoreRule(Scene, Speaker, 150, "Scène près d'une enceinte +150"),
    ScoreRule(Tent, Vending_machine, 100, "Scène près d'un distributeur +100"),
    ScoreRule(Tent, Bodyguard, 150, "Scène près d'un bodyguard +150"),
    ScoreRule(Tent, Stand, 100, "Scène près d'un stand +100"),
    ScoreRule(Tent, Speaker, -150, "Scène près d'une enceinte -150"),
    ScoreRule(
        Vending_machine, Vending_machine, 50, "Distrib près d'un distributeur +50"
    ),
    ScoreRule(Tent, Vending_machine, 100, "Scène près d'un distributeur +100"),
    ScoreRule(Stand, Vending_machine, 150, "Stand près d'un distributeur +150"),
    ScoreRule(Bodyguard, Bodyguard, -200, "Vigile à coté d'un vigile +0 "),
    ScoreRule(Stand, Toilet, -100, "Stand près d'un toilet -100"),
    ScoreRule(Toilet, Toilet, 50, "Toilet près d'un toilet +50"),
    ScoreRule(Toilet, Water_fountain, +100, "fontaine près d'un toilet +100"),
    ScoreRule(Speaker, Speaker, -200, "Speaker près d'un Speaker -200"),
]


class ScoreEngine:
    def __init__(self, grid):
        self.grid = grid

    def _placed_elements(self):
        """Retourne la liste des (element, top_left_cell) uniques sur la grille."""
        seen = set()
        result = []
        for row in self.grid.cells:
            for cell in row:
                if cell.state == CellState.OCCUPIED and cell.is_top_left:
                    eid = id(cell.occupant)
                    if eid not in seen:
                        seen.add(eid)
                        result.append((cell.occupant, cell))
        return result

    def _occupied_cells(self, element):
        """Retourne toutes les cellules occupées par un élément donné."""
        cells = []
        for row in self.grid.cells:
            for cell in row:
                if cell.occupant is element:
                    cells.append(cell)
        return cells

    def _are_adjacent(self, elem_a, elem_b):
        """
        Retourne True si les deux éléments ont au moins une cellule adjacente
        (voisinage à 4 directions + diagonales = 8 directions).
        """
        cells_a = self._occupied_cells(elem_a)
        cells_b = self._occupied_cells(elem_b)
        positions_b = {(c.row, c.col) for c in cells_b}

        for ca in cells_a:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    if (ca.row + dr, ca.col + dc) in positions_b:
                        return True
        return False

    def compute(self):
        """
        Calcule le score total et retourne un dict :
        {
            'total'  : int,
            'base'   : int,       # somme des scores de base des éléments
            'bonus'  : int,       # somme des bonus/malus de proximité
            'details': [str, ...]  # lignes explicatives
        }
        """
        placed = self._placed_elements()
        base = sum(getattr(e, "score", 0) for e, _ in placed)

        bonus = 0
        details = []
        already_applied = set()

        for i, (elem_a, _) in enumerate(placed):
            for j, (elem_b, _) in enumerate(placed):
                if i >= j:
                    continue

                if not self._are_adjacent(elem_a, elem_b):
                    continue

                for rule in RULES:
                    if isinstance(elem_a, rule.source_type) and isinstance(
                        elem_b, rule.target_type
                    ):
                        key = (id(elem_a), id(elem_b), id(rule))
                        if key not in already_applied:
                            bonus += rule.bonus
                            details.append(rule.description)
                            already_applied.add(key)

                    if rule.bidirectional and rule.source_type != rule.target_type:
                        if isinstance(elem_b, rule.source_type) and isinstance(
                            elem_a, rule.target_type
                        ):
                            key = (id(elem_b), id(elem_a), id(rule))
                            if key not in already_applied:
                                bonus += rule.bonus
                                details.append(rule.description)
                                already_applied.add(key)

        total = base + bonus
        return {
            "total": total,
            "base": base,
            "bonus": bonus,
            "details": details,
        }
